import random

with open('data/karty.txt', encoding='utf-8') as vstup:
  radky = vstup.readlines()

random.shuffle(radky)
karty = radky[:4]
karty = [karta.strip().split() for karta in karty]
# Zkopírováno z minulé úložky
hodnoty = [str(karta[0]).replace("kluk", "10").replace("dáma", "10").replace("král", "10").replace("eso", "1") for karta in karty]
hodnoty = [int(hodnota) for hodnota in hodnoty]
print(karty)
print(sum(hodnoty))
