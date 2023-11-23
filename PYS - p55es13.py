#Le Classi
class Robot:
    def _init_(self, nome, massa, tipologia):
        self.nome = nome
        self.massa = massa
        self.tipologia = tipologia 

    def stampaNome(self):
        print(f"nome robot: {self.nome}")

    def pericoloso(self):
        return (self.tipologia == 'umanoide' and self.massa > 100)

def main():
    r1 = Robot("RoboOne", 100, 'noUmanoide')
    r2 = Robot("RoboTwo", 150, 'umanoide')

    r1.stampaNome()
    print(f"massa: {r1.massa} ")

    if r1.pericoloso()==True:
        print("è pericoloso")

    r2.stampaNome()
    print(f"massa: {r2.massa} ")

    if r2.pericoloso()==True:
        print("è pericoloso")


#formula per l'esecuzione del main
if __name__ == "__main__":
    main()