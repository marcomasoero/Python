#definizione della funzione main
#non abbiamo bisogno delle graffe perchè le funzioni sono tutte definite da indentazione
def main(): 
    a = int(input("Inserisci un numero: "))
    contatore = 0

    if a % 2 == 0:
        print(f"Il numero {a} è divisibile per 2.")
        contatore = contatore + 1
    if a % 3 == 0:
        print(f"Il numero {a} è divisibile per 3.")
        contatore = contatore + 1
    if a % 5 == 0:
        print(f"Il numero {a} è divisibile per 5.")
        contatore = contatore + 1
    if contatore == 0:
        print(f"Il numero non {a} è divisibile ne per 2, ne per 3, ne per 5.")
    
#formula per l'esecuzione del main
if __name__ == "__main__":
    main()