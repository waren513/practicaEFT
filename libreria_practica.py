def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))

            if 1 <= opcion <= 6:
                return opcion
            else:
                print("debe seleccionar una opcion válida")
        except ValueError:
            print("Debe seleccionar una opcion valida")

def stock_genero(genero, libros, inventario):

    total_stock = 0

    for codigo, datos in libros.items():
        if datos[1].lower() == genero.lower():
            total_stock += inventario[codigo][1]
    print(f"El total de estock disponible es: {total_stock}")

def Busqueda_precio(precio_min, precio_max, inventario, libros):
    resultados = []

    for codigo, datos_inventario in inventario.items():
        precio = datos_inventario[0]
        stock = datos_inventario[1]
        
        if precio_min <= precio <= precio_max and stock !=0:
            nombre_libro = libros[codigo][0]
            resultados.append(f"{nombre_libro}--{codigo}")

    if len(resultados) == 0:
        print("No hay libros en ese rango de precios")
    else:
        resultados_ordenados = sorted(resultados)
        print(f"los productos encontrados son: {resultados_ordenados}")

def buscar_codigo(codigo, libros):
    return codigo.upper() in [k.upper() for k in libros.keys()]

def actualizar_precio(codigo, nuevo_precio, libros, inventario):
    if buscar_codigo(codigo, libros):
        inventario[codigo.upper()][0] = nuevo_precio
        return True
    else:
        return False

def validar_codigo_nuevo(codigo, libros):
    if codigo.strip() == "":
        return False
    if codigo in libros:
        return False
    return True

def validar_texto_no_vacio(texto):
    return texto.strip() != ""

def validar_entero_positivo(valor_texto):
    try:
        valor = int(valor_texto)
        return valor > 0
    except ValueError:
        return False

def validar_entero_no_negativo(valor_texto):
    try:
        valor = int(valor_texto)
        return valor >= 0
    except ValueError:
        return False
    
def validar_encuadernacion(tipo):
    return tipo.lower() in ['blanda', 'dura', 'digital']

def validar_novedad_texto(texto):
    return texto.lower() in ['s', 'n']

def agregar_libro(codigo, titulo, genero, encuadernacion, autor, es_novedad, precio, stock, libros, inventario):
    if buscar_codigo(codigo, libros):
        return False
    
    cod_upper = codigo.upper()
    libros[cod_upper] = [titulo, genero, encuadernacion, autor, es_novedad]
    inventario[cod_upper] = [precio, stock]
    return True
def eliminar_libro(codigo, libros, inventario):
    if buscar_codigo(codigo, libros):
        cod_upper = codigo.upper()
        libros.pop(cod_upper)
        inventario.pop(cod_upper)
        return True
    return False

def mostrar_menu():
    print("============ MENÚ PRINCIPAL ==============")
    print("1.-Stock por Genero")
    print("2:-Busqueda de libros por rango de precio")
    print("3.-Actualizar precio de un libro")
    print("4.-Agregar precio de un libro")
    print("5.-Eliminar libro del catálogo")
    print("6.-Salir")
    print("==========================================")
          
libros = {
    'B001': ['Cien Anos de Soledad', 'novela', 'blanda', 'Gabriel Garcia Marquez', False],
    'B002': ['El Resplandor', 'terror', 'dura', 'Stephen King', True],
    'B003': ['Dune', 'ciencia ficcion', 'blanda', 'Frank Herbert', False],
    'B004': ['Dracula', 'terror', 'dura', 'Bram Stoker', False],
    'B005': ['Fundacion', 'ciencia ficcion', 'digital', 'Isaac Asimov', True]
}
          
inventario = {
    'B001': [15000, 12],
    'B002': [22000, 0],
    'B003': [18500, 8],
    'B004': [12000, 5],
    'B005': [9500, 14]
}

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        gen = input("Ingrese genero a consultar: ")
        stock_genero(gen, libros, inventario)

    elif opcion == 2:
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                if p_min >= 0 and p_max >= p_min:
                    break
                print("El precio mínimo debe ser mayor a 0 y menor o igual al máximo")
            except ValueError:
                print("Debe ingresar valores enteros")

        
        Busqueda_precio(p_min, p_max, inventario, libros) 

    elif opcion == 3:
        while True:
            cod = input("Ingrese código del libro: ")
            try:
                nuevo_p = int(input("Ingrese nuevo precio: "))
                if nuevo_p <= 0:
                    print("El precio debe ser un entero positivo.")
                    continue
            except ValueError:
                print("El precio debe ser un número entero.")
                continue 
            if actualizar_precio(cod, nuevo_p, libros, inventario):
                print("Precio actualizado")
            else:
                print("El codigo no existe")
                
            resp = input("¿Desea actualizar otro precio (s/n)?: ").lower()
            if resp != 's':
                break

    elif opcion == 4:
        cod = input("Ingrese código del libro: ")
        titulo = input("Ingrese el título del libro: ")
        genero = input("Ingrese género: ")
        encu = input("Ingrese encuadernacion (blanda/dura/digital): ")
        autor = input("Ingrese autor: ")
        nov = input("¿es novedad? (s/n): ")
        p_texto = input("Ingrese precio: ")
        s_texto = input("Ingrese stock disponible: ")
        
        if (validar_codigo_nuevo(cod, libros) and 
            validar_texto_no_vacio(titulo) and 
            validar_texto_no_vacio(genero) and 
            validar_encuadernacion(encu) and 
            validar_texto_no_vacio(autor) and 
            validar_novedad_texto(nov) and 
            validar_entero_positivo(p_texto) and 
            validar_entero_no_negativo(s_texto)):
            
            nov_bool = True if nov.lower() == 's' else False
            precio_int = int(p_texto)
            stock_int = int(s_texto)

            if agregar_libro(cod, titulo, genero, encu, autor, nov_bool, precio_int, stock_int, libros, inventario):
                print("libro agregado")
            else:
                print("El codigo ya existe")
        else:
            print("Error: Uno o mas datos ingresados no cumplen las validaciones")

    elif opcion == 5:
        cod = input("Ingrese el codigo del libro a eliminar: ")
        if eliminar_libro(cod, libros, inventario): 
            print("Libro eliminado")
        else:
            print("El codigo no existe")

    elif opcion == 6:
        print("Programa finalizado.")
        break
