import pandas as pd
import re

modification_map = {
    15.99: "[UNIMOD:35]",
    57.02: "[UNIMOD:4]",
    0.98: "[UNIMOD:7]",
    79.97: "[UNIMOD:21]",
    42.01: "[UNIMOD:1]",
    43.01: "[UNIMOD:5]",
    -17.03: "[UNIMOD:385]"
}

def closest_modification(value):
    min_diff = float('inf')
    closest_value = None
    for mod_value in modification_map:
        diff = abs(value - mod_value)
        if diff < min_diff:
            min_diff = diff
            closest_value = modification_map[mod_value]
    return closest_value

def replace_bracket(match):

    content = match.group(0)
    inner = content[1:-1]

    mods = re.findall(r"[+-]?\d+\.\d+", inner)

    replaced = ""
    for m in mods:
        value = float(m)
        replacement = closest_modification(value)
        replaced += replacement if replacement else f"[{m}]"

    return replaced

def modify_preds(preds):
    return re.sub(r"\[[^\]]+\]", replace_bracket, preds)

def main():
    excel_file = "Mouse.xlsx"
    output_file = "Mouse_modified.xlsx"

    df = pd.read_excel(excel_file)

    if 'preds' not in df.columns:
        raise ValueError("Excel must contain 'preds' ")

    df['preds'] = df['preds'].apply(modify_preds)
    df.to_excel(output_file, index=False)

    print(f"Saved ：{output_file}")

if __name__ == "__main__":
    main()
