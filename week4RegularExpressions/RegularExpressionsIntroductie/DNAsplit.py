import re

dna = "ATGGAGACCACACCACATTATGGAGACCATTAGAGG"
pattern = "([ATGC]{3})"
print (re.split(pattern,dna))