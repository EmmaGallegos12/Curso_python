import csv

def cargar_csv(nombre_archivo, columna_llave):
    """Carga un archivo CSV y devuelve un diccionario con la columna especificada como clave"""
    diccionario_datos = {}
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                clave = fila[columna_llave]
                diccionario_datos[clave] = fila
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")

    return diccionario_datos

def guardar_csv(nombre_archivo, diccionario_datos, encabezados):
    """Guarda un diccionario de datos en un archivo CSV con los encabezados especificados"""
    try:
        with open(nombre_archivo, mode='w', encoding='utf-8', newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=encabezados)
            escritor.writeheader()
            for datos_fila in diccionario_datos.values():
                escritor.writerow(datos_fila)
    except Exception as e:
        print(f"Error al guardar '{nombre_archivo}': {e}")

def listar_por_clase(diccionario_animales, id_clase, diccionario_clases):
    """Recorre el diccionario de animales y muestra los que coinciden con la clase"""
    nombre_clase = diccionario_clases.get(id_clase, {}.get('Clase_tipo', 'Desconocida'))
    print(f"Animales de la clase '{nombre_clase}':")

    encontrados = False

    for animal in diccionario_animales.values():
        if animal.clasificacion == id_clase:
            print(f"- {animal}")
            encontrados = True

    if not encontrados:
        print("No se encontraron animales de esta clase.")

def listar_por_caracteristica(diccionario_animales, caracteristicas):
    """Filtra animales basandose en si poseen una caracteristica especifica"""
    print(f"Animales con las características: {caracteristicas}")
    encontrados = False

    for animal in diccionario_animales.values():
        if animal.caracteristicas.get(caracteristicas) == '1':
            print(f"- {animal}")
            encontrados = True

    if not encontrados:
        print("No se encontraron animales con estas características.")  

def recolectar_datos_nuevo_animal(diccionario_clases, caracteristicas_requeridas):
    """
    Solicita al usuario los datos para un nuevo animal y los valida.
    """
    print("\n--- Agregar Nuevo Animal ---")
    nombre = input("Ingresa el nombre del animal: ").strip().lower()
    
    if not nombre:
        print("El nombre no puede estar vacío.")
        return None

    print("\nClases disponibles:")
    for id_c, datos_c in diccionario_clases.items():
        print(f"{id_c}. {datos_c['Clase_tipo']}")
        
    clase_id = input("Ingresa el ID de la clasificación: ").strip()
    if clase_id not in diccionario_clases:
        print("Clase inválida. Operación cancelada.")
        return None

    print("\nA continuación, define sus características.")
    print("Ingresa '1' para Sí, '0' para No (o el número correspondiente para patas).")
    
    nuevas_caracteristicas = {}
    for car in caracteristicas_requeridas:
        valor = input(f"¿{car.capitalize()}?: ").strip()
        # Validación muy básica para asegurar que haya un valor
        nuevas_caracteristicas[car] = valor if valor else '0'

    return nombre, clase_id, nuevas_caracteristicas
