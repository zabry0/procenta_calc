
def vypocet_procent(a, b):
    try:
      
        procenta = (a / b) * 100
        return procenta
    except ZeroDivisionError:
        return "Dělení nulou není povoleno."


def main():
 
    try:
        cislo1 = float(input("Zadejte první číslo: "))
        cislo2 = float(input("Zadejte druhé číslo: "))
    except ValueError:
        print("Prosím, zadejte platná čísla.")
        return

    
    vysledek = vypocet_procent(cislo1, cislo2)

    
    if isinstance(vysledek, str):
        print(vysledek)
    else:
        print(f"{cislo1} je {vysledek:.2f}% z {cislo2}.")

if __name__ == "__main__":
    main()
