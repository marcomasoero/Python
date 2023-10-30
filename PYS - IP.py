#List Comprehension
import math

def completa8bit(strbin):
    b = strbin[2:]
    l = len(b)
    return "0"*(8 - l) + b

def main():
    ip = "90.90.120.1"
    #Divide la stringa sui punti
    groups = ip.split(".")
    print(groups)
    #Converte i singoli valori in interi
    groups = [int(group) for group in groups]
    print(groups)
    #Verrà stampato il valore in binario preceduto da "0b",  delineazione del binario
    groups = [bin(group) for group in groups]
    print(groups)
    #Completa gli otteti binari
    print(completa8bit(groups[1]))
    groupsStrbin = [completa8bit(strbin) for strbin in groups]
    print(groupsStrbin)
    #Ricrea la stringa in notazione binaria puntata
    print(".".join(groupsStrbin))

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()