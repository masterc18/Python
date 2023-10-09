# 1. Hacer un diccionario donde se registre el nombre y salario de los trbajadores
from os import system
trabajadores = dict()

def addWorkers():
    name = input("Ingrese el nombre del trabajador: ")
    salary = float(input("Ingrese su salario: "))
    
    trabajadores[name] = salary

def isWorker(name):
    return name in trabajadores  

def showWorker():
    name = input("Ingrese el nombre del trabajador a buscar: ")
    if isWorker(name):
        print(f"Se encontro {name}\n Datos:\n Nombre: {name:<10}, Salario: {trabajadores[name]:>3}")
    else:
        print("No se encontro el nombre en el registro")

def showAllWorkers():
    #Siempre para iterar en un diccionario se debe usar el metodo item()
    for name, salary in trabajadores.items():
        print(f"Nombre del trabajador {name:<10}, Salario {salary:>3}")

def deleteWorker():
    name = input("Ingrese el nombre del trabajador que desea elimiar: ")
    if isWorker(name):
        del trabajadores[name]
    else:
        print("Nombre no encontrado")
        
def menu():
    print("""1. Agregar trabajador
2. Mostrar trabajador 
3. Mostrar todos los trabajadores
4. Borrar trabajador 
5. Salir""")
    op = int(input("Digita una opcion: "))
    return op

def main():
    while True:
        op = menu()
        if op == 1:
            addWorkers()
            system("Pause")
        elif op == 2:
            showWorker()
            system("Pause")
        elif op == 3:
            showAllWorkers()
            system("Pause")
        elif op == 4:
            deleteWorker()
            system("Pause")
        elif op == 5:
            print("Adios....")
            system("Pause")
        else:
            print("Opcion invalida")
            
main()