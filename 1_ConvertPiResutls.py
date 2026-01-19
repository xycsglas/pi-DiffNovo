import csv
import math
from openpyxl import Workbook

input_tsv = "denovo.tsv"
output_xlsx = "Mouse.xlsx"


wb = Workbook()
ws = wb.active
ws.title = "Sheet1"

headers = [
    "label",
    "preds",
    "charge",
    "score",
    "log_probs",
    "spectrum_id",
]
ws.append(headers)


with open(input_tsv, "r", newline="") as fin:
    reader = csv.DictReader(fin, delimiter="\t")

    for idx, row in enumerate(reader):
        score = float(row["score"])

        ws.append([
            row["label"],
            row["prediction"],      # preds
            row["charge"],
            score,
            math.log10(score),
            f"peaks.db:{idx}",
        ])


wb.save(output_xlsx)
