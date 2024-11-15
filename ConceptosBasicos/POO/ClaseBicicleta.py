
# Clase Bicicleta
    # Incluimos propiedades para color, tamaño y velocidad máxima
    # Constructor para inicializar velocidad a cero
    # Métodos para aumentar velocidad, disminuir velocidad y cambiar la velocidad máxima

class Bicicleta:
    color = ""
    tamanio = ""
    Vel_max = 15  # Velocidad máxima por defecto

    def __init__(self):
        # Inicializamos la velocidad actual a 0
        self.velocidad = 0

    def subirmarcha(self):
        # Aumenta la velocidad actual en 1 unidad
        self.velocidad += 1

    def bajarmarcha(self):
        # Disminuye la velocidad actual en 1 unidad
        self.velocidad -= 1

    def cambiarVelMax(self, maxVel):
        # Cambia la velocidad máxima de la bicicleta
        self.Vel_max = maxVel

    def __str__(self):
        # Devuelve la representación en cadena del objeto Bicicleta
        return f"Velocidad Actual: {self.velocidad}, Velocidad Máxima: {self.Vel_max}"
