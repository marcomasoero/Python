#List Comprehension
import math

def main():
    stringa = "ciao"
    vocali = "aeiouAEIOU"

    mod = [k for k in stringa if (k not in vocali)]
    print("".join(mod))

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()