#List Comprehension
import math

def main():
    n = int(input("Inserisci il numero massimo della potenza: "))
    esponente = int(math.log2(n))
    quadrati = [2**i for i in range(0, esponente + 1) if 2**i <= n]
    print(quadrati)

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()