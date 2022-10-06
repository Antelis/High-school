# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 13:48:03 2022

@author: Benja
"""

def add():
    pass
def edit(edvd):
    pass
def remo(rdvd):
    pass
def find(fdvd):
    pass
def lista(ldvd):
    pass
def prese(pdvd):
    pass
def exp(edvd):
    pass
def finds(fdvd):
    pass
def conne(cdvd):
    pass

print("############################")
print("    Bienvenido al menu      ")
print("   Selecciona una opcion    ")
print("############################")

oui = -1

while oui != 0:
    print("Ingresa 1 para agregar un DVD")
    print("Ingresa 2 para editar un DVD")
    print("Ingresa 3 para eliminar un DVD")
    print("Ingresa 4 para encontrar un DVD")
    print("Ingresa 5 para presenta un DVDr")
    print("Ingresa 6 para exportar un DVD")
    print("Ingresa 0 para salir")
    oui = int(input("Ingresa tu opcion deseada: "))

    if oui == 1:
        print("   Agregar un DVD   ")
        print("############################")
    elif oui == 2:
        print("   Editar un DVD   ")
        print("############################")
    elif oui == 3:
        print("   Eliminar un DVD   ")
        print("############################")
    elif oui == 4:
        print("   Encontrar un DVD   ")
        print("############################")
    elif oui == 5:
        print("   Presentar un DVD   ")
        print("############################")
    elif oui == 6:
        print("   Exportar un DVD   ")
        print("############################")
    elif oui == 0:
        print("        Bye bye   ")
        print("############################")
    else:
        print("Opcion no valida, plz intenta otra vez")
        print("############################")

        

        