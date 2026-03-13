class Animal:
    """Clase para reprentar un animal"""
    def __init__(self, nombre, clasificacion, caracteristicas):
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.caracteristicas = caracteristicas

    def __str__(self):
        """Devuelve una representación legible del animal"""
        return f"{self.nombre} (Clase: {self.clasificacion})" 

    def __repr__(self):
        """Devuelve una representación detallada del animal"""
        return f"Animal(nombre='{self.nombre}', clasificacion='{self.clasificacion}', caracteristicas={self.caracteristicas})"