
alumnos = {
    'A01': ['juan','3ro medio']
    }

notas = {
    'A01': [6.5, 5.8, 7.0,]
    }
    
codigo = input("Ingrese el codigo de alumno: ")

if codigo in alumnos:
    lista_notas = notas[codigo]
    promedio = round(sum(lista_notas) / len(lista_notas),1)
    print(f"su promedio es : {promedio}")
else:
    print("alumno no encontrado")


    
