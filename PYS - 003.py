#definizione della funzione main
#non abbiamo bisogno delle graffe perchè le funzioni sono tutte definite da indentazione
def main(): 
    #cicla in un range (da zero a quattro, quattro escluso)
    for i in range(0,8):
        print(f"i vale {i}")

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()