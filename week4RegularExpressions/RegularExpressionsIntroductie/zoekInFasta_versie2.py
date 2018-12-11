# Patroon voor p53 https://prosite.expasy.org/cgi-bin/prosite/prosite_browse.cgi?order=hits%20desc&type=all
# Gebruikt bestand: https://www.uniprot.org/downloads


import re
patroon = ".*[LIVMFE][FY]PWM[KRQTA].*"
patroon = ".*C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H.*"



bestand = open ("uniprot_sprot.fasta","r")
aantal = 0
aantal_gevonden = 0
seq = ""
for regel in bestand:
    if regel.startswith(">"):
        gevonden = re.search(patroon, seq)
        aantal +=1
        if gevonden:
            aantal_gevonden += 1
            print(titel.strip("\n"))
            print("Gevonden {} {}".format(aantal_gevonden, seq))
            print()
        #reset titel en seq
        titel = regel
        seq = ""
    else:
        seq += regel.strip("\n")

print (aantal)


