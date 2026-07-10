

#   - Dos diccionarios relacionados, pasados siempre como argumento
#     (NUNCA accedidos como variables globales dentro de funciones).
#   - Funciones con responsabilidad única.
#   - Validaciones independientes por campo.
#   - Manejo de excepciones para datos no numéricos.
#   - Reutilización de buscar_codigo() en actualizar y eliminar.
# ============================================================


def leer_opcion():
    """
    Lee la opción del menú principal.
    No recibe parámetros.
    Valida que sea un número entero entre 1 y 6.
    Maneja la excepción si el usuario ingresa algo que no es un entero.
    Retorna la opción ya validada como número entero.
    """
    # Se repite hasta que el dato ingresado sea válido (entero entre 1 y 6).
    while True:
        try:
            # input() siempre entrega un string; int() intenta convertirlo.
            # Si el usuario escribe algo como "hola", int() lanza ValueError.
            opcion = int(input("Ingrese opción: "))

            # Una vez que sabemos que es entero, validamos el rango.
            if 1 <= opcion <= 6:
                return opcion  # Dato válido: salimos de la función.
            else:
                # Es un entero, pero fuera del rango del menú (ej: 9, 0, -1).
                print("Debe seleccionar una opción válida")
        except ValueError:
            # Se activa cuando int(input(...)) falla por no ser numérico.
            print("Debe seleccionar una opción válida")


def stock_categoria(categoria, productos, ventas):
    """
    Opción 1 - Stock por categoría.
    Recibe la categoría a buscar y los dos diccionarios.
    No retorna ningún valor: imprime el resultado directamente.
    """
    total_stock = 0  # Acumulador de stock disponible.

    # Recorremos el diccionario 'productos' con .items() para tener
    # acceso simultáneo al código (clave) y a los datos (valor/lista).
    for codigo, datos in productos.items():
        # datos[1] corresponde al campo "categoria" según el diseño:
        # [nombre_producto, categoria, tamano, tipo_leche, es_temporada]
        # .lower() en ambos lados para que la búsqueda no distinga
        # mayúsculas/minúsculas (ej: "cafe" == "CAFE").
        if datos[1].lower() == categoria.lower():
            # Si el producto pertenece a la categoría buscada, vamos a
            # 'ventas' a buscar su stock disponible.
            # ventas[codigo] = [precio, stock_disponible]
            total_stock += ventas[codigo][1]

    print(f"El total de stock disponible es: {total_stock}")


def busqueda_precio(precio_min, precio_max, productos, ventas):
    """
    Opción 2 - Búsqueda de productos por rango de precio.
    Recibe el precio mínimo, máximo y los dos diccionarios.
    No retorna ningún valor: imprime el resultado directamente.
    """
    resultados = []  # Aquí guardamos los textos "Nombre--Código".

    # Recorremos 'ventas' porque ahí está el precio y el stock.
    for codigo, datos_venta in ventas.items():
        precio = datos_venta[0]   # [precio, stock_disponible]
        stock = datos_venta[1]

        # Condición (a): el precio debe estar dentro del rango ingresado.
        # Condición (b): debe tener stock disponible (distinto de 0).
        if precio_min <= precio <= precio_max and stock != 0:
            # Buscamos el nombre del producto en 'productos' usando
            # el mismo código como clave.
            nombre_producto = productos[codigo][0]  # [nombre_producto, ...]
            resultados.append(f"{nombre_producto}--{codigo}")

    if len(resultados) == 0:
        # No se encontró ningún producto que cumpla ambas condiciones.
        print("No hay productos en ese rango de precios.")
    else:
        # sorted() ordena la lista alfabéticamente (ascendente por defecto).
        resultados_ordenados = sorted(resultados)
        print(f"Los productos encontrados son: {resultados_ordenados}")


def buscar_codigo(codigo, ventas):
    """
    Función auxiliar reutilizable.
    Recibe el código a buscar y el diccionario 'ventas'.
    Retorna True si el código existe como clave, False si no existe.
    """
    # 'in' sobre un diccionario revisa solamente sus claves,
    # por eso es la forma correcta y eficiente de verificar existencia.
    return codigo in ventas


def actualizar_precio(codigo, nuevo_precio, ventas):
    """
    Opción 3 - Actualizar precio de un producto.
    Recibe el código, el nuevo precio y el diccionario 'ventas'.
    Retorna True si actualizó correctamente, False si el código no existe.
    """
    # Reutilizamos buscar_codigo() en vez de repetir la lógica de búsqueda.
    if buscar_codigo(codigo, ventas):
        # ventas[codigo] = [precio, stock_disponible]
        # Solo modificamos la posición 0 (el precio), sin tocar el stock.
        ventas[codigo][0] = nuevo_precio
        return True
    else:
        return False


