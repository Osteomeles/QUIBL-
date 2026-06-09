#!/usr/bin/env python3
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
target1 = sys.argv[3]
target2 = sys.argv[4]

target_set = {target1, target2}

kept = 0
total = 0

with open(input_file, "r") as fin, open(output_file, "w") as fout:
    for line in fin:
        line = line.strip()
        if not line:
            continue

        cols = line.split(",")
        triplet = cols[0]
        outgroup = cols[1]

        total += 1

        # split triplet species
        species = set(triplet.split("_"))

        # 条件1：必须包含目标pair
        if not target_set.issubset(species):
            continue

        # 条件2：outgroup不能是目标pair之一
        if outgroup in target_set:
            continue

        fout.write(line + "\n")
        kept += 1

print(f"[INFO] total lines: {total}")
print(f"[INFO] kept lines: {kept}")
print(f"[INFO] output: {output_file}")
