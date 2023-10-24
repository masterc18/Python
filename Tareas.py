# Hacer una lista de tareas donde las tareas completadas se han eliminadas
from os import system
tasks = dict()


def addTask():
    task = input("Write a task: ")
    hour = input("Set a time: ")
    tasks[task] = hour


def isTask(task):
    return task in tasks


def showTask():
    task = input("Write the task that you are looking for: ")
    if isTask(task):
        print(f"Tarea : {task}")
        print(f"Hora: {tasks[task]}")
    else:
        print("Task didn't find")


def showTasks():
    for task, hour in tasks.items():
        print(f"Task: {task:<10}, Hour: {hour:>3}")


def deleteTask():
    task = input("Write the task that you are delete: ")
    if isTask(task):
        del tasks[task]
    else:
        print("Task didn't find")


def menu():
    print("""1. Agregar tarea
2. Mostrar tarea
3. Mostrar tareas
4. Eliminar tarea
5. Salir""")
    op = int(input("Digite una opcion: "))
    return op


def main():
    while True:
        system("cls")
        op = menu()
        if op == 1:
            addTask()
            system("pause")
        elif op == 2:
            showTask()
            system("pause")
        elif op == 3:
            showTasks()
            system("pause")
        elif op == 4:
            deleteTask()
            system("pause")
        elif op == 5:
            print("Saliendo......")
            system("pause")
        else:
            print("opcion invalida")
            system("pause")


main()
