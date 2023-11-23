def   main():
    rubrica = {}
    #leggo il file, salvo in righe, chiudo il file
    file = open("rubrica.txt", "r")
    righe = file.readlines()
    file.close()

    for riga in righe:
        #restituisce i campi
        campi = riga.split(", ")
        #sostiuisco il carattere \n con un carattere a scelta
        numeroTelefonico = int(campi[1].replace("\n", ""))
        nome = campi[0]
        #numeroTelefonico lo utilizzo come chiave, che serve per indicizzare
        rubrica[numeroTelefonico] = nome
    print(rubrica)

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()