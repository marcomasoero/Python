def main():
    file = open("covid-19_gen1.txt", "r")
    righe = file.readlines()
    file.close()

    righe.replace(", ", "")
    righe.replace("\n", "")
    lista = righe
    print(lista)

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()