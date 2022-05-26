# Maturita

```
Jméno,Český jazyk,Anglický jazyk,Matematika,Biologie,Chemie,Informatika
Guido van Rossum,1,1,1,1,1,
James Gosling,3,1,3,2,5,
Mads Torgersen,2,2,1,3,,2
```

Uvažuj program, který bude pracovat s výsledky z maturitní zkoušky. Data jsou v souboru [maturita.csv](maturita.csv). Každý maturoval povinně z českého jazyka, anglického jazyka, matematiky a biologie a dále si mohl vybrat mezi informatikou a chemií.

Student může mít jeden z následujících výsledků:

- "Prospěl s vyznamenáním", pokud je průměr jeho známek maximálně 1.5 a nemá žádnou trojku.
- "Neprospěl", pokud má alespoň jednu pětku.
- "Prospěl", pokud nemá vyznamenání a současně nedostal žádnou pětku.

Tvůj program by měl zapsat do souboru ve formátu JSON jména studentů a jejich výsledky.

```
[
    {
        "Jméno": "Guido van Rossum",
        "Výsledek": "Prospěl s vyznamenáním"
    },
    {
        "Jméno": "James Gosling",
        "Výsledek": "Neprospěl"
    },
    {
        "Jméno": "Mads Torgersen",
        "Výsledek": "Prospěl"
    }
]
```

