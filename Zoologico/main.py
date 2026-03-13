from funciones import cargar_csv, guardar_csv, listar_por_caracteristica, listar_por_clase
from modelos import Animal

def display_menu():
    print("Bienvenido al Zoológico")
    print("1. Cargar animales desde CSV")
    print("2. Mostrar animales")
    print("3. Guardar animales en CSV")
    print("4. Salir")
    return input("Seleccione una opción: ")

def main():
    diccionario_clases = cargar_csv('clases.csv', 'Clase_id')
    diccionario_animales_cvs = cargar_csv('zoo.csv', 'nombre_animal')

    animales_objetos = {}
    for nombre, datos in diccionario_animales_cvs.items():
        clasificacion_id = datos.pop('clase')
        animales_objetos[nombre] = Animal(nombre, clasificacion_id, datos)

    while True:
        opcion = display_menu()
        if opcion == '1':
            print("Clases Disponibles:")
            for id_c, datos_c in diccionario_clases.items():
                print(f"{id_c}. {datos_c['Clase_tipo']}")
            seleccion = input("Seleccione una clase por su ID: ")
            listar_por_caracteristica(animales_objetos, seleccion)
        elif opcion == '2':
            for animal in animales_objetos.values():
                print(animal)
        elif opcion == '3':
            diccionario_para_guardar = {nombre: {'clase': animal.clasificacion, **animal.caracteristicas} for nombre, animal in animales_objetos.items()}
            guardar_csv('zoo_guardado.csv', diccionario_para_guardar, ['nombre_animal', 'clase'] + list(next(iter(diccionario_para_guardar.values())).keys()))
            print("Animales guardados en zoo_guardado.csv.")
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")