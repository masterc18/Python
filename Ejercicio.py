# * Escribir un programa que muestre los numeros del 1 al 100 
# y que sustituya los multiplos de 3 con fizz, 
# los multiplos de 5 con buzz 
# y los de 15 con fizz buzz

for i in range(1, 101):
    if i % 15 == 0:
        print('fizz buzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 7 == 0:
        print('Woof')
    elif i % 5 == 0:
        print ('buzz')
    else:
        print(i)