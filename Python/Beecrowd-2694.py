from sys import *

def main():
    n = int(stdin.readline())
    for j in range (n):
        cadena = stdin.readline()
        numeros = "1234567890"
        cont = 0
        numero = ""
        for i in cadena:
            if i in numeros:
                numero += i
            else:
                if numero != "":
                    cont += int(numero)
                numero = ""
        if numero != "":
            cont += int(numero)      
        print(cont)

main()