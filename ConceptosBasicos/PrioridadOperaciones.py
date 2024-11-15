
# 4. PRIORIDAD EN LAS OPERACIONES
    # En Python se siguen las normas de prioridad en las operaciones: primero multiplicaciones y divisiones, después sumas y restas.
    # Podemos forzar a realizar operaciones en otro orden haciendo uso de los paréntesis.
    # Realizar una aplicación para comprobar la prioridad en operaciones.

print("--------------PRIORIDAD EN OPERACIONES-------------")

#Primero se realiza la multiplicación
num1=10
num2=20
num3=2
resultado=num1+num2*num3;
print("Resultado:",resultado)

#Podemos forzar con paréntesis para cambiar el orden de la operación

num1=10
num2=20
num3=2
resultado=(num1+num2)*num3;
print("Resultado:",resultado)
