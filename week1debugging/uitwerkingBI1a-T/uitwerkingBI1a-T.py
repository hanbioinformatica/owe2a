


def main():
    # gemiddelde_lengte("chr1_oefenbestand.csv")
    groter_gc_perc_dan("chr1_oefenbestand.csv")


def aantal_genen(bestandsnaam):
    aantal = -1
    bestand = open(bestandsnaam)
    for regel in bestand:
        aantal += 1
    print(aantal)


def gemiddelde_lengte(bestandsnaam):
    bestand = open(bestandsnaam)
    totaal = 0
    aantal = 0
    for regel in bestand:
        lijst = regel.split("\t")
        # print (lijst)
        start = int(lijst[3])
        eind = int(lijst[4])
        lengte = eind - start
        print(lengte)
        aantal += 1
        totaal += lengte
    print(totaal / aantal)


def groter_gc_perc_dan(bestandsnaam, gc=50):
    bestand = open(bestandsnaam)
    aantal = 0
    for regel in bestand:
        lijst = regel.split("\t")
        gc_perc = float(lijst[5].rstrip("\n"))
        if gc_perc >= gc:
            aantal += 1
    print(aantal)


main()
