import ast #Sirve para interpretar strings como estructuras de python
productos = []

def añadir_producto():
    producto={'nombre':"",'precio':"",'cantidad':""}

    nombre=str(input("Nombre del producto: "))
    precio=str(input("Ingresa el precio: "))
    cantidad=str(input("Ingrese la cantidad en stock: "))
    producto['nombre'] = nombre

    if productos == []:
        producto['precio'] = precio +"$"
        producto['cantidad'] = cantidad
        productos.append(producto)
    elif productos != []:
        for item in productos:
            if item['nombre'] == nombre:
                print("")
                print("Error el producto ya existe, volviendo al menú")
                print("")
                return
        producto['precio'] = precio +"$"
        producto['cantidad'] = cantidad    
        productos.append(producto)

     
    
        
    
    
def ver_productos():
    for producto in productos:
        print(f'{producto}\n')
    
def actualizar_producto():
        for producto in productos:
            
            productoCambiar = str(input("Seleccione el nombre del producto que desea cambiar: "))
            
          
            
            if productoCambiar == producto["nombre"]:
                print("1: -Cambiar nombre\n2:-Cambiar precio\n3:-Cambiar cantidad\n")
                
                accion = int(input('Seleccione la accion a realizar: '))
                if accion == 1 and productoCambiar != producto['nombre']:
                    newName= str(input("Ingrese el nuevo nombre: "))
                    producto['nombre'] = newName
                    break
                elif accion == 2 :
                    newPrice = str(input('Ingrese el nuevo precio: '))
                    producto['precio'] = newPrice +"$"
                    break
                elif accion == 3:
                    newCant = str(input("Ingrese la nueva cantidad"))
                    producto['cantidad'] = newCant
                    break
                else:
                    print("Numero ingresado no valido, volviendo al menú")
                    break
            else:
                print("El producto no existe")
                

def eliminar_producto():
    nombreEliminar= str(input("Ingrese el nombre del producto que desea eliminar: "))
    for dic in productos:
        if nombreEliminar == dic["nombre"]:
            productos.remove(dic)
        else:
            print("Este producto no existe")

def guardar_datos():
    
    with open("productos.txt","a") as file_g:
        for producto in productos:
            file_g.write(f'{producto}\n')
    

def cargar_datos():
    try:
        file_leer= open("productos.txt","r")
        for linea in file_leer:
            producto = ast.literal_eval(linea.strip())
            productos.append(producto)
        print(file_leer.read())
        file_leer.close()
    except FileNotFoundError:
        print("Archivo aún no existe\n")


def menu():
    cargar_datos()
    while True:
            print("1: Añadir producto\n")
            print("2: Ver todos los productos\n")
            print("3: Actualizar producto\n")
            print("4: Eliminar producto\n")
            print("5: Guardar datos y salir\n")     
    
            opcion = (input("Seleccione una opción: "))

            if opcion == "1" :
                añadir_producto()
            elif opcion == "2":
                ver_productos()
            elif opcion == "3":
                actualizar_producto()
            elif opcion ==  "4":
                eliminar_producto()
            elif opcion == "5":
                guardar_datos()
                break
            else:
                print("")
                print("Por favor ingrese una opcion valida")
                print("")
print("")
print("")
menu()