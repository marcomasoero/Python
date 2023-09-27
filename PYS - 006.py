#definizione della funzione main
#non abbiamo bisogno delle graffe perchè le funzioni sono tutte definite da indentazione
def main(): 
    a = int(input("Inserisci un numero: "))
    if a % 3 == 0:
        print(f"Il numero {a} è divisibile per 3.")
    else:
        print(f"Il numero {a} non è divisibile per 3.")
#formula per l'esecuzione del main
if __name__ == "__main__":
    main()