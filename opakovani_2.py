import json
with open("battles.tsv", encoding="utf-8") as vstup:
    radky = vstup.readlines()
data = []
vitezni_velitele = []
statistika_vitezu = {}
for radek in radky[1:]:
    radek_seznam = radek.split("\t")
    attackers = radek_seznam[5:9]
    attackers = [x for x in attackers if len(x) > 0]
    defenders = radek_seznam[9:13]
    defenders = [x for x in defenders if len(x) > 0]
    if radek_seznam[13] == "win":
        winners = attackers
    else:
        winners = defenders
    
    """
    Statistika vítězů - zde 
    https://kodim.cz/czechitas/progr2-python/zaklady-programovani-2/slovniky/#o-slovnicich
    """
    for winner in winners:
        # Vítěz už ve statistice je - připočtu mu jedno vítězství
        if winner in statistika_vitezu:
            statistika_vitezu[winner] += 1
        # Vítěz ve statistice není - je to jeho první vítězství
        else:
            statistika_vitezu[winner] = 1
    """
    Kontrolujeme vítězství proti přesile.
    Pro zjednodušení používám výraz and -> obě podmínky musí být splněné, aby byla celá
    podmínka vyhodnocená jako pravda.
    """
    if len(radek_seznam[17]) > 0 and len(radek_seznam[18]) > 0:
        # Útočník měl menší armádu než obránce
        if float(radek_seznam[17]) < float(radek_seznam[18]):
            # Jestliže útočník vyhrál
            if radek_seznam[13] == "win":
                """
                Přidám velitele útočníků do seznamu velitelů, kteří vyhráli proti přesile.
                Můžu použít metodu append
                """
                # vitezni_velitele.append(radek_seznam[19])
                """
                Je tu jedna nepřesnost - někdy bylo v bitvě více velitelů. Můžu zde
                použít opět metodu split a seznam vítězných velitelů v aktální bitvě 
                přičíst k seznamu vítězných velitelů. Ukazovali jsme si to na sobotní lekci,
                ale v materiálech to není a v testu to samozřejmě taky nebude. Do budoucna
                se vám to ale může hodit :-)
                """
                vitezni_velitele = vitezni_velitele + radek_seznam[19].split(", ")
        # Opačný případ -> útočník měl větší armádu než obránce
        else:
            # Jestliže útočník prohrál
            if radek_seznam[13] == "loss":
                # Opět přidávám více velitelů najednou - viz poznámka výše
                vitezni_velitele = vitezni_velitele + radek_seznam[19].split(", ")
    radek_slovnik = {
        "name": radek_seznam[0],
        "year": int(radek_seznam[1]),
        "attackers": attackers,
        "defenders": defenders,
        "winners": winners,
    }
    data.append(radek_slovnik)
print(vitezni_velitele)
with open("battles.json", mode="w", encoding="utf-8") as soubor:
    json.dump(data, soubor, indent=4)
