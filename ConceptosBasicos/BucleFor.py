
# 10. BUCLE FOR
    # Este bucle permite establecer la inicialización de la variable que controla el bucle y
    # el elemento sobre el que vamos a iterar,en la propia definición del for.


print("--------------BUCLE FOR-------------")
for i in [0, 1, 2, 3, 4]:
    print(f"El valor de i es :{i}")


print("--------------BUCLE FOR-------------")
listaNumeros = [0, 1, 2, 3, 4]

for i in listaNumeros:
    print(f"El valor de i es :{i}")



# Podemos controlar el número de veces que se realiza el bucle utilizando Range().
# En el ejemplo utilizamos el tipo Range para indicar que realizaremos el bucle 10 veces.

print("--------------BUCLE FOR CON SECUENCIA-------------")

# Podemos incluir range para incluir una secuencia

for i in range(10):
    print(f"El valor de i es :{i}")

# Bucle for con cadenas
print("--------------BUCLE FOR CON CADENAS-------------")
Nombres = ['Benito', 'Floro', 'Rosa', 'Luisa']

for valor in Nombres:
    print(valor)

# Bucle for con cadenas y Range
print("--------------BUCLE FOR CON CADENA Y RANGO-------------")

for valor in range(len(Nombres)):
    print ("Nombre:", Nombres[valor], "posicion:", valor)




# Con Range() se puede indicar el inicio y fin del valor de la variable con la que itera el bucle
print("--------------BUCLE FOR CON SECUENCIA-------------")
for i in range(1,11):
    print(f"El valor de i es :{i}")