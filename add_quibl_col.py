#!/usr/bin/env python3

import csv
import sys
from collections import defaultdict

if len(sys.argv) != 3:
    sys.exit(
        f"Usage: python {sys.argv[0]} input.txt output.txt"
    )

infile = sys.argv[1]
outfile = sys.argv[2]

# ---------- 第一遍：统计每个triplet总count ----------

triplet_total_count = defaultdict(float)
rows = []

with open(infile) as f:
    reader = csv.DictReader(f)

    for row in reader:
        rows.append(row)

        triplet = row["triplet"]

        try:
            count = float(row["count"])
        except:
            count = 0

        triplet_total_count[triplet] += count

# ---------- 第二遍：计算新增三列 ----------

new_header = list(rows[0].keys()) + [
    "diffBIC",
    "totalILSProp",
    "totalIntroProp"
]

with open(outfile, "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(new_header)

    for row in rows:

        triplet = row["triplet"]

        mixprop1 = float(row["mixprop1"])
        mixprop2 = float(row["mixprop2"])

        bic2 = float(row["BIC2Dist"])
        bic1 = float(row["BIC1Dist"])

        count = float(row["count"])

        total_count = triplet_total_count[triplet]

        diffBIC = bic2 - bic1

        if total_count > 0:
            totalILSProp = mixprop1 * count / total_count
            totalIntroProp = mixprop2 * count / total_count
        else:
            totalILSProp = 0
            totalIntroProp = 0

        writer.writerow(
            list(row.values())
            + [
                diffBIC,
                totalILSProp,
                totalIntroProp
            ]
        )

print(f"Output written to {outfile}")
