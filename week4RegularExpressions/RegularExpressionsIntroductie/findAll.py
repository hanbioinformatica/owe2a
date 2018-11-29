import re
patroon = "tata"
gevonden = re.findall (patroon, "atgagataggagatataatcacactataataaaa")

print (gevonden)
