import pandas as pd

def normalize(seq: str) -> str:
    if pd.isna(seq):
        return ""
    return seq.replace("I", "L")

def compare(seq1: str, seq2: str) -> int:

    return int(normalize(seq1) == normalize(seq2))

def main():
    file_path = "Mouse_predictions.xlsx"
    df = pd.read_excel(file_path)




    required_cols = ["GroundTruth", "diffusion_predictions", "transformer_predictions", "final_prediction"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Lack COL: {col}")



    df["GND=Tran"] = [compare(gt, tran) for gt, tran in zip(df["GroundTruth"], df["transformer_predictions"])]
    print("GND=Tran done")
    df["GND=DIFF"] = [compare(gt, diff) for gt, diff in zip(df["GroundTruth"], df["diffusion_predictions"])]
    print("GND=DIFF done")
    df["GND=Final"] = [compare(gt, final) for gt, final in zip(df["GroundTruth"], df["final_prediction"])]
    print("GND=Final done")


    out_path = "Methanosarcina-mazei_V2_InstaNovo.xlsx"   #172,584,193
    df.to_excel(out_path, index=False)
    print(f"Saved: {out_path}")

if __name__ == "__main__":
    main()
