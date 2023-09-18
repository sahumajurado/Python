##Crear una función que devuelva el promedio de notas de un alumno
alumno = input("Nombre del alumno: ")
n = int(input("Ingrese la cantidad de notas del alumno: "))
lista = []

for i in range(n):
    nota = float(input(f"Ingrese nota {i+1}: "))
    lista.append(nota)

def prom_alumno(lista):
    """Devuelve el promedio de notas de un alumno"""
    promedio = sum(lista)/len(lista)
    return promedio

print(f"El promedio de notas del alumno {alumno} es: {prom_alumno(lista)}")




