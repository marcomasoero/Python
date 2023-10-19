import turtle #import the funcion of turtle
#definizione della funzione main
#non abbiamo bisogno delle graffe perchè le funzioni sono tutte definite da indentazione

def main(): 
    prima = 10
    seconda = 20
    
    print(f"Il Primo è {prima} e il Secondo è {seconda}.")
    prima, seconda = seconda, prima
    print(f"Il Primo è {prima} e il Secondo è {seconda}.")

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()