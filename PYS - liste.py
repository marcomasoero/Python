#definizione della funzione main
#non abbiamo bisogno delle graffe perchè le funzioni sono tutte definite da indentazione

def print_list(l):
    print("La lista è: ", end = " ")
    for elemento in l:
        print(elemento, end = " ")
    print("\n")

def main(): 
    #Le Liste
    #l = [1, 2, 3, 4, "c", 3.14, "python"]
    #r = [10, 11, 12]
    #print_list(l + r)
    #print_list(3 * r)

    #vogliamo permettere all'utente di caricare
    #una lista
    lista = []
    num = 1
    while num > 0:
        num = int(input("Scrivi un numero: (-1 per uscire): "))
        if num > 0:
            lista.append(num)
    print_list(lista)

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()