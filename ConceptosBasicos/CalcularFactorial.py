
# 9. FACTORIAL DE UN NÚMERO
    # Realizar una aplicación que nos pida por teclado un número y mostremos el factorial de dicho número.
    # El factorial se define como el producto de un número y sus antecesores empezando desde 1. Y se le reconoce por este símbolo: "n!".

print("--------------CALCULAR FACTORIAL DE UN NÚMERO------------")

factorial = 1
numero=int(input("Introduzca un número:"))
dato=numero
while numero != 0:
    factorial = factorial * numero
    numero=numero-1

print(f"El factorial de {dato} es {factorial}")
