#definizione della funzione main
#non abbiamo bisogno delle graffe perchè le funzioni sono tutte definite da indentazione
def main(): 
    #simil vettore, denominato lista
    lista = [4, 100, 3, 5, "ciao", print]

    #ciclo for C-style
    #cicla per i da 0 a lunghezza di lista
    for i in range(0, len(lista)):
        print(lista[i])

    print("\n")

    #ciclo for PY-style
    #cicla per elemento in lista
    for elemento in lista:
        print(f"Elemento: {elemento}")

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()