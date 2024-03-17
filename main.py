import os

def pulisci():
    os.system('clear')

def carica():
    n = int(input("Quanti numeri vuoi inserire? "))
    numeri = []
    for i in range(n):
        numero = float(input(f"Inserire numero {i+1}: "))
        numeri.append(numero)
    return numeri

def addizione(numeri):
    risultato = 0 
    for numero in numeri:
        risultato+=numero
    print(f"\nL'addizione tra i numeri che hai inserito è: {risultato}")

def sottrazione(numeri):
    risultato = numeri[0]  
    for numero in numeri[1:]:
        risultato -= numero
    print(f"\nLa sottrazione tra i numeri che hai inserito è: {risultato}")

def moltiplicazione(numeri):
    risultato = 1 
    for numero in numeri:
        risultato *= numero
    print(f"\nLa moltiplicazione tra i numeri che hai inserito è: {risultato}")

def divisione(numeri):
    risultato = numeri[0]
    for numero in numeri[1:]:
        risultato /= numero
    print(f"\nLa divisione tra i numeri che hai inserito è: {risultato}")

def menu():
    pulisci()
    numeri = carica()
    scelta = 0

    while scelta != 5:
        print("\nCALCOLATRICE")
        print("1) Addizione")
        print("2) Sottrazione")
        print("3) Moltiplicazione")
        print("4) Divisione")
        print("5) Esci")

        scelta = int(input("Scegli un'operazione (1-5): "))

        match scelta:
            case 1:
                pulisci()
                addizione(numeri)
            case 2:
                pulisci()
                sottrazione(numeri)
            case 3:
                pulisci()
                moltiplicazione(numeri)
            case 4:
                pulisci()
                divisione(numeri)
            case _: 
                print("La scelta immessa non e' disponibile.")


def main():
    menu()

if __name__ == "__main__":
    main()