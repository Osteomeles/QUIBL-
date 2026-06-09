#!/usr/bin/env python3
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

pairs = set()

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        cols = line.split(",")
        triplet = cols[0]
        outgroup = cols[1]

        # 拆分三元组
        species = triplet.split("_")

        # 去掉 outgroup
        remaining = [x for x in species if x != outgroup]

        # sanity check（应该剩2个）
        if len(remaining) != 2:
            continue

        # 排序保证无方向性
        remaining.sort()

        # 变成标准 pair key
        pair = f"{remaining[0]} {remaining[1]}"

        pairs.add(pair)

# 输出
with open(output_file, "w") as out:
    for p in sorted(pairs):
        out.write(p + "\n")

print(f"[INFO] unique pairs: {len(pairs)}")
print(f"[INFO] written to {output_file}")
