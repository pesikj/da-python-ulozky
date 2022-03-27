## Práce s textem, chroustání seznamů

Zadání úložek jsou [zde](https://kodim.cz/czechitas/python-data/zaklady-programovani/text-chroustani/#doporucene-ulozky-na-doma).

### 9

```py
veky = [35, 12, 44, 11, 18, 21, 28, 18]
zbyva_do_18 = [18 - vek for vek in veky]
starsi_18 = [vek > 18 for vek in veky]
presne_18 = [vek == 18 for vek in veky]
```

### 10

```py
delky = [136, 105, 82]
trvani = [f"{minuty//60}:{minuty%60}" for minuty in delky]
```

### 11

```py
nazvy = [kraj[0] for kraj in kraje]
pocty_obyvatel = [int(kraj[1].replace(" ", "")) for kraj in kraje]
tabulka_dva_seznamy = [nazvy, pocty_obyvatel]
```

### 12
#### 12.1

Můžeme provést pětkrát chroustání seznamů, tj. pro kandidáta 0:

```py
hlasy_kandidata_0 = [radek[0] for radek in hlasy]
```

Provedeme podobné chroustání pro další kandidáty a poté jednotlivé seznamy sečteme.
Alternativně můžeme zanořit dvě chroustání do sebe (výraz "zanořit chroustání" je opravdu hrozný, ale snad je to jasné) a použít funkci `range()`, která je v kurzu až později, ale ze soboty už byste ji měly znát.

```py
hlasy_kandidatu = [[radek[i] for radek in hlasy] for i in range(0,5)]
```

#### 12.2

```py
soucty.index(max(soucty))
```

#### 12.3

Zde řeším otázku, kde bylo nejméně a nejvíce hlasů, volební účast v procentech je až níže, ale řešení by bylo podobné.

```py
pocty_hlasu = [sum(radek) for radek in hlasy]
pocty_hlasu.index(max(pocty_hlasu))
pocty_hlasu.index(min(pocty_hlasu))
```

#### 12.4

```py
vitezove_v_krajich = [radek.index(max(radek)) for radek in hlasy]
```

#### 12.5

```py
procenta_kraj_0 = [round(100 * hodnota / sum(hlasy[0])) for hodnota in hlasy[0]]
```

Stejným způsobem lze dopočítat ostatní kraje.

#### 12.6

Potřebujeme seznam, kde budou dvojice s počtem hlasů a obyvatel. To lze spojit pomocí samostatného chroustání, ale můžete použít funkci zip() , která udělá to samé. Vizuálně si to můžete představit opravdu jako zip - spojujeme dva prvky do jednoho.

```py
pocty_hlasu_a_obyvatel = list(zip(pocty_hlasu, pocty_obyvatel))
ucast_nad_50_procent = [radek[0] > radek[1] * 0.5 for radek in pocty_hlasu_a_obyvatel]
```

### 13

```py
procenta_hlasu_pro_kandidaty = [[round(100 * hodnota / sum(radek)) for hodnota in radek] for radek in hlasy]

```