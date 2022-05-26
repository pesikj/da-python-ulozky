import json
with open("maturita.csv", encoding="utf-8") as soubor:
    data = soubor.readlines()

data = [x.strip().split(",") for x in data]
data = data[1:]
print(data)
vystup = []
for radek in data:
    print(radek)
    radek_vystup = {"Jméno": radek[0]}
    znamky = [int(x) for x in radek[1:] if x != ""]
    nejhorsi_znamka = max(znamky)
    prumer = sum(znamky) / len(znamky)
    if nejhorsi_znamka == 5:
        radek_vystup["Výsledek"] = "Neprospěl"
    elif nejhorsi_znamka <= 2:
        if prumer <= 1.5:
            radek_vystup["Výsledek"] = "Prospěl s vyznamenáním"
        else:
            radek_vystup["Výsledek"] = "Prospěl"
    else:
        radek_vystup["Výsledek"] = "Prospěl"
    vystup.append(radek_vystup)
print(vystup)

with open("maturita_vystup.json", "w", encoding="utf-8") as maturita_vystup:
    json.dump(vystup, maturita_vystup, indent=4, ensure_ascii=False)
