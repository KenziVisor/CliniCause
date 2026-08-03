from pathlib import Path

path = Path(r'c:\Users\kobik\Desktop\הנדסת מערכות תקשורת\תואר שני\תזה\code\CliniCause\causal-irregular-time-series\src\preprocess_mimic_iii_large.py')
text = path.read_text(encoding='utf-8')
lines = text.splitlines()
start = next(i for i,l in enumerate(lines) if l.strip() == 'return parser.parse_args()')
main = next(i for i,l in enumerate(lines) if l.strip() == 'def main():')
new_block = [
    '',
    'def main():',
    '    global RAW_DATA_PATH, OUTPUT_PATH',
    '    _ARGS = parse_args()',
    '    RAW_DATA_PATH = _ARGS.raw_data_path or RAW_DATA_PATH',
    '    OUTPUT_PATH = _ARGS.output_path or OUTPUT_PATH',
    '    print("=== Starting MIMIC-III preprocessing ===")',
    '    print(f"Raw data root: {os.path.abspath(RAW_DATA_PATH)}")',
    '    print(f"Output artifact: {os.path.abspath(OUTPUT_PATH)}")',
    '',
    '    # Get all ICU stays.',
    '    log_stage(1, "Loading ICU stays and patient demographics")',
    '    icu = pd.read_csv(os.path.join(RAW_DATA_PATH, "ICUSTAYS.csv"),',
    '                      usecols=["SUBJECT_ID", "HADM_ID", "ICUSTAY_ID",',
    '                               "INTIME", "OUTTIME"])',
    '    icu = icu.loc[icu.INTIME.notna()]',
    '    icu = icu.loc[icu.OUTTIME.notna()]',
]
new_lines = lines[:start+1] + new_block + lines[main+1:]
path.write_text("\n".join(new_lines) + "\n", encoding='utf-8')
print('Wrote fixed file')