def validar_codigo_nuevo(codigo, productos):
    """Valida que el código no esté vacío/en blanco y que no exista aún."""
    # .strip() elimina espacios al inicio y al final; si lo que queda
    # es una cadena vacía, significa que el dato era vacío o solo espacios.
    if codigo.strip() == "":
        return False
    if codigo in productos:
        return False
    return True


def validar_texto_no_vacio(texto):
    """Valida que un campo de texto no esté vacío ni contenga solo espacios."""
    return texto.strip() != ""


def validar_entero_positivo(valor_texto):
    """
    Valida que el valor ingresado sea un número entero mayor que cero.
    Recibe el dato como string (tal como llega desde input()).
    """
    try:
        valor = int(valor_texto)
        return valor > 0
    except ValueError:
        # Si no se puede convertir a entero, no es válido.
        return False


def validar_entero_no_negativo(valor_texto):
    """Valida que el valor ingresado sea un número entero mayor o igual a cero."""
    try:
        valor = int(valor_texto)
        return valor >= 0
    except ValueError:
        return False


def validar_tamano(tamano_texto):
    """Valida que el tamaño sea exactamente 'chico', 'mediano' o 'grande'."""
    return tamano_texto in ("chico", "mediano", "grande")


def validar_es_temporada(respuesta):
    """Valida que la respuesta de '¿es producto de temporada?' sea 's' o 'n'."""
    return respuesta in ("s", "n")


def agregar_producto(codigo, nombre_producto, categoria, tamano, tipo_leche,
                      es_temporada, precio, stock_disponible,
                      productos, ventas):
    """
    Agrega un nuevo registro en ambos diccionarios.
    Se asume que TODOS los datos ya fueron validados antes de llegar aquí.
    Retorna True si se agregó, False si el código ya existía.
    """
    # Verificación final de seguridad (no debería ocurrir si el programa
    # principal ya validó con validar_codigo_nuevo, pero evita duplicados).
    if codigo in productos:
        return False

    # Insertamos el registro descriptivo en 'productos', respetando el
    # orden de campos definido en el enunciado.
    productos[codigo] = [nombre_producto, categoria, tamano, tipo_leche,
                          es_temporada]

    # Insertamos el registro operativo en 'ventas'.
    ventas[codigo] = [precio, stock_disponible]

    return True


def eliminar_producto(codigo, productos, ventas):
    """
    Opción 5 - Eliminar producto.
    Recibe el código y ambos diccionarios.
    Retorna True si eliminó el registro, False si el código no existe.
    """
    # Reutilizamos buscar_codigo() para evitar duplicar la lógica de búsqueda.
    if buscar_codigo(codigo, ventas):
        # del elimina la entrada completa (clave + valor) del diccionario.
        del productos[codigo]
        del ventas[codigo]
        return True
    else:
        return False


def mostrar_menu():
    """Muestra el menú principal en pantalla. No recibe ni retorna nada."""
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

# ----------------------------------------------------------
# Diccionario 'productos': información descriptiva.
# clave = código de producto
# valor = [nombre_producto, categoria, tamano, tipo_leche, es_temporada]
# ----------------------------------------------------------
productos = {
    'P001': ['Capuccino Clásico', 'cafe', 'mediano', 'entera', False],
    'P002': ['Latte Vainilla', 'cafe', 'grande', 'descremada', True],
    'P003': ['Té Verde Helado', 'te', 'mediano', 'sin leche', False],
    'P004': ['Mocha Avellana', 'cafe', 'grande', 'entera', True],
    'P005': ['Chocolate Caliente', 'bebida', 'chico', 'entera', False],
    'P006': ['Té Chai Latte', 'te', 'mediano', 'descremada', True],
}

# ----------------------------------------------------------
# Diccionario 'ventas': información operativa.
# clave = mismo código de producto
# valor = [precio, stock_disponible]
# ----------------------------------------------------------
ventas = {
    'P001': [2500, 15],
    'P002': [3200, 0],
    'P003': [2800, 10],
    'P004': [3500, 4],
    'P005': [2200, 7],
    'P006': [3100, 9],
}

