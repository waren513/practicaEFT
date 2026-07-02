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

    for codigo, datos in productos.items():
        if datos[1].lower() == categoria.lower():
            total_stock = += ventas[codigo][1]

    print(f"El total es de stock disponible es: {total_stock}")

def busqueda_precio(precio_min, precio_max, productos, ventas):
    resultados = []

    for codigo, datos_venta in ventas.items():
        precio = datos_venta[0]
        stock = datos_ventas[1]

        if precio_min <= precio <= precio_max and stock != 0:
            nombre_producto = productos[codigo][0]
            resultados.append(f"{nombre_producto}--{codigo}")
    if len(resultados) == 0:
        print("no hay productos en ese rango de precios.")
    else:
        resultados_ordenados = sorted(resultados)
        print(f"Los productos encontrados son: {resultados_ordenados}")

def buscar_codigo(codigo, ventas):
#dicionarios
producto = {
    'p1':['capuccino clasico','cafe','mediano','entera',False],
    'p2':['latte vainilla','cafe','grande','descremada',True],
    'p3':['té verde Helado','té','mediano','sin leche',False],
    'p4':['mocha Avellana','cafe','grande','entera',True],
    'p5':['chocolate caliente','bebida','chico','entera',False],
    'p6':['té Chai Latte','té','mediano','descremada',True]
}

ventas = {
    'p1':[2500, 15],
    'p2':[3200, 0],
    'p3':[2000, 10],
    'p4':[3500, 4],
    'p5':[2200, 7],
    'p6':[1100, 9]
}

    
    
    
    


    
