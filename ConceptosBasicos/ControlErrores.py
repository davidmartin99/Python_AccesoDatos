
# 13. CONTROL DE ERRORES (EXCEPCIONES)
    # Python implementa excepciones con el propósito de conseguir código robusto.
    # Cuando ocurre un error en un programa, el código que encuentra el error lanza una excepción
    # que se puede capturar desde la aplicación con el propósito de recuperarse de ella.

# Salta error
print("----- Introducir número -----")
def controlErrores():
    try:
        numero = int(input("Introduce número:"))
        print("Número:",numero)
    except ValueError:
        print ("Error, debes introducir un número")

controlErrores()


# Pide un numero hasta que sea un numero y sea diferente a 0
print("----- Division -----")
def controlErrores():
    try:
        dividendo = int(input("Introduce dividendo:"))
        divisor = int(input("Introduce divisor:"))
        resultado = dividendo / divisor
        print(f"Resultado división: {resultado}")
    except ValueError:
        print("Error, debes introducir un número")
    except ZeroDivisionError:
        print("¡¡¡Error!!!. El divisor no puede ser cero")

controlErrores()