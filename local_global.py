#Local: Existe solo dentro de la función
def numeros(n1,n2):
    if n1 > n2:
        print("n1 es mayor que n2")
    elif n1 == n2:
        print("Son iguales.")
    else:
        print("n2 es mayor que n1")

respuesta = numeros(4,7)
print(respuesta)

#Global: Puede usarse en todo el archivo .py
pi = 3.1416
def area_circulo(a):
    area = pi * (a**2)
    return area

resultado = area_circulo(5)
print(resultado)