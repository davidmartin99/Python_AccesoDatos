
# 8. BUCLE WHILE
    # Ejecuta repetidamente un conjunto de sentencias mientras una expresión booleana sea verdadera.
    # Vamos a crear un bucle que se ejecute mientras la condición sea verdadera.
    # Declaramos i con valor inicial en uno, indicar que permanezca el bucle mientras i sea menor de diez.
    # Es importante aumentar el valor de i dentro del bucle o de lo contrario crearemos un bucle infinito.

print("--------------BUCLE WHILE-------------")
i = 1
while i <= 10:
    print(f"El valor de i es :{i}")
    i += 1

# Bucle con break
print("--------------BUCLE WHILE-------------")
i = 1
while i <= 10:
    print(f"El valor de i es :{i}")
    i += 1
    if i == 3:
        break

# Bucle con continue
print("--------------BUCLE WHILE-------------")
i = 1
while i <= 10:
    i += 1
    if i == 3:
        continue
    print(f"El valor de i es :{i}")
