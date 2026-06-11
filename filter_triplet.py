#!/usr/bin/env python3

import sys

if len(sys.argv) != 5:
    sys.exit(
        f"Usage: python {sys.argv[0]} <input.txt> <species1> <species2> <output.txt>"
    )

infile = sys.argv[1]
sp1 = sys.argv[2]
sp2 = sys.argv[3]
outfile = sys.argv[4]

with open(infile) as fin, open(outfile, "w") as fout:

    header = fin.readline()
    fout.write(header)

    for line in fin:
        line = line.rstrip()

        if not line:
            continue

        fields = line.split(",")

        triplet = fields[0]
        outgroup = fields[1]

        species = triplet.split("_")

        # triplet必须同时包含两个目标物种
        if sp1 not in species:
            continue

        if sp2 not in species:
            continue

        # outgroup不能是目标物种
        if outgroup == sp1 or outgroup == sp2:
            continue

        fout.write(line + "\n")
