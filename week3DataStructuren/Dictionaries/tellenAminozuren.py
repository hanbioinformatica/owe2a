aantal = {}
seq = "KYRTWEEFTRAAEKLYQADPMKVRVVLKYRHCDG"
for aa in seq:
    try:
        aantal[aa] += + 1
    except KeyError:
        aantal[aa]=1
print (aantal)
