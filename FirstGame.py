# This is a simple game where you will try to guess the number and if you guess correctly you win, if not you try again
# This game can be improve soon

import random
# cont = 3
# answer = int(input('Dime un numero\n'))
# Numbers = random. randint(0, 10)

# while answer == Numbers:
#     #print('La respuesta es: ', Numbers)
#     if (answer == Numbers):
#         print('Congratulations you are the best')
#         if (cont == 0):
#             print("No tienes mas vidas")
#         elif(cont <= 3):
#             print("Ganaste con ", cont)
# else:
#     print('Sorry, try again. You have ', cont-1, "lifes")

num = random.randint(0, 10)
guess = False
oportunities = 3

while (guess == False) and (oportunities > 0):
    print("Write a number")
    x = int(input())
    if (x == num):
        guess = True
        print("Adivinaste")
        oportunities = 0
    else:
        oportunities -= 1
        print(f"Sigue intentando te quedan {oportunities}")
