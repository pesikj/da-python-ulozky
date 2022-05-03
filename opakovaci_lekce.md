# Soubor JSON

Příklad záznamu jednoho člověka

```
    {
        "first_name": "Otakar",
        "last_name": "Kučera",
        "birth_number": "155625/8341",
        "friends": "Hynek, Erik, Tomáš",
        "permanent_address": "Žherská 941\n383 98 Mikulášovice",
        "phone_number": "604 965 934",
        "mail_address": "Bajkalská 5\n411 22 Vimperk"
    }
```

Vytvoř soubor CSV, který obsahuje následující data:

- jméno,
- příjmení,
- rok narození,
- počet přátel,
- město, kde je možné jej zastihnout (korespondenční adresa, pokud je zadána, jinak trvalé bydliště).

Dále vytvoř seznam lidí, které můžeme zastihnout ve Středočeském kraji (PSČ začíná číslem 2)

# Soubor TSV

Načti soubor `battles.tsv` a vytvoř z něj soubor ve formátu JSON, který bude obsahovat informace o názvu bitvy, roce, kdy se odehrála, útečnících, obráncích a vítězi.

```
    {
        "name": "Battle of the Golden Tooth",
        "year": "298",
        "attackers": [
            "Lannister"
        ],
        "defenders": [
            "Tully"
        ],
        "winners": [
            "Lannister"
        ]
    }
```

Dále vytvoř:

- statistiku, kolikrát který rod vyhrál v bitvě,
- pokud je zadaná síla obou armád, ověř, zda zvítězila silnější armáda,
- vytvoř seznam velitelů, kteří vyhráli v boji proti přesile (každý velitel bude v seznamu tolikrát, kolikrát vyhrál).

