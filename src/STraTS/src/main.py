import argparse
import os
from pathlib import Path
import sys
import pandas as pd
from utils import Logger, set_all_seeds
import torch
from dataset_pretrain import PretrainDataset
from dataset import Dataset
from modeling_strats import Strats
from modeling_gru import GRU_TS
from modeling_tcn import TCN_TS
from modeling_sand import SAND
from modeling_grud import GRUD_TS
from modeling_interpnet import InterpNet
import numpy as np
from tqdm import tqdm
from torch.optim import AdamW
from models import count_parameters
from evaluator import Evaluator
from evaluator_pretrain import PretrainEvaluator
from learning_curves import append_learning_curve_row, save_learning_curves
from artifact_metadata import (
    cohort_descriptor,
    validate_artifact_metadata,
)
from runtime_contract import (
    derive_dataset_seed,
    derive_effective_seed,
    validate_base_seed,
)
from checkpoint_runtime import (
    prepare_checkpoint_roles,
    validate_restored_dataset,
    write_runtime_metadata,
)

SRC_DIR = os.path.dirname(os.path.abspath(__file__))


def resolve_from_src(path: str | None) -> str | None:
    """Resolve relative paths as if they were passed from the src/ directory."""
    if path is None or os.path.isabs(path):
        return path
    return os.path.normpath(os.path.join(SRC_DIR, path))


def clear_cuda_cache(device: torch.device) -> None:
    if device.type == 'cuda':
        torch.cuda.empty_cache()


def save_run_learning_curves(args, history):
    if args.max_steps <= 0:
        args.logger.write(
            'Skipping learning-curve save because this invocation has '
            'no training steps; existing artifacts in output_dir are left untouched.'
        )
        return None
    if not history:
        args.logger.write(
            'Skipping learning-curve save because no evaluation rows were '
            'appended in this invocation; existing artifacts in output_dir are left untouched.'
        )
        return None
    return save_learning_curves(history, args.output_dir, logger=args.logger)


def format_summary_value(value):
    if value is None:
        return 'N/A'
    if isinstance(value, (bool, np.bool_)):
        return str(bool(value))
    if isinstance(value, (int, np.integer)):
        return str(int(value))
    if isinstance(value, (float, np.floating)):
        return f'{float(value):.6f}'
    return str(value)


def get_first_metric_value(results, keys):
    if results is None:
        return None
    for key in keys:
        value = results.get(key)
        if value is not None:
            return value
    return None


def write_metric_block(handle, title, results):
    handle.write(title + '\n')
    handle.write('-' * len(title) + '\n')
    handle.write(
        'loss: '
        + format_summary_value(get_first_metric_value(results, ['loss']))
        + '\n'
    )
    handle.write(
        'accuracy: '
        + format_summary_value(get_first_metric_value(results, ['accuracy', 'acc']))
        + '\n'
    )
    handle.write(
        'auroc: '
        + format_summary_value(get_first_metric_value(results, ['auroc', 'auc_roc']))
        + '\n'
    )
    handle.write(
        'f1: '
        + format_summary_value(get_first_metric_value(results, ['f1', 'f1_score']))
        + '\n'
    )
    for extra_key in ['loss_neg', 'auprc', 'minrp']:
        if results is not None and extra_key in results:
            handle.write(extra_key + ': ' + format_summary_value(results.get(extra_key)) + '\n')
    handle.write('\n')


def write_training_summary(args, output_path, best_val_res, best_test_res,
                           best_selection_metric_name):
    with open(output_path, 'w', encoding='utf-8') as handle:
        handle.write('Training Summary\n')
        handle.write('================\n')
        handle.write('dataset: ' + str(args.dataset) + '\n')
        handle.write('model_type: ' + str(args.model_type) + '\n')
        handle.write('output_dir: ' + str(args.output_dir) + '\n')
        handle.write('run: ' + str(args.run) + '\n')
        handle.write('train_frac: ' + format_summary_value(args.train_frac) + '\n')
        handle.write('pretrain: ' + format_summary_value(bool(args.pretrain)) + '\n\n')
        handle.write('checkpoint_selection_metric: '
                     + str(best_selection_metric_name) + '\n\n')
        write_metric_block(handle, 'Validation', best_val_res)
        write_metric_block(handle, 'Test', best_test_res)



