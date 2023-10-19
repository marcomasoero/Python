import turtle #import the funcion of turtle
#definizione della funzione main
#non abbiamo bisogno delle graffe perchè le funzioni sono tutte definite da indentazione

def disegna(l, t):
    for elemento in l:
        if elemento == 'F':
            t.forward(100)
        if elemento == 'R':
            t.right(90)
        if elemento == 'L':
            t.left(90)

def main(): 
    lista = []
    mov = 'F'
    while mov != 'E':
        mov = input("Scrivi un movimento (F avanti, R rotazione destra, L rotazione sinistra, E uscire): ")
        if mov != 'E':
            lista.append(mov)

    x = 0
    y = -100
    dimension = 30
    window = turtle.Screen()
    alice = turtle.Turtle()
    alice.shape("turtle")
    alice.color("red")
    alice.speed("slow")

    disegna(lista, alice)
    window.mainloop() #gestione finestra

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()