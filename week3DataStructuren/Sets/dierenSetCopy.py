

boerderij1 = set(["Koe","Geit"])
boerderij2 = boerderij1
boerderij1.add ("Varken")
boerderij2.add ("Schaap")
print(boerderij1)
print(boerderij2)


boerderij1 = set(["Koe","Geit"])
boerderij2 = boerderij1.copy()
boerderij1.add ("Varken")
boerderij2.add ("Schaap")
print(boerderij1)
print(boerderij2)
