from funciones import cargar_csv, guardar_csv, listar_por_caracteristica, listar_por_clase, recolectar_datos_nuevo_animal
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

    encabezados_zoo = ['nombre_animal', 'pelo', 'plumas', 'huevos', 'leche', 'vuela', 'acuatico', 'depredador', 'dientes', 'espinazo', 'respira', 'venenoso', 'aletas', 'patas', 'cola', 'domestico', 'tamanio_gato', 'clase']
    lista_caracteristicas = encabezados_zoo[1:-1]
    animales_objetos = {}
    for nombre, datos in diccionario_animales_cvs.items():
        clasificacion_id = datos.pop('clase')
        animales_objetos[nombre] = Animal(nombre, clasificacion_id, datos)

    while True:
        opcion = display_menu()
        if opcion == '1':
            print("\nClases disponibles:")
            for id_c, datos_c in diccionario_clases.items():
                print(f"{id_c}. {datos_c['Clase_tipo']}")
            seleccion = input("Ingresa el ID de la clase que deseas listar: ")
            listar_por_clase(animales_objetos, seleccion, diccionario_clases)

        elif opcion == '2':
            print("\nEjemplos de características: pelo, plumas, vuela, acuatico, depredador, venenoso...")
            seleccion = input("Ingresa el nombre de la característica (en minúsculas): ").strip()
            listar_por_caracteristica(animales_objetos, seleccion)
        elif opcion == '3':
            datos_nuevo = recolectar_datos_nuevo_animal(diccionario_clases, lista_caracteristicas)
            if datos_nuevo:
                nombre, clase_id, caracteristicas = datos_nuevo
                if nombre in animales_objetos:
                    print(f"Error: El animal '{nombre}' ya existe en el sistema.")
                else:
                    animales_objetos[nombre] = Animal(nombre, clase_id, caracteristicas)
                    print(f"¡{nombre.capitalize()} agregado exitosamente!")

        elif opcion == '4':
            print("Preparando datos para guardar...")
            datos_a_guardar = {}
            for nombre, obj_animal in animales_objetos.items():
                fila = {'nombre_animal': nombre, 'clase': obj_animal.clasificacion}
                fila.update(obj_animal.caracteristicas)
                datos_a_guardar[nombre] = fila
                
            guardar_csv('zoo.csv', datos_a_guardar, encabezados_zoo)
            print("Cambios guardados. Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()