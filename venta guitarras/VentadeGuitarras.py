import os
import pyfiglet
from datetime import datetime

productos = []
ventas = []

print(pyfiglet.figlet_format("guitarras"))
print("""Autores: Damián Sandoval
         Jose Quiero""")
os.system("pause")


fecha="13-06-2024"
folio=10000



archivo= "productos.txt"
archivo2= "ventas_prod.txt"



def cargar_productos(archivo):
    with open (archivo, "r") as file:
        for linea in file:
            linea = linea.strip()
            datos = linea.split(",")
            try:  
                id_producto = datos[0]
                nombre_producto = datos[1]
                marca = datos[2]
                stock_producto = int(datos[3])
                precio_producto = int(datos[4])
                productos.append([id_producto, nombre_producto, marca, stock_producto, precio_producto])

            except:
                print('Error')

cargar_productos(archivo)

def cargar_ventas(archivo):
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
                ventas.append([folio, fecha, id, stock_producto, precio_producto])

            except:
                print('Error')

cargar_ventas(archivo2)

def get_folio():
    elemento= len(ventas)-1
    return (ventas[elemento])[0]

id=""
opc=0

def buscar_id(id):
    for i in productos:
        if i[0] == id:           
           return i
       
opcion = 0


while opcion !=5:
    os.system("cls")
    opc = 0
    
    

    print("ultimo folio realizado: ",())
    print("""
                SISTEMA DE VENTAS
            
            1.  Venta de Guitarras
            2.  Reportes
            3.  Mantenedores
            4.  Administracion
            5.  Salir
             
         """ )
        
    opc=int(input("Ingresa una opcion entre 1-5: "))
        
    match opc:
        case 1:
            respuesta = "s"
            while True:
                    
                os.system("cls")
                print("   PRODUCTO        \n")
                try:
                    print("{:<5} {:<20} {:<15} {:<10} {:<10}".format("ID", "Nombre", "Marca", "Stock", "Precio"))
                    print("="*60)
                    for producto in productos:
                        print("{:<5} {:<20} {:<15} {:<10} {:<10}".format(producto[0], producto[1], producto[2], producto[3], producto[4]))
                    print("="*60)
                    while True:
                        id_producto = input("Ingrese la ID de la Guitarra: ")
                        if len(id_producto) == 4:
                            break
                        else:
                            print("Error: la ID debe tener 4 caracteres.")
                    
                    cantidad = int(input("Ingrese la cantidad de productos que desea comprar: "))
                    producto_encontrado = None
                    for producto in productos:
                        if producto[0] == id_producto:
                            producto_encontrado = producto
                            break

                    if producto_encontrado:
                        stock_disponible = producto_encontrado[3]
                        precio_unitario = producto_encontrado[4]

                        if cantidad <= stock_disponible:
                            valor_total = cantidad * precio_unitario
                            fecha_act = datetime.now().strftime("%d-%m-%Y")  # Obtener la fecha actual
                            fecha_act = ventas[-1][0] + 1 if ventas else 10000
                            ventas.append([fecha_act, fecha_act, id_producto, cantidad, valor_total])

                            producto_encontrado[3] -= cantidad
                            print(f"Venta realizada exitosamente. Total a pagar: ${valor_total}")
                        else:
                            print("Error: La cantidad solicitada sobrapasa el stock disponible.")
                    else:
                        print("Error: Producto no encontrado.")

                    respuesta = input("Desea comprar otra cosas? [s/n]: ").lower()
                    if respuesta != 's':
                        break
                    
                except ValueError:
                    print("Error: entrada inválida, por favor ingrese un número.")
                except Exception as ex:
                    print(f"Error inesperado: {ex}")
                
                os.system("pause")
        
        case 2:
            os.system("cls")
            op=0
            while op<=4:
                print("""
                        
                                REPORTES
                        ------------------
                        1. General de ventas (con total)
                        2. Ventas por fecha específica (con total)
                        3. Ventas por rangos de fechas (con total)
                        4. Salir
                        
                        """)
                op = int(input("Ingrese opción del 1-4: "))
                if op>=1 and op<=4:
                    os.system("cls")
                        
                    match op:
                        case 1:
                            total_general = sum(venta[4] for venta in ventas)
                            print("Ventas totales:")
                            for venta in ventas:
                                print(venta[0], venta[1], venta[2], venta[3], venta[4])
                            print("Total de ventas: ", total_general)
                            
                        case 2:
                            fecha = input("Ingrese fecha (dd-mm-aaaa): ")
                            total_fecha = sum(venta[4] for venta in ventas if venta[1] == fecha)
                            print(f"Ventas para la fecha {fecha}:")
                            for venta in ventas:
                                if venta[1] == fecha:
                                    print(venta[0], venta[1], venta[2], venta[3], venta[4])
                            print("Total de ventas para la fecha: ", total_fecha)
                        
                        case 3:
                            fecha_inicio = input("Ingrese la fecha de inicio (dd-mm-aaaa): ")
                            fecha_fin = input("Ingrese la fecha de termino (dd-mm-aaaa): ")
                            rango = sum(venta[4] for venta in ventas if fecha_inicio <= venta[1] <= fecha_fin)
                            print(f"Ventas en el rango {fecha_inicio} a {fecha_fin}:")
                            for venta in ventas:
                                if fecha_inicio <= venta[1] <= fecha_fin:
                                    print(venta[0], venta[1], venta[2], venta[3], venta[4])
                            print("Total de ventas para el rango de fechas: ", rango)
                    
                    if op == 4:
                        break
                    os.system("pause")
        
        case 3:
            os.system("cls")
            op=0
            while op<=6:
                print("""
                        MANTENEDOR DE PRODUCTOS
                    -------------------------------
                    1. Agregar producto
                    2. Buscar producto
                    3. Eliminar producto
                    4. Modificar producto
                    5. Listar productos
                    6. Salir del menú principal

                    """)
                op = int(input("Ingrese una opción del 1-6: "))

                if op>=1 and op<=6:
                    os.system("cls")
                    match op:
                        case 1: 
                            print("\n Agregar Guitarra\n")
                            print("Agregar datos a la Lista de Guitarras \n")
                            id_producto = input("Ingrese la id de la Guitarra: ")
                            nombre_producto = input("Ingrese el nombre de la Guitarra: ")
                            marca = input("Ingrese la marca de la Guitarra: ")
                            stock_producto = int(input("Ingrese el Stock de la Guitarra: "))
                            precio_producto = int(input("Ingrese el precio de la Guitarra: "))
                            
                            productos.append([id_producto, nombre_producto, marca, stock_producto, precio_producto])

                        case 2: 
                            id_producto = input("Ingrese id de la guitarra que busca: ")
                            producto_encontrado = None
                            for producto in productos:
                                if producto[0] == id_producto:
                                    producto_encontrado = producto
                                    break

                            if producto_encontrado:
                                print(f"Producto encontrado: {producto_encontrado}")
                            else:
                                print("Error: Guitarra no encontrada.")

                        case 3: 
                            id_producto = input("Ingrese la id de la Guitarra para eliminar: ")
                            producto_encontrado = None
                            for producto in productos:
                                if producto[0] == id_producto:
                                    producto_encontrado = producto
                                    break

                            if producto_encontrado:
                                productos.remove(producto_encontrado)
                                print("Producto eliminado.")
                            else:
                                print("Error: Producto no encontrado.")

                        case 4: 
                            id_producto = input("Ingrese la id de la Guitarra para modificar: ")
                            producto_encontrado = None
                            for producto in productos:
                                if producto[0] == id_producto:
                                    producto_encontrado = producto
                                    break

                            if producto_encontrado:
                                print("Modificar Producto")
                                nombre_producto = input(f"Ingrese el nuevo nombre para {producto_encontrado[1]}: ")
                                marca = input(f"Ingrese la nueva marca para {producto_encontrado[2]}: ")
                                nueva_stock = int(input(f"Ingrese el nuevo stock para {producto_encontrado[1]}: "))
                                nuevo_precio = int(input(f"Ingrese el nuevo precio para {producto_encontrado[1]}: "))

                                producto_encontrado[1] = nombre_producto
                                producto_encontrado[2] = marca
                                producto_encontrado[3] = nueva_stock
                                producto_encontrado[4] = nuevo_precio

                                print("El producto se modificado de manera correcta.")
                            else:
                                print("Error: El producto no fue encontrado.")

                        case 5: 
                            print("\n Lista de productos\n")
                            print("{:<5} {:<20} {:<15} {:<10} {:<10}".format("ID", "Nombre", "Marca", "Stock", "Precio"))
                            print("="*60)
                            for producto in productos:
                                print("{:<5} {:<20} {:<15} {:<10} {:<10}".format(producto[0], producto[1], producto[2], producto[3], producto[4]))
                            print("="*60)
                    
                    if op == 6:
                        break
                    os.system("pause") 
                                

        case 4: 
            os.system("cls")

            print("""
                    MENU ADMINISTRACION
                    
                1. Cargar datos
                2. Guardar datos
                3. Salir

                """)
            try:
                op = int(input("Ingrese una opción del 1-3: "))
                if op == 1:
                    cargar_productos(archivo)
                    cargar_ventas(archivo2)
                    print("Los datos fueron cargados correctamente.")
                elif op == 2:
                    print("Guardar Datos")
                    guardar_productos = "productos.txt"
                    guardar_ventas = "ventas_prod.txt"

                    with open(guardar_productos, "w") as file:
                        for producto in productos:
                            linea = ','.join(map(str, producto))
                            file.write(linea + '\n')
                        
                    with open(guardar_ventas, "w") as file:
                        for venta in ventas:
                            linea = ','.join(map(str, venta))  
                            file.write(linea + '\n')

                    print("Los datos se guardaron correctamente.")
                elif op == 3:
                    break
            except:
                print("Error, opción no válida")
        case 5:
            print("Fin del menú")
            break
