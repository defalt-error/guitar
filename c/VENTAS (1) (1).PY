import os
os.system("cls")
fecha="13-06-2024"
folio=10000


productos = []
ventas=[]

archivo= "producto.txt"
archivo2= "ventas_prod.txt"

def cargar_productos(archivo):
    with open (archivo, "r") as file:
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
    
    

    print("ultimo folio: ",())
    print("""
                SISTEMA DE VENTAS
            
            1.  Venta de Guitarras
            2.  REPORTES
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
                    print("   VENDER PRODUCTO        \n")
                    # mostrar lista de productos #
                    producto=buscar_id(input('ingrese ID:'))
                    #print("Encontrado en el elemento ",i)
                    print(producto[0]," ",producto[1]," ",producto[2]," ",int(producto[3])," ",int(producto[4]))
                    cantidad=int(input("ingrese cantidad a comprar: "))
                    stock = producto[3]
                    valor = cantidad*producto[4]
                    producto[3]-=cantidad
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
                        
                        

            case 2:
                os.system("cls")
                op=0
                while op<=4:
                    print("""
                            
                                    REPORTES
                            ------------------
                            1.General de ventas (con total)
                            2.Ventas por fechas especifica (con total)
                            3.Ventas por rangos (con total)
                            4. salir
                            
                            """)
                    op = int(input("ingrese opcion del 1-4:"))
                    if op>=1 and op<=4:
                        os.system("cls")
                            
                        match op:
                            case 1:
                                e=0
                                for venta in ventas:
                                    print(venta[0]," ",venta[1]," ",venta[2]," ",venta[3]," ",venta[4])
                                    e=e+venta[4]
                                print("total= ",e)
                            case 2:
                                fecha=input("ingrese fecha (dd-mm-aaaa): ")
                                e=0
                                for venta in ventas:
                                    if venta[1] == fecha:
                                        e=e+venta[4]
                                        print(venta[0]," ",venta[1]," ",venta[2]," ",venta[3]," ",venta[4])
                                print("total: ",e)

                            case 3:
                                e=0
                                fecha_inicio=input("ingrese la fecha de inicio: ")
                                fecha_termino=input("ingrese la fecha de termino: ")
                                for venta in ventas:
                                    if venta[1] >= fecha_inicio and venta[1] <= fecha_termino:
                                        e=e+venta[4]
                                        print(venta[0]," ",venta[1]," ",venta[2],venta[3]," ",venta[4])
                                        print("total= ",e)
                                
                                
                    if op==4:
                        break
                    os.system("pause")  
            case 3:
                os.system("cls")
                op=0
                while op<=6:
                    print("""
                            MANTENEDOR DE productos
                        -------------------------------
                        1. Agregar
                        2. Buscar
                        3. Eliminar
                        4. Modificar
                        5. Listar
                        6. Salir del menu principal


                        """)
                    op = int(input("Ingrese una opcion del 1-6: "))

                
                    if op>=1 and op<=6:
                        os.system("cls")
                        match op:
                            case 1: 
                                print("\n Agregar Guitarra\n")
                                #agregar
                                print("Agregar datos a la Lista de Guitarras \n")
                                id=input("Ingrese la id de la Guitarra:  ")
                                prod=input("Ingrese la Guitarra:  ")
                                marca=input("Ingrese la marca:  ")
                                stock = int(input("Ingrese el Stock:  "))
                                precio = int(input("Ingrese el precio:  "))
                            
                                productos.append([id,prod,marca,stock,precio])

                            case 2: 
                                id=input("Ingrese id de la guitarra a buscar: ")
                                sw=0
                                for i in productos:
                                    if i[0] == id:
                                        sw=1
                                        print(i[0]," ",i[1]," ",i[2]," ",i[3]," ",i[4])
                                        break

                                if sw==0:
                                    print("Error, esta gitarra no existe")

                            case 3: 
                                
                                id=input("Ingrese una Guitarra a eliminar:  ")

                                lista=buscar_id(id)

                                if lista != -1:
                                    productos.remove(lista)
                                    print(productos)
                                else:
                                    print("Error, la guitarra no existe")
                                    
                            
                            
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
                                    print(productos)
                                else:
                                    print("Error, id no existe")


                            case 5: 
                                print("\n Listar productos\n")
                                for i in productos:
                                        print(i[0],"",i[1],"",i[2],"",i[3],"",i[4])

                        if op==6:
                            break
                        os.system("pause")          


            case 4:
                
        
                print("lista de productos")
                
                os.system("pause")
                """
                        MENU ADMINISTRACION
                        
                    1. Cargar datos
                    2. Respaldo datos (grabar Actualizar)
                    3. Salir



                    cargar datos: Esto lee todo lo que contiene los archivos productos.txt y ventas_ptod.txt y cargar las lista productos y ventas
                    """
                
            



    

print("Fin del menu")
