# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:10:51 2022

@author: Benja
"""

import numpy 

maxs = 0
promoomal = 0
prom = 0
maxo = 0
sucursal = None
z = 0
suma = 0


x = int(input("Ingrese el número de sucursales y años: "))
y = x
venta = [] #empty


for i in range(y):
    for j in range(x):
        venta.append(float(input(print("Ingrese ventas de sucursal", j , "en el año", i, ": "))))

ventaenarray = numpy.array(venta).reshape((y, x))

for j in range(z):
    suma = 0
    for i in range(y):
        suma = ventaenarray[i][j]
    if(suma > maxo):
        maxo = suma
        sucursal == j
    else:
        pass
    
print(ventaenarray)
print("##########################")
print("Sucursal que más vendió", sucursal)
            
for i in range(y):
    suma = 0
    for j in range(x):
        suma = ventaenarray[i][j]
        prom = suma/x
    print("Promedio de ventas del año", i, "es", prom)
    if(maxs < prom):
       maxs = prom
       promoomal = i
       
print("Año con mayor promedio ", promoomal)
       

            

        
