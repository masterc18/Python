"""Una empresa requiere de un programa donde en una lista inicial del registro
se averigue si existe el nombre de un empleado y si no que se agregue"""

import os
os.system("cls")
os.system("color 02")

employees = ['Jose', 'Lucia', 'Armando']

# print(employees)

search = input("Write name you are looking: ")


while True:
    if (search in employees):
        print("The name is in the register")
        print(search)
        break
    else:
        print("No, the name is not in the register\n")
        print("Do you want to add a new one")
        answer = input("Write yes or no\n")
        if (answer.lower() == "yes"):
            new_Employee = input("Write the name again to confirm: ")
            employees.append(new_Employee)
            print("It's been saved")
            print(employees)
            break
        elif (answer.lower() == "no"):
            print("Command canceled")
            break
        else:
            print("Sorry you have to decide yes or no")

# print(employees)
