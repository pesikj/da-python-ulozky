import json
with open("people.json", encoding="utf-8") as soubor:
    text = soubor.read()
lide = json.loads(text)
lide_vystup = []
for clovek in lide:
    jmeno = clovek["first_name"]
    prijmeni = clovek["last_name"]
    rok_narozeni = clovek["birth_number"]
    rok_narozeni_cislo = int(clovek["birth_number"][:2])
    if rok_narozeni_cislo <= 22:
        if len(rok_narozeni) == 10:
            rok_narozeni_cislo = 1900 + rok_narozeni_cislo
        else:
            rok_narozeni_cislo = 2000 + rok_narozeni_cislo
    else:
        rok_narozeni_cislo = 1900 + rok_narozeni_cislo
    #Emilie,Marešová,1920
    pratele = len(clovek["friends"].split(","))
    adresa = clovek["permanent_address"].split("\n")
    mesto = adresa[1][7:]
    # Alternativní řešení pro město
    adresa_druhy_radek = adresa[1].split()
    mesto = " ".join(adresa_druhy_radek[2:])
    # ["U Rajské Zahrady 596", "475 15 Městec Králové"]
    if adresa[1][0] == "2":
        print(jmeno)
    
    radek = f"{jmeno},{prijmeni},{rok_narozeni_cislo},{pratele},{mesto}\n"
    #radek = ",".join([jmeno, prijmeni, str(rok_narozeni), str(pratele), mesto])
    lide_vystup.append(radek)
with open("people.csv", mode="w", encoding="utf-8") as vystup:
    vystup.writelines(lide_vystup)
    

