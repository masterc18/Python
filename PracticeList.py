# import random
# names = ["Carlos", "Alvaro", "Diego", "Jose"]
# numbers = [1, 2, 3, 4, 5]
# # random.shuffle(numbers)#Desordena de manera aleatoria
# # numbers.sort(reverse=True) Invertir el orden de las listas
# names.sort() #Ordena los elementos de la lista
# print(names)
from os import system



# Hacer un programa que
names = list()


def addPeople():
    people = input("Escribe el nombre de la persona: ")
    names.append(people)


def showPeople():
    for person in names:
        print(person)


def OrderPeople():
    return names.sort()


def main():
    while True:
        system("cls")
        print("1. Agregar persona")
        print("2. Mostrar lista")
        print("3. Ordenar Lista")
        print("4. Salir")
        op = int(input("Digite una opcion: "))
        #Switch en python
        match op:
            case 1:
                addPeople()
                system("pause")
            case 2:
                showPeople()
                system("pause")
            case 3:
                OrderPeople()
                system("pause")
            case 4:
                print("Adioooosssss...")
                system("Pause")


main()


# from math import factorial

# def Factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)


# def main():
#     n = eval(input("Introduce un numero entero positivo para calcular el factorial: "))
#     print(f"El factorial de {n} es {Factorial(n)}")


# main()
