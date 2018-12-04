import re

dna = "CGATNCGGAACGATC"
m = re.search(r"[^ATGC]", dna)

if m:
    print("Een foute nucleotide gevonden")
    print("Nucleotide " + m.group())
    print("Op positie " + m.start())