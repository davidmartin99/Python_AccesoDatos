# Clase Dni
# Incluye una propiedad para almacenar la letra y un método para calcular la letra del DNI

class Dni:
    letra = ""

    def calcularLetra(self, numero):
        # Calculamos el índice usando el módulo 23
        resultado = numero % 23

        # Diccionario para asignar letras según el resultado
        letras_dni = {
            0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y",
            7: "F", 8: "P", 9: "D", 10: "X", 11: "B", 12: "N", 13: "J",
            14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H", 19: "L", 20: "C",
            21: "K", 22: "E", 23: "T"
        }

        # Obtenemos la letra correspondiente
        letra = letras_dni.get(resultado, "SIN LETRA")
        return letra
