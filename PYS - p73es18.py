#List Comprehension
import math

def main():
    quadrati = [i**2 for i in range(0, int(math.sqrt(200)) + 1) if (i % 2 != 0)]
    print(quadrati)

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()