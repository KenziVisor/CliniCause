import importlib.util
import pathlib
import sys
from types import SimpleNamespace

spec = importlib.util.spec_from_file_location('router', pathlib.Path('router.py'))
router = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = router
spec.loader.exec_module(router)

context_physionet = SimpleNamespace(
    args=SimpleNamespace(python_executable='python', preprocess_chunksize=500000, tmp_dir='/tmp/preprocess', dry_run=False, skip_existing=False),
    thesis_repo_root=pathlib.Path('.'),
    datasets={'physionet': SimpleNamespace(resolved_config_csv=pathlib.Path('config.csv'), thesis_processed_pkl=pathlib.Path('out.pkl'))},
)
command_physionet = router.build_preprocessing_command('physionet', context_physionet)
print('physionet_has_chunksize', '--chunksize' in command_physionet)
print(command_physionet)

context_mimic = SimpleNamespace(
    args=SimpleNamespace(python_executable='python', preprocess_chunksize=500000, tmp_dir='/tmp/preprocess', dry_run=False, skip_existing=False),
    thesis_repo_root=pathlib.Path('.'),
    datasets={'mimic': SimpleNamespace(resolved_config_csv=pathlib.Path('config.csv'), thesis_processed_pkl=pathlib.Path('out.pkl'))},
)
command_mimic = router.build_preprocessing_command('mimic', context_mimic)
print('mimic_has_chunksize', '--chunksize' in command_mimic)
print(command_mimic)
