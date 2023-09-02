
# para borrar consola
import os
os.system("cls")


def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def dividir(num1, num2):
    return num1 / num2


def calculator():

    num1 = float(input("Dime un numero\n"))
    num2 = float(input("Dime otro numero\n"))

    # while True:
    #     print("Select a option")
    #     print("1.Addition")
    #     print("2.Rest")
    #     print("3.Multiplic")
    #     print("4.Dividir")

    #     op = int(input("Write a option\n"))

    #     if op == "1":
    #         print(f"the addition between {num1} and {num2} is {suma(num1,num2)}")
    #     elif op == "2":
    #         print(f"The rest between {num1} and {num2} is {resta(num1,num2)}")
    #     elif op == "3":
    #         print(f"The multiplication between {num1} and {num2} is {mult(num1,num2)}")
    #     elif op == "4":
    #         print(f"The division between {num1} and {num2} is {dividir}")
    #     else:
    #         print("Invalid opcion")
            
    # print(op)

    print("La suma es ", suma(num1,num2))
    print("La resta es ",resta(num1,num2))
    print("la multiplicacion es ",mult(num1,num2))
    print("La division es ",dividir(num1,num2))


calculator()
