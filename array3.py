import numpy as np


#array_size = int(input("Escribe el numero de datos de tu array "))
#multlyping_number = int(input("Escribe tu numero multplicador "))

def Survey():
    while True:
        try:
            array_size = int(input("Escribe el numero de datos de tu array "))
            break
        except:
            print("That's not a valid option!")
    return array_size

def Survey2():
    while True:
        try:
            multlyping_number = int(input("Escribe tu numero multplicador "))
            break
        except:
            print("That's not a valid option!")
    return multlyping_number

loco = Survey()
gato = Survey2() 

y = np.arange(loco)
print(y)
y = gato*y
print(y)