## Poznámky k lekci

* Funkce round() v dokumentaci Pythonu https://docs.python.org/3/library/functions.html#round
* Přehled všech funkcí a modulů: https://docs.python.org/3/library/index.html
* Modul statistics: https://docs.python.org/3/library/statistics.html

Použití modulu statistics

```py
import statistics
Výpočet průměrné hodnoty
statistics.mean([3, 7, 15])
```

Výpočet mediánu (pokud seřadíme data podle velikosti, medián je číslo přesně uprostřed)

```py
statistics.median([3, 7, 15]
```

Spojení dvou seznamů pomocí operátoru + :

```py
[1, 2] + [3, 4]
```

Výsledek je `[1, 2, 3, 4]`

## Doporučené úložky na doma

Zadání úložek jsou [zde](https://kodim.cz/czechitas/python-data/zaklady-programovani/hodnoty-promenne-funkce/#doporucene-ulozky-na-doma).

### 3 - Úroky

```py
1000000 * (1 + 0.024) ** 10
```

### 4 - Délka filmu

```py
223 // 60
223 % 60
```

### 5 - Průměrné teploty
Vytvoření proměnné `radky`

```py
radky = [[2001, 7.8], [2002, 8.7], [2003, 8.2], [2004, 7.8], [2005, 7.7], [2006, 8.2], [2007, 9.1], [2008, 8.9], [2009, 8.4], [2010, 7.2]]
```

Vytvoření proměnné `sloupce`

```py
sloupce = [[2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], [7.8, 8.7, 8.2, 7.8, 7.7, 8.2, 9.1, 8.9, 8.4, 7.2]]
```

#### 5.1

```py
radky[2][1]
```

#### 5.2

```py
radky[4][0]
```

#### 5.3

```py
radky[-1]
```

#### 5.4

```py
radky[2:]
```

#### 5.5

```py
radky[:2]
```

#### 5.6

```py
radky[4:8]
```

#### 5.7

```py
seznam_teplot = sloupce[1]
seznam_teplot.sort()
seznam_teplot
```

### 6 - Průměr
První řádek je pouze příklad

```py
seznam = [1, 2, 3, 4]
sum(seznam) / len(seznam)
```

### 7

```py
30 ** 0.5
```

### 8

```py
s = [1, 2, 3, 4]
max(s) - min(s)
```

### 9

```py
s = [5, 9, 1, 0, 7, 3]
s.sort()
minimum = s[0]
maximum = s[-1]
```
### 10

```py
len(s) // 2
```

### 11

```py
(len(s) - 1) // 2
```
