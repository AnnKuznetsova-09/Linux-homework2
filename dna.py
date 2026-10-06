#!/usr/bin/python3
import sys


dna = sys.argv.upper()


complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
rev_comp = " ".join(complement[base] for base in reversed(dna))


rna = dna.replace("T", "U")


start_pos = dna.find("ATG")
if start_pos != -1:
    start_pos += 1
else:
    start_pos = -1

print(rev_comp, rna, start_pos)

