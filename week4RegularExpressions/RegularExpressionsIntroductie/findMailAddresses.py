import re

b = open("demo.txt", 'r')
for regel in b:
    if re.search(".*(@|\[at\]).*(\.|\[dot\])(com|nl|be)", regel):
        print(regel)
