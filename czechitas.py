#!/usr/bin/env python3

"""
Tady je příprava dat načtením zapickleného slovníku. 🥒 Na tento blok prosím
nesahejte, s tím, jak přesně funguje, se seznámíte v dalších lekcích. 🙂
"""

import pickle

with open("grouped.pickle", "rb") as f:
    data = pickle.load(f)

anything = data["wikicard/anythinggoes"]
continent = data["wikicard/continent"]

print("Počet položek v proměnné continent:", len(continent))
print("Počet položek v proměnné anything:", len(anything))
print("Ukázka dat v proměnné continent:", continent)

"""
A tady už je vaše pískoviště, tady si můžete dělat, co vás napadne. 🦄

Základem tohoto cvičení jsou data z otevřeného API Wikipedie. Jedná se o reálná data,
která v Seznamu využíváme ke tvorbě „chytrých“ kartiček: informačních karet obsahujících
strukturovaná data o lidech, přírodě, technice, zkrátka encyklopedických entitách.

Proměnná continent obsahuje data o světadílech. 🌍 Jedná seznam dvojic (tuple), jedna
dvojice pro každý světadíl. První hodnota dvojice udává počet zobrazení stránky
daného světadílu na Wikipedii za posledních 30 dnů. Druhá hodnota je název světadílu.

Proměnná anything obsahuje data o čemkoli, u čeho jsme nenalezli dostatečně zajímavý
infobox (boxík se strukturovanými daty vpravo na stránce Wikipedie). Práce s ní bude
v zásadě stejná jako s proměnnou continent, jen tam je těch dat o hodně víc, a tak jsou
taky o hodně zajímavější. 😊

No a teď konečně, co mě zajímá! Žádanost pro všechna zadání znamená počet zobrazení
dané stránky na Wikipedii, více je pochopitelně lépe.

Zadání je následující:

1) Vypište názvy 3 nejžádanějších světadílů oddělené čárkami (na pořadí nezáleží).

    Příklad výstupu (pouze kvůli formátu, nejedná se o správné řešení):
    Nejžádanější světadíly: Severní Amerika, Střední Amerika, Austrálie (kontinent)

2) Vypište počty zobrazení 3 nejžádanějších světadílů oddělené čárkami.

    Příklad výstupu:
    Nejvyšší počty zobrazení: 8836, 6866, 1921

3) Upravte výstup první úlohy tak, aby za názvem následoval počet zobrazení v závorce:

    Příklad výstupu:
    Nejžádanější světadíly: Severní Amerika (8836 zobr.), Střední Amerika (6866 zobr.), Austrálie (kontinent) (1921 zobr.)

4) BONUS: Místo dat o světadílech pracujte s daty „o čemkoli“. 🙂

5) BONUS: Místo 3 nejžádanějších položek vypište 4 položky z okolí mediánu žádanosti.

6) 🦸‍♀️ SUPERHERO BONUS: Kromě světadílů a nekategorizovaných položek, jaké všechny
   kategorie položek máme v této datové sadě k dispozici? Názvy kategorií ponechte
   v angličtině, ale předveďte ten nejkrásnější výstup, jaký umíte. 💪
"""
