import re

dna = "CGATXCGGAACYGATC"
m = re.search(r"[^ATGC]", dna.upper())

if m:
    print("Een foute nucleotide gevonden")
    print("Nucleotide ", m.group())
    print("Op positie ", m.start())