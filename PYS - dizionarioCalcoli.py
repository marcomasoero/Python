import math

def mediaAritmetica(n1, n2):
    return (n1 + n2) / 2

def mediaGeometrica(n1, n2):
    return math.sqrt(n1 * n2)

def main():
    numero1 = int(input("Inserisci il primo numero: "))
    numero2 = int(input("Inserisci il secondo numero: "))

    dizionario = {"mediaAritmetica": mediaAritmetica(numero1, numero2),
                  "mediaGeometrica": mediaGeometrica(numero1,  numero2)}
    print(dizionario)

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()