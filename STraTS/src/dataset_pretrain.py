import pickle
import numpy as np
from utils import CycleIndex
import torch
from dataset import (
    Dataset,
    _canonicalize_id_array,
    normalize_id_column,
)
from split_contract import (
    require_ids_present,
    require_no_excluded_indices,
    validate_split_contract,
)
import os

SRC_DIR = os.path.dirname(os.path.abspath(__file__))

class PretrainDataset(Dataset):
    def __init__(self, args):
        # read data
        filepath = getattr(args, 'processed_data_path', None)
        if filepath is None:
            filepath = os.path.join(SRC_DIR, '..', 'data', 'processed', args.dataset + '.pkl')
        filepath = os.path.normpath(filepath)
        data, oc, train_ids, val_ids, test_ids = pickle.load(open(filepath,'rb'))
        data = normalize_id_column(data, 'processed events')
        oc = normalize_id_column(oc, 'processed outcomes')
        if data['ts_id'].isna().any():
            raise ValueError('processed events contains missing canonical stay identifiers.')
        if oc['ts_id'].isna().any():
            raise ValueError('processed outcomes contains missing canonical stay identifiers.')
        train_ids = _canonicalize_id_array(train_ids, 'train_ids')
        val_ids = _canonicalize_id_array(val_ids, 'val_ids')
        test_ids = _canonicalize_id_array(test_ids, 'test_ids')
        validated_splits = validate_split_contract(
            data['ts_id'].tolist(), oc['ts_id'].tolist(),
            train_ids, val_ids, test_ids,
        )
        train_ids = np.asarray(validated_splits.train, dtype=object)
        val_ids = np.asarray(validated_splits.val, dtype=object)
        test_ids = np.asarray(validated_splits.test, dtype=object)
        args.logger.write('\nPreparing dataset '+args.dataset)
        static_varis = self.get_static_varis(args.dataset)
        if args.dataset=='mimic_iii':
            data = data.loc[(data.minute>=0)&(data.minute<=5*24*60)]
            data.loc[(data.variable=='Age')&(data.value>200), 'value'] = 91.4
            self.max_minute = 24*60
        elif args.dataset=='physionet_2012':
            self.max_minute = 48*60

        # Preserve the authoritative train/validation split and remove test data.
        data = data.loc[~data.ts_id.isin(test_ids)]

        # keep variables seen in training set only
        train_variables = data.loc[data.ts_id.isin(train_ids)].variable.unique()
        all_variables = data.variable.unique()
        delete_variables = np.setdiff1d(all_variables, train_variables)
        args.logger.write('Removing variables not in training set: '+str(delete_variables))
        data = data.loc[data.variable.isin(train_variables)]
        require_ids_present(
            np.concatenate((train_ids, val_ids)), data.ts_id.unique(),
            'Pretraining time/variable filtering',
        )
        args.logger.write('# train, val TS: '+str([len(train_ids), len(val_ids)]))
        unsup_ts_ids = np.concatenate((train_ids, val_ids))
        ts_id_to_ind = {ts_id:i for i,ts_id in enumerate(unsup_ts_ids)}
        data['ts_ind'] = data['ts_id'].map(ts_id_to_ind)
        N = len(unsup_ts_ids)

        # to save
        self.N = N
        self.args = args
        self.static_varis = static_varis
        self.splits = {'train':[ts_id_to_ind[i] for i in train_ids],
                       'val':[ts_id_to_ind[i] for i in val_ids]}
        self.metadata_cohort_ids = list(unsup_ts_ids)
        self.target_columns = []
        self.authoritative_splits = validated_splits
        
        # Get static data with missingness indicator.
        data = self.get_static_data(data)

        # normalize ts variables
        means_stds = data.loc[data.ts_id.isin(train_ids)].groupby(
                                'variable').agg({'value':['mean', 'std']})
        means_stds.columns = [col[1] for col in means_stds.columns]
        means_stds.loc[means_stds['std']==0, 'std'] = 1
        data = data.merge(means_stds.reset_index(), on='variable', how='left')
        data['value'] = (data['value']-data['mean'])/data['std']

        # prepare time series inputs
        variables = data.variable.unique()
        pickle.dump([variables, means_stds, self.max_minute], 
                    open(os.path.join(args.output_dir, 'pt_saved_variables.pkl'),'wb'))
        var_to_ind = {v:i for i,v in enumerate(variables)}
        V = len(variables)
        args.V = V
        args.logger.write('# TS variables: '+str(V))
        values = [[] for i in range(N)]
        times = [[] for i in range(N)]
        varis = [[] for i in range(N)]
        data = data.sample(frac=1).sort_values(by='minute')
        for row in data.itertuples():
            values[row.ts_ind].append(row.value)
            times[row.ts_ind].append(row.minute)
            varis[row.ts_ind].append(var_to_ind[row.variable])
        self.values, self.times, self.varis = values, times, varis

        # remove any samples with single timestamp
        self.timestamps = [np.array(sorted(list(set(x)))[:-1]) for x in self.times]
        self.timestamps = [x[x>=720] for x in self.timestamps] # atleast 12 hrs
        delete = [i for i in range(self.N) if len(self.timestamps[i])==0]
        require_no_excluded_indices(
            unsup_ts_ids, delete,
            'Pretraining forecast-window eligibility',
        )
        self.train_cycler = CycleIndex(self.splits['train'], args.train_batch_size)
        self.V = args.V
        self.max_obs = args.max_obs

    def get_batch(self, ind=None):
        if ind is None:
            ind = self.train_cycler.get_batch_ind()
        bsz = len(ind)
        input_values = []
        input_times = []
        input_varis = []
        forecast_values = torch.zeros((bsz,self.V))
        forecast_mask = torch.zeros((bsz,self.V), dtype=torch.int)
        for b,i in enumerate(ind):
            t1 = np.random.choice(self.timestamps[i]) # minutes
            curr_times = self.times[i]
            for ix in range(len(curr_times)-1,-1,-1):
                if curr_times[ix]==t1:
                    t1_ix = ix+1 # start of prediction window
                    break
            t0_ix = max(0,t1_ix-self.max_obs)
            if self.args.dataset=='mimic_iii': # obs window max length is 24 hrs
                while curr_times[t0_ix]<t1-self.max_minute:
                    t0_ix += 1
            if self.args.dataset=='mimic_iii' and t1>self.max_minute: # shift times
                diff = t1-self.max_minute
                input_times.append(list(np.array(self.times[i][t0_ix:t1_ix])-diff))
            else:
                input_times.append(self.times[i][t0_ix:t1_ix])
            input_values.append(self.values[i][t0_ix:t1_ix])
            input_varis.append(self.varis[i][t0_ix:t1_ix])
            t2 = t1+120 # prediction window is 2 hrs
            for t2_ix in range(t1_ix, len(curr_times)):
                if curr_times[t2_ix]>t2:
                    break
            # t2_ix: last+1 for prediction window
            curr_varis = self.varis[i]
            curr_values = self.values[i]
            for ix in range(t2_ix-1,t1_ix-1,-1):
                vari = curr_varis[ix]
                val = curr_values[ix]
                forecast_mask[b,vari] = 1
                forecast_values[b,vari] = val

        num_obs = list(map(len, input_values))
        max_obs = max(num_obs)
        pad_lens = max_obs-np.array(num_obs)
        values = [x+[0]*(l) for x,l in zip(input_values,pad_lens)]
        times = [x+[0]*(l) for x,l in zip(input_times,pad_lens)]
        varis = [x+[0]*(l) for x,l in zip(input_varis,pad_lens)]
        values, times = torch.FloatTensor(values), torch.FloatTensor(times)
        times = times/self.max_minute*2-1
        varis = torch.IntTensor(varis)
        obs_mask = [[1]*l1+[0]*l2 for l1,l2 in zip(num_obs,pad_lens)]
        obs_mask = torch.IntTensor(obs_mask)
        return {'values':values, 'times':times, 'varis':varis,
                'obs_mask':obs_mask, 
                'demo':torch.FloatTensor(self.demo[ind]),
                'forecast_values':forecast_values,
                'forecast_mask':forecast_mask}


        


            
            
