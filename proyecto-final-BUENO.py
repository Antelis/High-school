#a
#Andres Benjamin Antelis
#Diego de la Vega
#Ana Cristina Rodriguez

import sqlite3

#function
def is_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def connect():
    conexion = sqlite3.connect("db_DVD.db")
    return conexion

def create():
    conexion = connect()
    try:
        conexion.execute("""create table DVDs (codigo integer primary key autoincrement, Titulo text, A_Lanza integer, Tam_min integer, Director text)""")
        print('Se creo la tabla DVDs')
    except sqlite3.OperationalError:
        print(' ')
    conexion.close()
    
def add():
    titulo = str(input('Ingresa el título de la película: '))
    a_lanz = int(input('Ingresa el año de lanzamiento: '))
    tam_min = int(input('Ingresa la duración de la película en minutos: '))
    director = str(input('Ingresa el director de la película: '))
    
    conexion = connect()
    
    conexion.execute('insert into DVDs(Titulo,A_Lanza,Tam_min,Director) values (?,?,?,?)', (titulo, a_lanz, tam_min, director))
    
    conexion.commit()
    
    conexion.close()
    print("Agregado correctamente")
    
def edit():
    print()

def delete():
    print()

def find():
    conexion = sqlite3.connect("db_DVD.db")
    codigo=int(input("Escriba el codigo de la pelicula: "))
    cursor=conexion.execute("select Titulo,A_Lanza,Tam_min,Director from DVDs where codigo=?", (codigo, ))
    fila=cursor.fetchone()
    if fila!=None:
        print(fila)
    else:
        print("No existe ninguna película con ese código.")
    conexion.close()
    
#Filtrar for rango de articulos

#55    conexion = sqlite3.connect("db_DVD.db")
#   año = float(input("Escriba el año: "))
 #   cursor=conexion.execute("select Titulo,A_Lanza,Tam_min,Director from DVDs where A_Lanza=?", (año, ))
  #  filas=cursor.fetchone()
   # if len(filas)>0:
    #    for fila in filas:
     #       print(fila)
    #else:
       # print("No existe un artículo con un precio menor al seleccionado: ")
    conexion.close()
    pass
    print()

def present():
    conexion = connect()
    cursor = conexion.execute("select codigo,Titulo,A_Lanza,Tam_min,Director from DVDs")
    for fila in cursor:
        print(fila)
    conexion.commit()
    conexion.close()
    print()

def listsss():
    print()

def export():
    print()

def search():
    print()

#variables
opc = -1
a = 0

#menu
print('-------------------------------')
print('--------- Bienvenido ----------')
print('-------------------------------')


create()


while opc != 0:
    print('Selecciona la opción que deseé realizar:')
    print('1: Agregar un elemento')
    print('2: Editar un elemento')
    print('3: Eliminar un elemento')
    print('4: Encontrar un elemento')
    print('5: Presentar un elemento')
    print('6: Exportar un elemento')
    print('0: Finalizar el programa')
    print()
    
    while a != 1:
        opc = input('Elija una opción: ')
        if is_int(opc):
            opc = int(opc)
            a = 1
        else:
            print('Esa no es una opción valida.')
    
    if opc == 1:
        add()
        a = 0
    
    elif opc == 2:
        edit()
        a = 0
    
    elif opc == 3:
        delete()
        a = 0
    
    elif opc == 4:
        find()
        a = 0
    
    elif opc == 5:
        present()
        a = 0
    
    elif opc == 6:
        export()
        a = 0
    
    elif opc == 0:
        print('----------------------------------')
        print('-- Gracias por usar el programa --')
        print('----------------------------------')
    
    else:
        print('Esa no es una opción válida')