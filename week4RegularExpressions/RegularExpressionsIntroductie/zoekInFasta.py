# Patroonn voor p53 https://prosite.expasy.org/cgi-bin/prosite/prosite_browse.cgi?order=hits%20desc&type=all
# Gebruikt bestand: https://www.uniprot.org/downloads


import re
patroon = "MCNSSC[MV]GGMNRR"



bestand = open ("uniprot_sprot.fasta","r")
for regel in bestand:
    if regel.startswith(">"):
        titel = regel
    else:
        gevonden = re.search(patroon, regel)
        if gevonden:
            print(titel)
            print("Gevonden {}".format(regel))


