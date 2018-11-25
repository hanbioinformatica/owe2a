aantal = {}
seq = "TCTCCAAGACGCATCCCAGTGG"
for i in range(0, len(seq) - len(seq)%3, 3):
  codon = seq[i:i+3]
  print (codon)
  aantal[codon] = 0
  aantal[codon] = aantal[codon] + 1
print (aantal)



