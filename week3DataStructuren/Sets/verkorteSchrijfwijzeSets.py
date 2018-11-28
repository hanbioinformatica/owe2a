getallen1 = set([1,4,5,9])
#getallen1 = {1,4,5,9} # alternatieve schrijfwijze
getallen2 = set([4,8,3,1])
#getallen2 = {4,8,3,1} # alternatieve schrijfwijze

print("Bepalen intersection")
print(getallen1.intersection(getallen2))
print(getallen1&getallen2) # alternatieve schrijfwijze

print("Bepalen union")
print(getallen1.union(getallen2))
print(getallen1|getallen2) # alternatieve schrijfwijze


print("Bepalen verschil")
print(getallen1.difference(getallen2))
print(getallen1-getallen2) # alternatieve schrijfwijze


