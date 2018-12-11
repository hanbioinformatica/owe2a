import re

def main():
    find_consensus_pattern()


def find_consensus_pattern():
    bestand = open("genome_e.coli.fasta","r")
    seq = ""
    promoter = "TATA"
    startcodon = "ATG"
    stopcodon = "(TAA|TAG|TGA)"

    searchterm = (promoter + "[ATGC]{10,25}" + startcodon + "([ATGC]{3})*" + stopcodon)
    print(searchterm)
    line = bestand.readline()
    print ("Zoeken naar...")
    print (line)
    for line in bestand:
        seq += line.strip("\n")
    vinden = re.search('TTGACA[ATGC]{20,25}TATAAT([ATGC]{3})*ATG([ATGC]{3})*(TAA|TAG|TGA)', seq)
    print(vinden)    x = vinden.span()

    print (seq[int(x[0]):int(x[0]+100)]+"...")

main()