# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 18:54:20 2022

@author: Benja
"""
V = 100*[0]
i = 0
print("Ingrese el tamaño del vector: ")
n = int(input())
opc = -1
while opc != 0:
    print("Ingresa 1 para añadir un elemento")
    print("Ingresa 2 para eliminar un elemto")
    print("Ingresa 3 para listar los elementos")
    print("Ingresa 4 para contar las apariciones de un número")
    print("Ingresa 5 para calcular media y máximo")
    print("Ingresa 0 para terminar")
    
    opc = int(input("Ingrese la opción deseada: "))
    
    if opc == 1:
        if(i<n):
            V[i] = int(input("Ingrese el dato: "))
            i = i + 1
    elif opc == 2:
        print("Ingrese el número a eliminar: ")
        num = int(input())
        
        if num > 0:
            a = 0
            for j in range(i):
                if V[i] == num:
                    a = j
                    break
            if a >= 0 and a <= i:
                for j in range(a,i+1):
                    V[j] = V[j+1]
                V[i] = 0
                i = i +1
    elif opc == 3:
        for i in range(n):
            print(V[i])
    
    elif opc == 4:
        moda=0
        numbero = int(input("Cual numero quisieras contar el numero de repeticiones?: "))
        for i in range(n):
            if (V[i] == numbero):
                moda += 1
        print("Tu numero se repitio", moda)
    
    elif opc == 5:
        x = 0
        for i in range(n):
            x = V[i]
            if(x < V[i]):
                x = V[i]
        media = x/n
        print("tu numero maximo es" , x, "y la media es" , media)
    else:
        break