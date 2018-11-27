d = {"K":0,"Y":0}
seq = "KYRTWEEFTRAAEKLYQADPMKVRVVLKYRHCDG"
for aa in seq:
    try:
        d[aa] += 1
    except KeyError:
        d[aa] = 1

print(d)
