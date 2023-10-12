import turtle #import the funcion of turtle

#k define the number of side of the different polygons to draw
def draw(t, k, side):
    #this calculate the angle of the polygon's side
    angle = 360 / k
    t.begin_fill()
    #this create the polygon and fill it with the color
    for i in range(0, k):
        t.forward(side)
        t.left(angle)
    t.end_fill()

def position(t, k, side, x, y):
    #all this move the turtle in different positions during the process
    t.penup()
    if(k % 3 == 0):
        x = -100 
        y = y + side * 4
    else:
        x = x + side * 4
    t.goto(x, y)
    t.pendown()
    return x,y

def main():
    #this is the initial position x, y
    x = 0
    y = -100
    #this is the standard dimension of the sides
    dimension = 30
    #this open the window
    window = turtle.Screen()
    #this create the turtle and assing the shape
    alice = turtle.Turtle()
    alice.shape("turtle")
    #this define the color
    alice.color("red")
    alice.speed("slow")

    #this function is repeated 12 - 3 times (= 9 times)
    for k in range(3, 12):
        #change the position of alice during the process
        x, y = position(alice, k, dimension, x, y)
        #draw the polygons always adding a side to the polygon (3, 4, 5, 6,  7, 8, 9, 10, 11, 12)
        draw(alice, k, dimension)
    #alowd the window to stay open during the proces
    window.mainloop() #gestione finestra

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()