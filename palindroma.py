##Escribe un programa en Python que determine si una cadena de texto es un palíndromo o no. Un palíndromo es una palabra, 
##frase o secuencia de caracteres 
##que se lee igual de izquierda a derecha y de derecha a izquierda, 
##ignorando espacios, signos de puntuación y mayúsculas/minúsculas.
print("Bienvenido al programa que determina si una palabra es palindroma o no.")
texto = input("Ingrese una palabra: ")
contador = 0
palindromo = texto
for i in range(palindromo):
    if palindromo[i] == palindromo[i][i-1]:
        palindromo[i][i-1-contador]
        contador+=1
if palindromo == texto:
    print("Las palabra es palindroma.")
else:
    print("La palabra no es palindroma.")