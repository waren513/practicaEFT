def mostrar_menu():
    print("============== MENU PRINCIPAL ===============")
    print("1.-Stock por categoria")
    print("2.-Busqueda de productos por rango de precio")
    print("3.-Actualizar precio de producto")
    print("4.- Agregar producto")
    print("5.-Eliminar producto")
    print("6.-Salir")
    print("=============================================")

def validar_opcion():
   while True:
       try:
            opcion = int(input("Ingrese una opcion del 1 al 6"))
            if opcion > 6 or opcion <= 0:
                print("Ingrese numero valido del menu")
            else:
                return opcion
    except valuerror:
        print("Ingrese un numero entero porfavor")
    return opcion

def stock_categoria(categoria,productos,venta):
    total_stock = 0
    
    


    
