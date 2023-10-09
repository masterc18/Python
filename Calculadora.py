
# para borrar consola
import os
from math import sqrt
os.system("cls")


def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def dividir(num1, num2):
    return num1 / num2


def raiz(num1):
    return sqrt(num1)


def calculator():

    op = 0
    while op != 6:
        msn = """1.Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Raiz
6. Salir"""
        print(msn)
        if (op == 1):
            num1 = eval(input("Dime un numero: "))
            num2 = eval(input("Dime otro numero: "))
            print(f"El rsultado es: {suma}")
        elif op == 2:
            num1 = eval(input("Dime un numero: "))
            num2 = eval(input("Dime otro numero: "))
            print(f"El resultado es: {resta}")
        elif op == 3:
            num1 = eval(input("Dime un numero: "))
            num2 = eval(input("Dime otro numero: "))
            print(f"El resultado es: {mult}")
        elif op == 4:
            num1 = eval(input("Dime un numero: "))
            num2 = eval(input("Dime otro numero: "))
            print(f"El resultado es: {dividir}")
        elif op == 5:
            num1 = eval(input("Dime un numero: "))
            print(f"El resultado es: {raiz}")
        elif op == 6:
            print("Saliendo.......")
        else:
            print("Opcion invalida")
        os.system("pause")


def main():
    calculator()

    
    
main()
