import os
import random
import sys

def pulisci():
    os.system("clear")

def mostra_parola(parola, lettere_indovinate):
    return ''.join([lettera if lettera in lettere_indovinate else '_' for lettera in parola])

def menu():
    pulisci()
    print("\n BENVENUTO/A NEL GIOCO DELL'IMPICCATO\n")
    print(" 1) Gioca")
    print(" 2) Esci\n")
    scelta=int(input("\n Scelta: "))
    if scelta==1:
        gioco()
    else:
        sys.exit()

def gioco():
    parole=['computer', 'python', 'developer','tastiera','mouse','monitor']
    parola=random.choice(parole)
    lettere_indovinate = set()
    tentativi_errati = 0
    max_tentativi = 6
    
    pulisci()
    print("\n GIOCO DELL'IMPICCATO\n")

    while tentativi_errati < max_tentativi:
        pulisci()
        print("\n GIOCO DELL'IMPICCATO\n")
        print(f" Parola da indovinare: {mostra_parola(parola, lettere_indovinate)}")
        print(f" Tentativi errati: {tentativi_errati}/{max_tentativi}")
        
        lettera = input(" Inserisci una lettera: ").lower()
        
        if lettera in lettere_indovinate:
            pulisci()
            print("\n GIOCO DELL'IMPICCATO\n")
            print(" Hai già indovinato questa lettera. Prova un'altra lettera.\n")
            continue
        
        if lettera in parola:
            lettere_indovinate.add(lettera)
            if set(parola) == lettere_indovinate:
                print(f"\n Hai vinto! La parola era '{parola}'.\n")
                break
        else:
            tentativi_errati += 1
            pulisci()
            print("\n GIOCO DELL'IMPICCATO\n")
            print(f" Lettera errata. Hai ancora {max_tentativi - tentativi_errati} tentativi.\n")
    
    if tentativi_errati == max_tentativi:
        print(f" Hai perso! La parola era '{parola}'.\n")

if __name__ == '__main__':
    menu()
