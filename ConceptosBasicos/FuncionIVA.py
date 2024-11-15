
# 12. FUNCIONES EN PYTHON
    # En Python podemos crear funciones utilizando la palabra reservada “def” seguido del nombre la función.
    # Las funciones se pueden crear en cualquier son de un programa.
    #
    # Imaginemos que en muchos bloques de código necesitamos añadir IVA a los precios de nuestros prgoductos.
    # Lo ideal sería crear una función par no repetir ese código en varios puntos.
    #
    # En el siguiente ejemplo crearemos una función donde pediremos el precio de un producto y añadiremos el 21% de Iva al precio introducido.

#
def calcularIVA():
    importe = int(input("Precio del producto: "))
    total = importe* 1.21
    print (f"IVA incluido (21%): {total}")
    return

print("LLAMANDO A LA FUNCIÓN")
calcularIVA()


# 2 Funciones con parámetros
def calcularIVA(importe):
    print (f"Precio del producto: {importe}")
    total = importe* 1.21
    print (f"IVA incluido (21%): {total}")
    return

print("LLAMANDO A LA FUNCIÓN")
calcularIVA(600)


# 3 Funciones que retorna valor
def calcularIVA(importe):
    print (f"Precio del producto: {importe}")
    total = importe* 1.21
    return total

print("LLAMANDO A LA FUNCIÓN")
result=calcularIVA(1000)
print(f"IVA incluido (21%): {result}")


# Retornar más de un valor separado por coma,
def calcularIVA(importe):
    total = importe* 1.21
    return importe,total


print("LLAMANDO A LA FUNCIÓN")
precio,result=calcularIVA(2000)

print(f"Precio del producto: {precio}")
print(f"IVA incluido (21%): {result}")

