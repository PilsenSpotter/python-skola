# Jednoducha kalkulacka (kalkulacka.py)

Tahle kalkulacka je co nejjednodussi. Ma ukazat zaklady:
- nacteni vstupu pres `input()`
- prevod textu na cislo pres `float()`
- vyber operace pres `if/elif`
- vypsani vysledku pres `print()`

## Jak spustit

```bash
python kalkulacka.py
```

## Co program dela krok za krokem

1) Zobrazi kratky uvod a seznam operaci.
2) Zepta se na prvni cislo.
3) Zepta se na druhe cislo.
4) Zepta se na operaci: `+`, `-`, `*`, `/`.
5) Spocita vysledek a vypise ho.

## Poznamky

- Vstup je text, proto se prevadi na cislo pomoci `float()`.
- Kdyz delis nulou, program to neudela a napise hlasku.
- Pokud napises jinou operaci, program napise "Neznamou operaci."

## Priklad pouziti

```
Jednoducha kalkulacka
Dostupne operace: +  -  *  /
Zadej prvni cislo: 12
Zadej druhe cislo: 3
Zadej operaci (+, -, *, /): /
Vysledek je: 4.0
```