# Ciclo principal del menú: se repite mientras el usuario no elija salir.
# Usamos while (no for) porque no sabemos de antemano cuántas veces
# el usuario interactuará con el menú: la condición de parada (opción
# de salida) depende de su decisión durante la ejecución.
continuar = True
while continuar:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        # ----- Opción 1: Stock por categoría -----
        categoria = input("Ingrese categoría a consultar: ")
        stock_categoria(categoria, productos, ventas)

    elif opcion == 2:
        # ----- Opción 2: Búsqueda por rango de precio -----
        # La validación de que sean enteros ocurre AQUÍ, en el
        # programa principal, como lo exige el enunciado.
        precio_min = None
        precio_max = None
        while precio_min is None or precio_max is None:
            try:
                precio_min = int(input("Ingrese precio mínimo: "))
                precio_max = int(input("Ingrese precio máximo: "))
            except ValueError:
                print("Debe ingresar valores enteros")
                precio_min = None
                precio_max = None

        busqueda_precio(precio_min, precio_max, productos, ventas)

    elif opcion == 3:
        # ----- Opción 3: Actualizar precio de producto -----
        repetir = "s"
        while repetir == "s":
            codigo = input("Ingrese código del producto: ").upper()

            # Validamos que el nuevo precio sea un entero positivo
            # antes de llamar a la función de actualización.
            nuevo_precio_valido = False
            while not nuevo_precio_valido:
                nuevo_precio_texto = input("Ingrese nuevo precio: ")
                if validar_entero_positivo(nuevo_precio_texto):
                    nuevo_precio = int(nuevo_precio_texto)
                    nuevo_precio_valido = True
                else:
                    print("El precio debe ser un entero positivo")

            # El programa principal decide el mensaje SOLO según
            # el valor booleano que retorna actualizar_precio().
            if actualizar_precio(codigo, nuevo_precio, ventas):
                print("Precio actualizado")
            else:
                print("El código no existe")

            repetir = input("¿Desea actualizar otro precio (s/n)?: ").lower()

    elif opcion == 4:
        # ----- Opción 4: Agregar producto -----
        codigo = input("Ingrese código del producto: ").upper()

        if not validar_codigo_nuevo(codigo, productos):
            print("El código no es válido o ya existe")
        else:
            nombre_producto = input("Ingrese nombre del producto: ")
            if not validar_texto_no_vacio(nombre_producto):
                print("El nombre no puede estar vacío")
            else:
                categoria = input("Ingrese categoría: ")
                if not validar_texto_no_vacio(categoria):
                    print("La categoría no puede estar vacía")
                else:
                    tamano = input(
                        "Ingrese tamaño (chico/mediano/grande): "
                    ).lower()
                    if not validar_tamano(tamano):
                        print("El tamaño ingresado no es válido")
                    else:
                        tipo_leche = input("Ingrese tipo de leche: ")
                        if not validar_texto_no_vacio(tipo_leche):
                            print("El tipo de leche no puede estar vacío")
                        else:
                            es_temporada_resp = input(
                                "¿Es producto de temporada? (s/n): "
                            ).lower()
                            if not validar_es_temporada(es_temporada_resp):
                                print("Debe responder 's' o 'n'")
                            else:
                                precio_texto = input("Ingrese precio: ")
                                if not validar_entero_positivo(precio_texto):
                                    print(
                                        "El precio debe ser un entero positivo"
                                    )
                                else:
                                    stock_texto = input(
                                        "Ingrese stock disponible: "
                                    )
                                    if not validar_entero_no_negativo(
                                        stock_texto
                                    ):
                                        print(
                                            "El stock debe ser un entero "
                                            "mayor o igual a cero"
                                        )
                                    else:
                                        # Todos los datos son válidos:
                                        # convertimos los numéricos y
                                        # el booleano antes de agregar.
                                        es_temporada = (
                                            es_temporada_resp == "s"
                                        )
                                        precio = int(precio_texto)
                                        stock_disponible = int(stock_texto)

                                        if agregar_producto(
                                            codigo, nombre_producto,
                                            categoria, tamano,
                                            tipo_leche, es_temporada,
                                            precio, stock_disponible,
                                            productos, ventas,
                                        ):
                                            print("Producto agregado")
                                        else:
                                            print("El código ya existe")

    elif opcion == 5:
        # ----- Opción 5: Eliminar producto -----
        codigo = input("Ingrese código del producto a eliminar: ").upper()

        # Igual que en la opción 3: el principal decide el mensaje
        # basándose exclusivamente en el booleano retornado.
        if eliminar_producto(codigo, productos, ventas):
            print("Producto eliminado")
        else:
            print("El código no existe")

    elif opcion == 6:
        # ----- Opción 6: Salir -----
        print("Programa finalizado.")
        continuar = False  # Esto detiene el ciclo while.

