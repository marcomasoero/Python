import turtle #import the funcion of turtle
#definizione della funzione main
#non abbiamo bisogno delle graffe perchè le funzioni sono tutte definite da indentazione

def main(): 
    a, b, c, d = 10, "Ciao", 12.5, True

    print(f"Il tipo di a è {type(a)}")
    print(f"Il tipo di b è {type(b)}")
    print(f"Il tipo di c è {type(c)}")
    print(f"Il tipo di d è {type(d)}")

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()