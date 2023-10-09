
import os
"""Una empresa requiere de un programa donde se guardaran los emails
usuarios y password de sus empleados"""

password = []  # Se declara el arreglo vacio donde se guardarn las password
user = []  # Se declara el arreglo vacio donde se guardaran los usuarios
email = []


os. system("cls")

while True:
    print("\n")
    new_user = input("Write your user: ")
    user.append(new_user)  # se agregan los usuarios al arreglo de los usuarios
    print("\n")
    new_email = input("Write the email: ")
    if "@" in user:
        email.append(new_email)
    else:
        print("Use @ to make the email")
        break
    print("\n")
    new_password = input("Write your password: ")
    # se agregan los usuarios al arreglo de las password
    password.append(new_password)

    print("\n")

    print(f"Usuarios: {user}")
    print(f"Emails: {email}")
    print(f"Passwords: {password}")
