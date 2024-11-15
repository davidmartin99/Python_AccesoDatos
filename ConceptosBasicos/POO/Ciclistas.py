
# Importamos la clase Bicicleta desde el archivo ClaseBicicleta.py
from ClaseBicicleta import Bicicleta

# Creamos una instancia de la clase Bicicleta
mibici = Bicicleta()

# Mostramos la velocidad inicial de la bicicleta
print("Velocidad inicial:", mibici.velocidad)

# Llamamos al método para aumentar la velocidad dos veces
mibici.subirmarcha()
mibici.subirmarcha()
print("Velocidad después de subir dos veces:", mibici.velocidad)

# Disminuimos la velocidad una vez
mibici.bajarmarcha()
print("Velocidad después de bajar una vez:", mibici.velocidad)

# Cambiamos la velocidad máxima a 25
mibici.cambiarVelMax(25)
print("Nueva velocidad máxima:", mibici.Vel_max)

# Imprimimos la representación del objeto usando __str__
print("Información de la bicicleta:", mibici)
