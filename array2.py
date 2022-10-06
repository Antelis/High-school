import numpy as np

def Survey():
    while True:
        try:
            num_nombres = int(input("Escribe tu cantidad de  nombres aqui "))
            break
        except:
            print("That's not a valid option!")
    return num_nombres

gato = Survey()
#nombres = np.zeros(num_nombres)
x = np.array([])
y = np.array([])
for xi in range(0, num_nombres, 1):
    #print(xi)
    nombre_actual = input("Escribe el nombre ")
    x = np.append(x, nombre_actual)
    y = np.append(y, len(nombre_actual))
    print(y, x)