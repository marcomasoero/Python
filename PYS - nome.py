def   main():
    nome = input("Inserisci il tuo nome: ")
    nomeAst = nome[0] + '*' * (len(nome) - 1)
    print(nomeAst)

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()