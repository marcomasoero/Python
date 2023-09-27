#definizione della funzione main
#non abbiamo bisogno delle graffe perchè le funzioni sono tutte definite da indentazione
def main(): 
    a = int(input("Che operazione si desidera effettuare? 0 = somma | 1 = sottrazione | 2 = moltiplicazione | 3 = divisione: "))
    b = int(input("Inserisci il primo numero: "))
    c = int(input("Inserisci il secondo numero: "))

    if a == 0:
        print(f"Il risultato è {b + c}.")
    if a == 1:
        if b >= c:
            print(f"Il risultato è {b - c}.")
        else:
            print("L'operazione non si può fare.")
    if a == 2:
        print(f"Il risultato è {b * c}.")
    if a == 3:
        if b % c == 0:
            print(f"Il risultato è {b / c}.")
        else:
            print("L'operazione non si può fare.")
    
#formula per l'esecuzione del main
if __name__ == "__main__":
    main()