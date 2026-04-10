""" Frases célebres.py Archivo con las funciones básicas para manipular las frases célebres. de películas. """
import json
import csv

class Frase:
    def __init__(self, frase, pelicula):
        self.frase = frase
        self.pelicula = pelicula

    def __str__(self):
        """ Devuelve una representación en cadena de la frase célebre. """
        return f'"{self.frase}" - {self.pelicula}'
    
    def to_dict(self):
        """ Devuelve un diccionario con los atributos de la frase célebre. """
        return { "Frase": self.frase, "Película": self.pelicula }
    
    def to_json(self):
        """ Devuelve una representación en formato JSON de la frase célebre. """
        return json.dumps(self.to_dict(), ensure_ascii=False)
    
def cargar_frases(nombre_archivo):
    """ Carga las frases célebres desde un archivo JSON y devuelve una lista de objetos Frase. """
    frase = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if len(fila) == 2:
                    frase.append(Frase(fila[0], fila[1]))
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al cargar las frases: {e}")
    return frase


if __name__ == "__main__":
    frases = cargar_frases('frases_consolidadas.csv')
    for frase in frases[0:5]:
        print(frase)