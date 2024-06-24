import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

fecha = "13-06-2024"
folio = 10000

productos = []
ventas = []

archivo_productos = "producto.txt"
archivo_ventas = "ventas_prod.txt"

def cargar_productos(archivo):
    with open(archivo, "r") as file:
        for linea in file:
            linea = linea.strip()
            datos = linea.split(",")
            try:
                id_producto = datos[0]
                nombre_producto = datos[1]
                genero_producto = datos[2]
                stock_producto = int(datos[3])
                precio_producto = int(datos[4])
                productos.append([id_producto, nombre_producto, genero_producto, stock_producto, precio_producto])
            except:
                print('Error al cargar productos')

def cargar_ventas(archivo):
    with open(archivo, "r") as file:
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
                print('Error al cargar ventas')

def get_folio():
    if ventas:
        return ventas[-1][0]
    return folio

def buscar_id(id):
    for i in productos:
        if i[0] == id:
            return i
    return None

cargar_productos(archivo_productos)
cargar_ventas(archivo_ventas)

while True:
    limpiar_pantalla()
    print(f"Último folio: {get_folio()}")
    print("""
                SISTEMA DE VENTAS
            
            1. Venta de Guitarras
            2. REPORTES
            3. Mantenedores
            4. Administración
            5. Salir
         """)
    opcion = int(input("Ingresa una opción entre 1-5: "))
    
    if opcion == 1:
        respuesta = "s"
        while respuesta.lower() == 's':
            limpiar_pantalla()
            print("   VENDER PRODUCTO\n")
            id_producto = input('Ingrese ID del producto: ')
            producto = buscar_id(id_producto)
            if producto:
                print(f"{producto[0]} {producto[1]} {producto[2]} {producto[3]} {producto[4]}")
                cantidad = int(input("Ingrese cantidad a comprar: "))
                stock = producto[3]
                valor = cantidad * producto[4]
                if cantidad <= stock:
                    producto[3] -= cantidad
                    print(f"El valor de esta compra por {cantidad} productos es de: {valor}")
                    respuesta = input("¿Desea otra compra? [s]/[n]: ")
                    ventas.append([get_folio() + 1, fecha, id_producto, cantidad, valor])
                else:
                    print("Error: el stock no es suficiente")
            else:
                print("Producto no encontrado")
            if respuesta.lower() == 'n':
                break

    elif opcion == 2:
        limpiar_pantalla()
        while True:
            print("""
                            REPORTES
                    ------------------
                    1. General de ventas (con total)
                    2. Ventas por fecha específica (con total)
                    3. Ventas por rango de fechas (con total)
                    4. Salir
            """)
            op = int(input("Ingrese opción del 1-4: "))
            if op == 1:
                limpiar_pantalla()
                e = sum(venta[4] for venta in ventas)
                for venta in ventas:
                    print(f"{venta[0]} {venta[1]} {venta[2]} {venta[3]} {venta[4]}")
                print(f"Total: {e}")
            elif op == 2:
                fecha_especifica = input("Ingrese fecha (dd-mm-aaaa): ")
                limpiar_pantalla()
                e = sum(venta[4] for venta in ventas if venta[1] == fecha_especifica)
                for venta in ventas:
                    if venta[1] == fecha_especifica:
                        print(f"{venta[0]} {venta[1]} {venta[2]} {venta[3]} {venta[4]}")
                print(f"Total: {e}")
            elif op == 3:
                fecha_inicio = input("Ingrese la fecha de inicio (dd-mm-aaaa): ")
                fecha_termino = input("Ingrese la fecha de término (dd-mm-aaaa): ")
                limpiar_pantalla()
                e = sum(venta[4] for venta in ventas if fecha_inicio <= venta[1] <= fecha_termino)
                for venta in ventas:
                    if fecha_inicio <= venta[1] <= fecha_termino:
                        print(f"{venta[0]} {venta[1]} {venta[2]} {venta[3]} {venta[4]}")
                print(f"Total: {e}")
            elif op == 4:
                break
            os.system("pause")

    elif opcion == 3:
        limpiar_pantalla()
        while True:
            print("""
                        MANTENEDOR DE PRODUCTOS
                    -------------------------------
                    1. Agregar
                    2. Buscar
                    3. Eliminar
                    4. Modificar
                    5. Listar
                    6. Salir del menú principal
            """)
            op = int(input("Ingrese una opción del 1-6: "))
            if op == 1:
                limpiar_pantalla()
                print("\nAgregar Guitarra\n")
                id = input("Ingrese la ID de la Guitarra: ")
                prod = input("Ingrese la Guitarra: ")
                marca = input("Ingrese la marca: ")
                stock = int(input("Ingrese el Stock: "))
                precio = int(input("Ingrese el precio: "))
                productos.append([id, prod, marca, stock, precio])
            elif op == 2:
                limpiar_pantalla()
                id = input("Ingrese ID de la guitarra a buscar: ")
                producto = buscar_id(id)
                if producto:
                    print(f"{producto[0]} {producto[1]} {producto[2]} {producto[3]} {producto[4]}")
                else:
                    print("Error: Esta guitarra no existe")
            elif op == 3:
                limpiar_pantalla()
                id = input("Ingrese ID de la guitarra a eliminar: ")
                producto = buscar_id(id)
                if producto:
                    productos.remove(producto)
                    print("Producto eliminado")
                else:
                    print("Error: La guitarra no existe")
            elif op == 4:
                limpiar_pantalla()
                id = input("Ingrese ID de la guitarra a modificar: ")
                producto = buscar_id(id)
                if producto:
                    nueva_id = input("Ingrese la nueva ID: ")
                    nueva_guitarra = input("Ingrese la nueva guitarra: ")
                    nueva_marca = input("Ingrese la nueva marca: ")
                    nuevo_stock = int(input("Ingrese el nuevo stock: "))
                    nuevo_precio = int(input("Ingrese el nuevo precio: "))
                    producto[0] = nueva_id
                    producto[1] = nueva_guitarra
                    producto[2] = nueva_marca
                    producto[3] = nuevo_stock
                    producto[4] = nuevo_precio
                    print("Producto modificado")
                else:
                    print("Error: ID no existe")
            elif op == 5:
                limpiar_pantalla()
                print("\nListar productos\n")
                for producto in productos:
                    print(f"{producto[0]} {producto[1]} {producto[2]} {producto[3]} {producto[4]}")
            elif op == 6:
                break
            os.system("pause")

    elif opcion == 4:
        limpiar_pantalla()
        print("Lista de productos")
        os.system("pause")
        print("""
                MENU ADMINISTRACIÓN

            1. Cargar datos
            2. Respaldo de datos (grabar/actualizar)
            3. Salir

            Cargar datos: Esto lee todo lo que contienen los archivos productos.txt y ventas_prod.txt y carga las listas productos y ventas.
        """)

    elif opcion == 5:
        print("Fin del menú")
        break

    os.system("pause")

