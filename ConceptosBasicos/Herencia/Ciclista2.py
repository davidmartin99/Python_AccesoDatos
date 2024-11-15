# Importamos la clase BicicletaCarreras desde el archivo ClaseBicicleta.py
from ClaseBicicleta2 import BicicletaCarreras

# Creamos una instancia de la clase BicicletaCarreras
mibici = BicicletaCarreras()

# Mostramos la velocidad inicial
print("Velocidad inicial:", mibici.velocidad)

# Subimos la marcha dos veces y mostramos el valor actual de la marcha
mibici.subir_marcha()
mibici.subir_marcha()
print("Marcha después de subir dos veces:", mibici.marcha)

# Bajamos la marcha y mostramos el valor actual de la marcha
mibici.bajar_marcha()
print("Marcha después de bajar una vez:", mibici.marcha)

# Subimos la velocidad y mostramos el valor actual de la velocidad
mibici.subir_velocidad()
print("Velocidad después de subir una vez:", mibici.velocidad)

# Cambiamos la velocidad máxima y la mostramos
mibici.cambiar_vel_max(25)
print("Velocidad máxima cambiada:", mibici.Vel_max)
