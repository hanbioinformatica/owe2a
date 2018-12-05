import re
scientific_name = "Urtica dioica"

m = re.search("([A-Z][a-z]*) ([a-z]+)", scientific_name)

if m:
    genus = m.group(1)
    species = m.group(2)
    print("genus is " + genus + ", species is " + species)

