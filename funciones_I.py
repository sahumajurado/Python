#Función básica
def nombre():
    print("Hola, soy una función")

nombre()

#Función con parámetros
def suma(a,b):
    suma = a + b
    return suma

def resta(m,n):
    resta = m -n
    return resta

def multiplicacion(x,y):
    multi = x * y
    return multi

##Forma01
print(suma(4,6))
##Forma02
resultado = suma(5,7)
print(resultado)

res1 = multiplicacion(2,6)
print(res1)

def funcion_parametros(a):
    print(a)

funcion_parametros("Holaaa")

#Función sin parámetros
def sumando():
    a = int(input("Ingrese un valor: "))
    b = int(input("Ingrese otro valor: "))
    suma = a + b
    print(suma)

sumando()

#Función de retorno varios valores
def calculadora(x,y):
    suma = x + y 
    resta = x - y
    multiplicacion = x * y
    division = x / y
    potencia = x ** y
    return suma, resta, multiplicacion, division, potencia

a, b, c , d, e = calculadora(4,6)
print(a,b,c,d,e)

#Función con parámetros por defecto
def area_circulo(a, pi = 3.1416):
    area = pi * (a**2)
    return area

print(area_circulo(3))