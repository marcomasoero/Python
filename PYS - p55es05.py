import turtle #import the funcion of turtle
#definizione della funzione main
#non abbiamo bisogno delle graffe perchè le funzioni sono tutte definite da indentazione

def main(): 
    s = "Ciao"
    print(f"tutta la stringa esclusi primo ed ultimo carattere: {s[1:-1]}")

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()