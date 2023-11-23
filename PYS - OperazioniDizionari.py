#chiedi all'utente che operazione fare, in aggiunta a due valori

def somma(a, b):
    return a + b

def prodotto(a, b):
    return a * b

def sottrazione(a, b):
    return a - b

def divisione(a, b):
    return a / b

def main():
    dizionario = {"+": somma, "*": prodotto, "-": sottrazione, "/": divisione}
    operazione = input("Scrivi + per somma, * per prodotto, - per sottrazione, / per divisione: ")
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    #è di tipo funzione, posso quindi passare dei parametri
    #in base alla chiave operazione usa o somma o prodotto
    print(dizionario[operazione](a, b))

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()