import turtle #import the funcion of turtle
#definizione della funzione main
#non abbiamo bisogno delle graffe perchè le funzioni sono tutte definite da indentazione

def main(): 
    s = "Ciao"
    k = 1
    for i in range(k, len(s)):
        print(s[k])
        k = k + 2


#formula per l'esecuzione del main
if __name__ == "__main__":
    main()