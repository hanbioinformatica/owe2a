from typing import Set

boerderij: Set[str]  = set(["Koe","Geit","Varken","Konijn","Konijn"])
dierentuin = set(["Olifant","Giraffe","Zebra", "Konijn","Geit"])

print(boerderij.difference(dierentuin))

print(boerderij.symmetric_difference(dierentuin))
