def main():
    stringa = ""
    na = 0
    nt = 0
    ng = 0
    nc = 0

    file = open("covid-19_gen1.txt", "r")
    for riga in file:
        riga = riga[:-1]
        stringa = stringa + riga
    file.close()

    print(stringa)

    for carattere in stringa:
        if (carattere == "A"):
            na += 1
        elif(carattere == "T"):
            nt += 1
        elif(carattere == "G"):
            ng += 1
        elif(carattere == "C"):
            nc += 1

    print(na, nt, ng, nc)
    print(stringa.find("ATGTTTGTTTTT"))

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()