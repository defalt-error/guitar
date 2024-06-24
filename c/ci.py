import os
import pyfiglet

from datetime import datetime

def limpiar_pantalla():
    # Detectar el sistema operativo y ejecutar el comando apropiado
    if os.name == 'nt':  # Si el sistema operativo es Windows
        os.system('cls')
    else:  # Si el sistema operativo es Unix/Linux/MacOS
        os.system('clear')

now = datetime.now()

print(pyfiglet.figlet_format("guitarras"))
print("""Autores: Damián Sandoval
         Jose Quiero""")

input()

fecha="13-06-2024"
folio=10000

id = ""

opc = ""
opcion = 0

lista_productos = []
lista_ventas = []

archivo = "producto.txt"
archivo2 = "ventas_prod.txt"

def cargar_productos(archivo):
    # try y un exept por si no se encuentra el archivo (FALTA!!!!!)
    with open (archivo, "r") as file:
        leer_file = file.read()

        for linea in leer_file:
            linea = linea.strip()
            datos = linea.split(",")
            try:  
                id_producto = datos[0]
                nombre_producto = datos[1]
                genero_producto = datos[2]
                stock_producto = int(datos[3])
                precio_producto = int(datos[4])
                lista_productos.append([id_producto, nombre_producto, genero_producto, stock_producto, precio_producto])

            except FileNotFoundError: 
                print('No se encontro el archivo')

cargar_productos(archivo)

def cargar_ventas(archivo):
    # try y un exept por si no se encuentra el archivo 
    with open (archivo, "r") as file:
        for linea in file:
            linea = linea.strip()
            datos = linea.split(",")
            try:  
                folio = int(datos[0])
                fecha = datos[1]
                id = datos[2]
                stock_producto = int(datos[3])
                precio_producto = int(datos[4])
                lista_ventas.append([folio, fecha, id, stock_producto, precio_producto])

            except:
                print('Error')

cargar_ventas(archivo2)

def get_folio():
    elemento= len(lista_ventas)-1
    return (lista_ventas[elemento])[0]

def buscar_id(id):
    for i in lista_productos:
        if i[0] == id:           
           return i
       
def menu_principal():
    
    print("""
==================SISTEMA DE VENTAS==================
1.  Venta de Guitarras
2.  REPORTES
3.  Mantenedores
4.  Administracion
5.  Salir
=====================================================
""" )
            
def menu_opcion1():
    limpiar_pantalla()        
    while True:
        try:
            print("==============VENDER PRODUCTO===============")
            
            print("{:<5} {:<20} {:<15} {:<10} {:<10}".format("ID", "Nombre", "Marca", "Stock", "Precio"))
            print("="*60)
            for producto in lista_productos:
                print("{:<5} {:<20} {:<15} {:<10} {:<10}".format(producto[0], producto[1], producto[2], producto[3], producto[4]))
            print("="*60)
        # ================ PREGUNTAR ID =================
            producto = buscar_id(input('ingrese ID (para volver al menu principal "v"): '))
            if producto == "v":
                break
            
            print(producto[0]," ",producto[1]," ",producto[2]," ",int(producto[3])," ",int(producto[4]))

        # =============== PREGUNTAR CANTIDAD ===============
            cantidad = int(input("ingrese cantidad a comprar: "))

            stock = producto[3]
            valor = cantidad*producto[4]
            producto[3]-=cantidad

            # DARLE UN VALOR A RESPUESTA (FALTA!!!!!!)
            if respuesta.lower() == 's':
                if cantidad <= stock:
                    print(f"El valor de esta compra por {cantidad} productos es de: {valor}")
                    respuesta = input("Desea Otra compra? [s]/[n]: ")
                    if respuesta.lower() == 'n':
                        break
                else:
                    print("Error el stock no es suficiente")
            else:
                break
                
        except ValueError:
                print("Error: entrada inválida, por favor ingrese un número.")
        except Exception as e:
                print(f"Error inesperado: {e}")     

def menu_opcion2():
    limpiar_pantalla()
    
    while True:
        print("""
=====================REPORTES=====================
1.General de ventas (con total)
2.Ventas por fechas especifica (con total)
3.Ventas por rangos (con total)
4. salir
==================================================
        """)
            
        opc = input("ingrese opcion del 1-4:")
        while not opc.isalnum():
            print("ingrese numeros")
            opc = input("ingrese opcion del 1-4:")
        opc = int(opc)

        if opc>=1 and opc<=4:
            limpiar_pantalla()

            match opc:
                case 1:
                    e = 0
                    for venta in lista_ventas:
                        print(venta[0]," ",venta[1]," ",venta[2]," ",venta[3]," ",venta[4])
                        e = e + venta[4]
                    print("total= ", e)

                case 2:
                    fecha = input("ingrese fecha (dd-mm-aaaa): ")
                    e=0
                    for venta in lista_ventas:
                        if venta[1] == fecha:
                            e=e+venta[4]
                            print(venta[0]," ",venta[1]," ",venta[2]," ",venta[3]," ",venta[4])
                    print("total: ",e)

                case 3:
                        e=0
                        fecha_inicio=input("ingrese la fecha de inicio: ")
                        fecha_termino=input("ingrese la fecha de termino: ")
                        for venta in lista_ventas:
                            if venta[1] >= fecha_inicio and venta[1] <= fecha_termino:
                                e=e+venta[4]
                                print(venta[0]," ",venta[1]," ",venta[2],venta[3]," ",venta[4])
                                print("total= ",e)
        
                case 4:
                    break
                
        input()

