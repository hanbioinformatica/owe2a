dict_aa = {"A":0,"Y":0}
seq = "GATGAGJHTYYYYHKTRBJNKRBJNLRBLRBGB"
for aa in seq:
    # try:
    #     dict_aa[aa]+=1
    # except KeyError:
    #     dict_aa[aa]=1

    if aa in dict_aa.keys():
        dict_aa[aa] += 1
    else:
        dict_aa[aa] = 1

print (dict_aa)
