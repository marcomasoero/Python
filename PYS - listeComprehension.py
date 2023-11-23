#List Comprehension
#Lista con i primi 5 quadrati perfetti
import random

def main():
    #i**2 --> Potenza
    stringhe = ["computer", "cellulare", "tablet"]

    quadrati = [i**2 for i in range(1, 6)]
    interi = [i for i in range(1, 11)]
    stringheC = [parola for parola in stringhe if parola[0] == "c"]

    print(quadrati)
    print(interi)
    print(stringheC)

    voti = [random.randint(2, 10) for _ in range(10)]
    print(voti)
    votiUnder6 = [voto for voto in voti if voto < 6]
    print(votiUnder6)

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()