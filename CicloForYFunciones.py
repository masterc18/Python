# * Cree un programa que muestre los numeros del 1 al 10 usando un ciclo y una funcion

def Uso_Ciclo():
    for i in range (1, 101):
        if (i%2==0):
            print("Los multiplos de 2 son",i)
        elif(i%9==0):
            print("Los multiplos de 9 son:",i)
        
        
        
Uso_Ciclo()