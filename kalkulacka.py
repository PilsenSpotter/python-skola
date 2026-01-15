print("Jednoducha kalkulacka")
print("Dostupne operace: +  -  *  /")

# Nacti dve cisla a operaci od uzivatele
a_text = input("Zadej prvni cislo: ")
op = input("Zadej operaci (+, -, *, /): ")
b_text = input("Zadej druhe cislo: ")

a = float(a_text)
b = float(b_text)

vysledek = None

if op == "+":
    vysledek = a + b
elif op == "-":
    vysledek = a - b
elif op == "*":
    vysledek = a * b
elif op == "/":
    if b == 0:
        print("Nulou delit nejde.")
    else:
        vysledek = a / b
else:
    print("Neznamou operaci.")

if vysledek is not None:
    print("Vysledek je:", vysledek)
