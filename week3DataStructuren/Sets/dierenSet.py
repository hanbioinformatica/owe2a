

boerderij = set(["Koe","Geit","Varken","Konijn","Konijn"])
dierentuin = set(["Olifant","Giraffe","Zebra", "Konijn","Geit"])

#print(boerderij)
#print(dierentuin)

print("Intersection")
print(boerderij.intersection(dierentuin))

print("Union")
print(boerderij.union(dierentuin))

print("Difference boerderij - dierentuin")
print(boerderij.difference(dierentuin))

print("Difference dierentuin - boerderij")
print(dierentuin.difference(dierentuin))