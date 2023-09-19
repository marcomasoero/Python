#definizione della funzione main
#non abbiamo bisogno delle graffe perchè le funzioni sono tutte definite da indentazione
def main(): 
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    if a < b:
        a, b = b, a
    print(f"Il maggiore è {a} e il minore è {b}.")

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()