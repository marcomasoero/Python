#definizione della funzione main
#non abbiamo bisogno delle graffe perchè le funzioni sono tutte definite da indentazione
def main():
    nome = input("Come ti chiami? ")
    #int() serve per cambiare il tipo della variabile successivamente alla creazione
    anni = int(input("Quanti anni hai? "))
    annoCorrente = int(input("In quale anno siamo? "))

    print(f"Il tuo nome è {nome} e hai {anni} anni.")
    print(f"Sei nato nel {annoCorrente - anni}")

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()