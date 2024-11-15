# 7. CALCULAR LETRA DNI
    # Realizar una aplicación para conocer la letra del Documento Nacional de Identidad a través del número de DNI.
    # Debe asegurarse de que en la caja DNI sólo se puedan introducir números y que no esté vacía.
    # La fórmula para calcular la letra del número del DNI se halla de la siguiente manera:
    # Se calcula el valor de la siguiente resta ( nº DNI - (Ent(nº DNI / 23) * 23)), tal que Ent es la función parte entera de un número.

print("--------------CALCULAR LETRA DNI CON IF-------------")

dni=int(input("Introduzca DNI:"))

resultado=dni%23

if resultado == 0:
    print("T")
elif resultado==1:
    print("R")
elif resultado==2:
    print("W")
elif resultado==3:
    print("A")
elif resultado==4:
    print("G")
elif resultado==5:
    print("M")
elif resultado==6:
    print("Y")
elif resultado==7:
    print("F")
elif resultado==8:
    print("P")
elif resultado==9:
    print("D")
elif resultado==10:
    print("X")
elif resultado == 11:
    print("B")
elif resultado == 12:
    print("N")
elif resultado == 13:
    print("J")
elif resultado == 14:
    print("Z")
elif resultado == 15:
    print("S")
elif resultado == 16:
    print("Q")
elif resultado == 17:
    print("V")
elif resultado == 18:
    print("H")
elif resultado == 19:
    print("L")
elif resultado == 20:
    print("C")
elif resultado == 21:
    print("K")
elif resultado == 22:
    print("E")
elif resultado == 23:
    print("T")
else:
    print("SIN LETRA")

print("--------------CALCULAR LETRA DNI CON IF-------------")
dni=int(input("Introduzca DNI:"))
resultado=dni%23
letrasDni="TRWAGMYFPDXBNJZSQVHLCKET";

letra=letrasDni[resultado]

"""Podemos utilizar el SubString de otros lenguajes de programación
EJEMPLOS:

s = 'Hello, everybody!'
>>> s[0]
'H'
>>> s[:3]
'Hel'
>>> s[2:5]
'llo'

"""

print (letra)