def parse_args() -> argparse.Namespace:
    """Function to parse arguments."""
    parser = argparse.ArgumentParser()

    # dataset related arguments
    parser.add_argument('--dataset', type=str, default='physionet_2012')
    parser.add_argument('--latent_csv_path', type=str, default='../data/latent_tags.csv',
                        help='Path to latent tags CSV file')
    parser.add_argument('--processed_data_path', type=str, default=None,
                        help='Explicit split-aware processed pickle path')
    parser.add_argument('--train_frac', type=float, default=0.5)
    parser.add_argument('--run', type=str, default='1o10')

    parser.add_argument('--save_pred_csv_path', type=str, default=None,
                        help='Where to save predicted latent tags CSV')
    parser.add_argument('--predict_split', type=str, default='all',
                        choices=['train', 'val', 'test', 'all'],
                        help='Which split to export predictions for')

    # model related arguments
    parser.add_argument('--model_type', type=str, default='strats',
                        choices=['gru','tcn','sand','grud','interpnet',
                                 'strats','istrats'])
    parser.add_argument('--load_ckpt_path', type=str, default=None)
    parser.add_argument('--init_ckpt_path', type=str, default=None,
                        help='Pretraining checkpoint used only to initialize fine-tuning')
    parser.add_argument('--restore_ckpt_path', type=str, default=None,
                        help='Metadata-bound supervised checkpoint restored strictly')
    ##  strats and istrats
    parser.add_argument('--max_obs', type=int, default=880)
    parser.add_argument('--hid_dim', type=int, default=32)
    parser.add_argument('--num_layers', type=int, default=2)
    parser.add_argument('--num_heads', type=int, default=4)
    parser.add_argument('--dropout', type=float, default=0.2)
    parser.add_argument('--attention_dropout', type=float, default=0.2)
    ## gru: hid_dim, dropout
    ## tcn: dropout, filters=hid_dim
    parser.add_argument('--kernel_size', type=int, default=4)
    ## sand: num_layers, hid_dim, num_heads, dropout
    parser.add_argument('--r', type=int, default=24)
    parser.add_argument('--M', type=int, default=12)
    ## grud: hid_dim, dropout
    parser.add_argument('--max_timesteps', type=int, default=880)
    ## interpnet: hid_dim
    parser.add_argument('--hours_look_ahead', type=int, default=24)
    parser.add_argument('--ref_points', type=int, default=24)

    # training/eval realated arguments
    parser.add_argument('--pretrain', type=int, default=0)
    parser.add_argument('--output_dir', type=str, default=None)
    parser.add_argument('--output_dir_prefix', type=str, default='')
    parser.add_argument('--seed', type=int, default=2023)
    parser.add_argument('--base_seed', type=int, default=None)
    parser.add_argument('--dataset_seed', type=int, default=None)
    parser.add_argument('--pipeline_run_id', type=str, default='standalone')
    parser.add_argument('--config_fingerprint', type=str, default='legacy-standalone')
    parser.add_argument('--max_epochs', type=int, default=50)
    parser.add_argument('--patience', type=int, default=10)
    parser.add_argument('--lr', type=float, default=5e-4)
    parser.add_argument('--train_batch_size', type=int, default=16)
    parser.add_argument('--gradient_accumulation_steps', type=int, default=1)
    parser.add_argument('--eval_batch_size', type=int, default=32)
    parser.add_argument('--print_train_loss_every', type=int, default=100)
    parser.add_argument('--validate_after', type=int, default=-1)
    parser.add_argument('--validate_every', type=int, default=None)

    args = parser.parse_args()
    if args.load_ckpt_path is not None:
        if args.init_ckpt_path is not None or args.restore_ckpt_path is not None:
            raise ValueError('--load_ckpt_path cannot be combined with explicit checkpoint roles.')
        args.init_ckpt_path = args.load_ckpt_path
    if args.init_ckpt_path is not None and args.restore_ckpt_path is not None:
        raise ValueError('--init_ckpt_path and --restore_ckpt_path are mutually exclusive.')
    args.latent_csv_path = resolve_from_src(args.latent_csv_path)
    args.processed_data_path = resolve_from_src(args.processed_data_path)
    args.load_ckpt_path = resolve_from_src(args.load_ckpt_path)
    args.init_ckpt_path = resolve_from_src(args.init_ckpt_path)
    if args.processed_data_path is None:
        args.processed_data_path = os.path.normpath(os.path.join(SRC_DIR, '..', 'data', 'processed', args.dataset + '.pkl'))
    args.restore_ckpt_path = resolve_from_src(args.restore_ckpt_path)
    args.save_pred_csv_path = resolve_from_src(args.save_pred_csv_path)
    args.output_dir = resolve_from_src(args.output_dir)
    if args.base_seed is None:
        args.base_seed = args.seed
    args.base_seed = validate_base_seed(args.base_seed)
    if args.dataset_seed is None:
        args.dataset_seed = derive_dataset_seed(args.base_seed, args.dataset)
    args.dataset_seed = validate_base_seed(args.dataset_seed)
    args.seed = validate_base_seed(args.seed)
    args.effective_seed = derive_effective_seed(args.seed, args.run)
    if not args.pipeline_run_id:
        raise ValueError('pipeline_run_id must not be empty.')
    if not args.config_fingerprint:
        raise ValueError('config_fingerprint must not be empty.')
    args.finetune = False
    args.preprocessing_state_path = None
    args.restore_metadata = None
    args.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    return args


