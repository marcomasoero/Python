#definizione della funzione main
#non abbiamo bisogno delle graffe perchè le funzioni sono tutte definite da indentazione

def sommaQuadrati(n1, n2):
    return (n1 ** 2) + (n2 ** 2)

def quadratoSomma(n1, n2):
    return (n1 + n2) * (n1 + n2)

def differenzaQuadrati(n1, n2):
    return (n1 ** 2) - (n2 ** 2)

def quadratoDifferenza(n1, n2):
    return (n1 - n2) * (n1 - n2)

def main(): 
    lista = []
    numero1 = int(input("Inserisci il primo numero: "))
    numero2 = int(input("Inserisci il secondo numero: "))

    lista.append(sommaQuadrati(numero1, numero2))
    lista.append(quadratoSomma(numero1, numero2))
    lista.append(differenzaQuadrati(numero1, numero2))
    lista.append(quadratoDifferenza(numero1, numero2))

    print(lista)

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()