aantal = {}
seq = "TCTTCTCCAAGACGCATCCCAGTGG"
for i in range(0, len(seq) - len(seq)%3, 3):
  codon = seq[i:i+3]
  try:
    aantal[codon] += + 1
  except KeyError:
    aantal[codon] = 1
print (aantal)



