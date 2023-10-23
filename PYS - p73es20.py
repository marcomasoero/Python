#List Comprehension

def main():
    lim = 11
    tavola = [[k * i for i in range(1, lim)] for k in range (1, lim)]

    for n, tabellina in enumerate(tavola):
        #tabellina è una lista
        #tavola è una lista di liste
        #enumarate restituisce indice e elemento
        print(f"Tabellina del {n + 1}: {tabellina}")

    file = open("tabellina.txt", "w")
    for tabellina in tavola:
        file.write(f"{tabellina}")
    file.close

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()