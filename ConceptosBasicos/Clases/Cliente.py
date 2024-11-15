# Importamos la clase Dni desde el archivo ClaseDni.py
from ClaseDNI import Dni

# Creamos una instancia de la clase Dni
midni = Dni()

# Solicitamos al usuario que introduzca el número de DNI
try:
    num = int(input("Introduzca el número de DNI (sin letra): "))
    # Calculamos la letra del DNI
    result = midni.calcularLetra(num)
    # Mostramos el resultado
    print("Letra del DNI:", result)
except ValueError:
    print("Error: Solo se permiten números.")
