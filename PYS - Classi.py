#Le Classi

class Quadrato():
    #self è il parente di this. in Java
    #sintassi per la creazione della classe, Metodo Costruttore
    def __init__(self, lato):
        self.lato = lato
    
    def calcolArea(self):
        return self.lato ** 2

def main():
    #creo l'istanza di quadrato
    l = float(input("Inserisci il lato del quadrato del quale si desidera conoscere l'area: "))
    q = Quadrato(l)
    print(f"L'area del quadrato è {q.calcolArea()}")

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()