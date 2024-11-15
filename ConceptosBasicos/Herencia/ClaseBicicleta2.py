# Clase genérica Bicicleta
class Bicicleta:
    color = ""
    tamanio = ""
    Vel_max = 15

    def __init__(self):
        self.velocidad = 0

    def subir_velocidad(self):
        self.velocidad += 1

    def bajar_velocidad(self):
        self.velocidad -= 1

    def cambiar_vel_max(self, max_vel):
        self.Vel_max = max_vel


# Clase derivada BicicletaCarreras que hereda de Bicicleta
class BicicletaCarreras(Bicicleta):
    marcha = 0

    def subir_marcha(self):
        self.marcha += 1

    def bajar_marcha(self):
        self.marcha -= 1
