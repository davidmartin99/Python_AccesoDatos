
# 11. VALIDACIÓN ISBN
    # Realizar una aplicación para comprobar si el ISBN introducido por teclado es válido.
    # Debemos comprobar que el número introducido tiene 10 caracteres.

import sys

print("--------------VALIDANDO ISBN-------------")

numero=input("Introduzca número ISBN:")
if len(numero)!=10:
    print ("Debe introducir un ISBN de 10 dígitos")
    sys.exit()

resultado = 0;0
for i in range(0,10):
    resultado =resultado  + (int(numero[i]) * (i + 1))

if resultado % 11 == 0:
    print("CORRECTO")
else:
    print("INCORRECTO")
