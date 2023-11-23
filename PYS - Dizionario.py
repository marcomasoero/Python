#List Comprehension Dizionari
#Dizionario --> Collezione di coppie chiave: valore
#           --> Non ha indici, ma si indicizza per chiave
#           --> Si delimita con le graffe
#Chiave     --> Deve essere univoca
#           --> Deve essere dello stesso tipo
import math

def main():
    dizionaro = {"Nome": "Mario", "Cognome": "Rossi"}
    #Accesso agli elementi
    print(dizionaro["Nome"])
    #Aggiungo elementi
    dizionaro["Data"] = "01/01/1990"
    dizionaro["Eta'"] = 123
    #Stampo dizionario
    print(dizionaro)
    #Ciclo for su dizionario
    for chiave in dizionaro:
        print(f"Chave: {chiave} - valore: {dizionaro[chiave]}")

    rubrica = {3493158617: "Mario Rossi", 9845632587: "Aldo Verdi"}

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()