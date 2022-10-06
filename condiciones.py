def xd():
    while True:
        try:
            Kilos = float(input("Escribe tu cantidad de kilos "))
            break
        except:
            print("That's not a valid option!")
    return Kilos

Kilos = xd()

if Kilos == 0:
        Costo = 0
elif Kilos > 0 and Kilos < 3:
    Costo = Kilos*2.4
elif Kilos >= 3 and Kilos < 6:
    Costo = Kilos*2.3
elif Kilos >= 6 and Kilos >= 10:
    Costo = Kilos*2.1
elif Kilos > 10:
    Costo = Kilos*1.85
else:
    print("Cant have negative kilos mate")
    Costo = 0

print("Tu costo total seria de ", Costo,"$")
