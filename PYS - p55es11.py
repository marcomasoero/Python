import turtle #import the funcion of turtle
#definizione della funzione main
#non abbiamo bisogno delle graffe perchè le funzioni sono tutte definite da indentazione

def main(): 
    x = [0, 1, 2, 3, 5, 6, 7, 8]
    x1 = x[0:4]
    x2 = x[4:8]
    #x1[5] = 5
    print(f"Lista x: {x[:]}")
    print(f"Lista x1: {x1[:]}")
    print(f"Lista x2: {x2[:]}")

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()