def export_latent_predictions(model, dataset, args):
    model.eval()

    if args.predict_split == 'train':
        pred_indices = dataset.splits['train']
    elif args.predict_split == 'val':
        pred_indices = dataset.splits['val']
    elif args.predict_split == 'test':
        pred_indices = dataset.splits['test']
    elif args.predict_split == 'all':
        pred_indices = np.arange(len(dataset.sup_ts_ids))
    else:
        raise ValueError(f"Unknown predict_split: {args.predict_split}")

    all_probs = []
    all_ts_ids = []

    batch_size = args.eval_batch_size

    with torch.no_grad():
        for start in range(0, len(pred_indices), batch_size):
            batch_ind = pred_indices[start:start + batch_size]
            batch = dataset.get_batch(batch_ind)
            batch.pop('labels', None)
            batch = {k: v.to(args.device) for k, v in batch.items()}
            probs = model(**batch)

            all_probs.append(probs.detach().cpu())
            all_ts_ids.extend([dataset.sup_ts_ids[i] for i in batch_ind])

    if not all_probs:
        raise ValueError('Prediction cohort is empty.')
    probs = torch.cat(all_probs, dim=0).numpy()
    if not np.isfinite(probs).all() or (probs < 0).any() or (probs > 1).any():
        raise ValueError('Model produced non-finite or out-of-range probabilities.')
    if len(all_ts_ids) != len(set(all_ts_ids)):
        raise ValueError('Prediction export produced duplicate canonical IDs.')
    if args.predict_split == 'all' and all_ts_ids != list(dataset.sup_ts_ids):
        raise ValueError('Full-cohort prediction order does not match the canonical cohort.')
    preds = (probs >= 0.5).astype(int)

    prob_cols = [f"{c}_prob" for c in dataset.target_columns]

    df_probs = pd.DataFrame(probs, columns=prob_cols)
    df_preds = pd.DataFrame(preds, columns=dataset.target_columns)
    df_out = pd.concat([pd.DataFrame({'ts_id': all_ts_ids}), df_probs, df_preds], axis=1)

    destination = Path(args.save_pred_csv_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(str(destination) + '.tmp')
    try:
        df_out.to_csv(temporary, index=False)
        os.replace(temporary, destination)
    finally:
        if temporary.exists():
            temporary.unlink()
    schema = {
        'columns': ['ts_id'] + prob_cols + list(dataset.target_columns),
        'probability_range': [0.0, 1.0],
        'binary_values': [0, 1],
    }
    write_runtime_metadata(
        args, dataset, str(destination),
        artifact_kind='prediction',
        schema=schema,
        producing_command=[sys.executable] + sys.argv,
        cohort_ids=all_ts_ids,
    )
    print(f"Saved predicted latent tags to: {args.save_pred_csv_path}")


def set_output_dir(args: argparse.Namespace) -> None:
    """Function to automatically set output dir 
    if it is not passed in args."""
    if args.output_dir is None:
        if args.pretrain:
            args.output_dir = os.path.join(
                SRC_DIR,
                '..',
                'outputs',
                args.dataset,
                args.output_dir_prefix + 'pretrain',
            )
        else:
            if args.init_ckpt_path is not None:
                args.output_dir_prefix = 'finetune_'+args.output_dir_prefix
            args.output_dir = os.path.join(
                SRC_DIR,
                '..',
                'outputs',
                args.dataset,
                args.output_dir_prefix,
            )
            args.output_dir += args.model_type
            if args.model_type=='strats':
                for param in ['num_layers', 'hid_dim', 'num_heads', 'dropout', 'attention_dropout', 'lr']:
                    args.output_dir += ','+param+':'+str(getattr(args, param))
            for param in ['train_frac', 'run']:
                args.output_dir += '|'+param+':'+str(getattr(args, param))
        args.output_dir = os.path.normpath(args.output_dir)
    os.makedirs(args.output_dir, exist_ok=True)


if __name__ == "__main__":
    # Preliminary setup.
    args = parse_args()
    if args.pretrain and args.model_type not in ['strats', 'istrats']:
        raise ValueError('Pretraining is only supported for model_type in {strats, istrats}.')
    set_output_dir(args)
    prepare_checkpoint_roles(args)
    args.logger = Logger(args.output_dir, 'log.txt')
    args.logger.write('\n'+str(args))
    set_all_seeds(args.effective_seed)
    model_path_best = os.path.join(args.output_dir, 'checkpoint_best.bin')

    # load data
    dataset = PretrainDataset(args) if args.pretrain==1 else Dataset(args)
    validate_restored_dataset(args, dataset)

    # load model
    model_class = {'strats':Strats, 'istrats':Strats, 'gru':GRU_TS, 'tcn':TCN_TS,
                   'sand':SAND, 'grud':GRUD_TS, 'interpnet':InterpNet}
    model = model_class[args.model_type](args)
    model.to(args.device)
    count_parameters(args.logger, model)
    if args.restore_ckpt_path is not None:
        restored_state = torch.load(args.restore_ckpt_path, map_location=args.device)
        model.load_state_dict(restored_state, strict=True)
        model.to(args.device)
    elif args.init_ckpt_path is not None:
        if not os.path.exists(args.init_ckpt_path):
            raise FileNotFoundError(f'Initialization checkpoint not found: {args.init_ckpt_path}.')
        curr_state_dict = model.state_dict()
        init_state_dict = torch.load(args.init_ckpt_path, map_location=args.device)
        compatible_count = 0
        for k, v in init_state_dict.items():
            if k in curr_state_dict and curr_state_dict[k].shape == v.shape:
                curr_state_dict[k] = v
                compatible_count += 1
        if compatible_count == 0:
            raise ValueError('Initialization checkpoint has no compatible model parameters.')
        model.load_state_dict(curr_state_dict, strict=True)
        model.to(args.device)
    # training loop
    checkpoint_saved_this_run = False
    num_train = len(dataset.splits['train'])
    num_batches_per_epoch = num_train/args.train_batch_size
    args.logger.write('\nNo. of training batches per epoch = '
                      +str(num_batches_per_epoch))
    if args.pretrain and args.eval_batch_size > args.train_batch_size:
        args.logger.write(
            'Reducing eval_batch_size from '
            + str(args.eval_batch_size)
            + ' to '
            + str(args.train_batch_size)
            + ' for pretraining to limit attention memory usage.'
        )
        args.eval_batch_size = args.train_batch_size
    args.max_steps = int(round(num_batches_per_epoch)*args.max_epochs)
    if args.validate_every is None:
        args.validate_every = int(np.ceil(num_batches_per_epoch))
    args.logger.write(
        'Learning-curve schedule: max_steps=' + str(args.max_steps)
        + ', num_batches_per_epoch=' + str(num_batches_per_epoch)
        + ', validate_after=' + str(args.validate_after)
        + ', validate_every=' + str(args.validate_every)
    )
    if args.max_steps <= 0:
        args.logger.write(
            'No training steps are scheduled. This run will not refresh '
            'learning-curve artifacts.'
        )
    elif args.validate_every > args.max_steps or args.validate_after > args.max_steps:
        args.logger.write(
            'The validation schedule has no guaranteed post-training validation '
            'before max_steps; check validate_after and validate_every if curves '
            'only show the initial row.'
        )
    cum_train_loss, num_steps, num_batches_trained = 0,0,0
    curve_train_loss_sum, curve_train_loss_count = 0.0, 0
    learning_curve_history = []
    wait, patience_reached = args.patience, False
    best_val_metric  = -np.inf
    best_val_res, best_test_res = None, None
    best_selection_metric_name = 'loss_neg' if args.pretrain else 'auprc + auroc'
    optimizer = AdamW(filter(lambda p:p.requires_grad, model.parameters()), lr=args.lr)
    train_bar = tqdm(range(args.max_steps))
    evaluator = PretrainEvaluator(args) if args.pretrain==1 else Evaluator(args)

    # results before any training
    if args.validate_after<0:
        val_res = evaluator.evaluate(model, dataset, 'val',  train_step=-1)
        if not(args.pretrain):
            evaluator.evaluate(model, dataset, 'eval_train', train_step=-1)
            test_res = evaluator.evaluate(model, dataset, 'test', train_step=-1)
        else:
            test_res = None
        clear_cuda_cache(args.device)
        append_learning_curve_row(
            learning_curve_history,
            train_step=0,
            epoch=0.0,
            recent_mean_train_loss=None,
            val_res=val_res,
            test_res=test_res,
            logger=args.logger,
        )
        save_run_learning_curves(args, learning_curve_history)

    model.train()
    for step in train_bar:
        # load batch
        batch = dataset.get_batch()
        batch = {k:v.to(args.device) for k,v in batch.items()}

        # forward pass
        loss = model(**batch)

        # backward pass
        if not torch.isnan(loss):
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(),0.3)
            if (step+1)%args.gradient_accumulation_steps==0:
                optimizer.step()
                optimizer.zero_grad()

        # add to cum loss
        loss_value = loss.item()
        cum_train_loss += loss_value
        curve_train_loss_sum += loss_value
        curve_train_loss_count += 1
        num_steps += 1
        num_batches_trained += 1

        # Log training losses.
        train_bar.set_description(str(np.round(cum_train_loss/num_batches_trained,5)))
        if (num_steps)%args.print_train_loss_every == 0:
            args.logger.write('\nTrain-loss at step '+str(num_steps)+': '
                              +str(cum_train_loss/num_batches_trained))
            cum_train_loss, num_batches_trained = 0, 0

        # run validatation
        if (num_steps>=args.validate_after) and (num_steps%args.validate_every==0):
            # get metrics on test and validation splits
            val_res = evaluator.evaluate(model, dataset, 'val', train_step=step)
            if not(args.pretrain):
                evaluator.evaluate(model, dataset, 'eval_train', train_step=step)
                test_res = evaluator.evaluate(model, dataset, 'test', train_step=step)
            else:
                test_res = None
            clear_cuda_cache(args.device)
            model.train(True)

            recent_curve_train_loss = None
            if curve_train_loss_count > 0:
                recent_curve_train_loss = curve_train_loss_sum / curve_train_loss_count
            epoch_estimate = None
            if num_batches_per_epoch > 0:
                epoch_estimate = num_steps / num_batches_per_epoch
            append_learning_curve_row(
                learning_curve_history,
                train_step=num_steps,
                epoch=epoch_estimate,
                recent_mean_train_loss=recent_curve_train_loss,
                val_res=val_res,
                test_res=test_res,
                logger=args.logger,
            )
            save_run_learning_curves(args, learning_curve_history)
            curve_train_loss_sum, curve_train_loss_count = 0.0, 0

            # Save ckpt if there is an improvement.
            curr_val_metric = val_res['loss_neg'] if args.pretrain \
                                else val_res['auprc'] + val_res['auroc']
            if curr_val_metric>best_val_metric:
                best_val_metric = curr_val_metric
                best_val_res, best_test_res = val_res, test_res
                args.logger.write('\nSaving ckpt at ' + model_path_best)
                torch.save(model.state_dict(), model_path_best)
                write_runtime_metadata(
                    args, dataset, model_path_best,
                    artifact_kind='checkpoint',
                    schema={'format': 'pytorch_state_dict', 'version': 1},
                    producing_command=[sys.executable] + sys.argv,
                )
                checkpoint_saved_this_run = True
                wait = args.patience
            else:
                wait -= 1
                args.logger.write('Updating wait to '+str(wait))
                if wait==0:
                    args.logger.write('Patience reached')
                    break

    save_run_learning_curves(args, learning_curve_history)

    # print final res
    args.logger.write('Final val res: '+str(best_val_res))
    args.logger.write('Final test res: '+str(best_test_res))
    if args.max_steps > 0:
        summary_path = os.path.join(args.output_dir, 'training_summary.txt')
        write_training_summary(
            args,
            summary_path,
            best_val_res,
            best_test_res,
            best_selection_metric_name,
        )
        args.logger.write('Saved training summary to: ' + summary_path)

    if args.save_pred_csv_path is not None:
        if args.restore_ckpt_path is None:
            if not checkpoint_saved_this_run:
                raise RuntimeError('Prediction export requires a verified current-run checkpoint.')
            validate_artifact_metadata(
                model_path_best,
                expected={
                    'artifact_kind': 'checkpoint',
                    'pipeline_run_id': args.pipeline_run_id,
                    'dataset': args.dataset,
                    'model': args.model_type,
                    'ordered_targets': list(dataset.target_columns),
                    'cohort': cohort_descriptor(dataset.metadata_cohort_ids),
                },
            )
            current_state = torch.load(model_path_best, map_location=args.device)
            model.load_state_dict(current_state, strict=True)
        export_latent_predictions(model, dataset, args)
