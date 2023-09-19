#definizione della funzione main
#non abbiamo bisogno delle graffe perchè le funzioni sono tutte definite da indentazione
def main(): 
    a = float(input("Inserisci un numero: "))
    #il tipo di a è <class 'int'>
    print(f"Il tipo di a è {type(a)}")
    if a > 5:
        print("a è maggiore di 5")
    #la and si può scrivere il lettere o come simbolo --> & (una sola, non come C)
    elif(a <= 5) and (a >= 0):
        print("a è maggiore 0 uguale a zero e minore o uguale a 5")
    else:
        print("a è minore o uguale a 5")

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()