def menu_opcion3():
    limpiar_pantalla()
    
    while True:
        print("""
                
=================MANTENEDOR DE productos=================  
1. Agregar
2. Buscar
3. Eliminar
4. Modificar
5. Listar
6. Salir del menu principal
=========================================================
        """)

        opc = input("Ingrese una opcion del 1-6: ")
        while not opc.isalpha():
            print("ingrese nuemros")
            opc = input("Ingrese una opcion del 1-6: ")
        opc = int(opc)

        if opc>=1 and opc<=6:
            limpiar_pantalla()
            match opc:
                case 1: 
                    print("\n Agregar Guitarra\n")
                    #agregar
                    print("Agregar datos a la Lista de Guitarras \n")
                    id=input("Ingrese la id de la Guitarra:  ")
                    prod = input("Ingrese la Guitarra:  ")
                    marca = input("Ingrese la marca:  ")
                    stock = int(input("Ingrese el Stock:  "))
                    precio = int(input("Ingrese el precio:  "))
                
                    lista_productos.append([id,prod,marca,stock,precio])

                case 2: 
                    id=input("Ingrese id de la guitarra a buscar: ")
                    sw=0
                    for i in lista_productos:
                        if i[0] == id:
                            sw=1
                            print(i[0]," ",i[1]," ",i[2]," ",i[3]," ",i[4])
                            break

                    if sw==0:
                        print("Error, esta gitarra no existe")

                case 3: 
                    try:
                            id=input("Ingrese una Guitarra a eliminar:  ")
                            lista=buscar_id(id)

                            if lista != -1:
                                lista_productos.remove(lista)
                                print(lista_productos)
                            else:
                                print("Error, la guitarra no existe")
                    except ValueError:
                        print("Error: entrada inválida, por favor ingrese un número.")
                
                case 4: 
                    print("\n Modificar\n")
                    id=input("Ingrese un id a buscar:  ")

                    nueva_id=(input("Ingrese la nueva id: "))
                    nueva_guitarra=(input("Ingrese la nueva guitarra: "))
                    nueva_marca=(input("Ingrese la nueva marca: "))
                    nueva_stock=(input("Ingrese el stock: "))
                    nueva_precio=(input("ingrese el precio: "))
                    lista=buscar_id(id)

                    if lista != -1:
                        lista[0]=nueva_id
                        lista[1]=nueva_guitarra
                        lista[2]=nueva_marca
                        lista[3]=nueva_stock
                        lista[4]=nueva_precio
                        print(lista_productos)

                    else:
                        print("Error, id no existe")


                case 5: 
                    print("\n Listar productos\n")
                    for i in lista_productos:
                            print(i[0],"",i[1],"",i[2],"",i[3],"",i[4])

            if opc == 6:
                break

            input()
                        


def menu_opcion4(): 
    print("lista de productos")

    while True:
        print("""
================MENU ADMINISTRACION================
1. Cargar datos
2. Respaldo datos (grabar Actualizar)
3. Salir
===================================================
        """)
# cargar datos: Esto lee todo lo que contiene los archivos productos.txt y ventas_ptod.txt y cargar las lista productos y ventas
        
        opc = input("ingrese opcion")
        while not opc.isnumeric():
            print("Ingrese numeros")
            opc = input("ingrese opcion")
        opc = int(opc)

        if opc == 1:
            with open(archivo,"r") as archivo_producto:
                leer_archivo = archivo_producto.read()
                for x in leer_archivo:
                    print(x)   

        print("Fin del menu")

while True:
    menu_principal()

    opc = input("Ingresa una opcion entre 1-5: ")
    while not opc.isnumeric():
         print("ingrese numeros")
         opc = input("Ingresa una opcion entre 1-5: ")
    opc = int(opc)

    if opc == 1:
        menu_opcion1()

    elif opc == 2:
        menu_opcion2()

    elif opc == 3:
        menu_opcion3()

    elif opc == 4:
        menu_opcion4()
        
    elif opc == 5:
        break
    else:
        print("Opcion fuera de los parametros")
    