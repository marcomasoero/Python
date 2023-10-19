import turtle #import the funcion of turtle
#definizione della funzione main
#non abbiamo bisogno delle graffe perchè le funzioni sono tutte definite da indentazione

def main(): 
    lista = []
    voto = 0
    k = 0
    while k < 7:
        voto = input("Inserisci un voto: ")
        lista.append(voto)
        k = k + 1
    print(f"Tutta la lista esclusi primo ed ultimo voto: {lista[1:-1]}")
    lista[4] = 10
    print(lista[4])
    print(f"I primi 3 voti sono: {lista[0:3]}")

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()