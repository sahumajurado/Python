print("Simulador de una interfaz humano-computadora")
val = input("Ingresar cadena de texto: ")
val = str(val)

# Dividir la cadena de texto en palabras
cadena = val.split()

def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
    return binario

def NPL_Ascii_BIN(mensajeNLP):
    for palabra in mensajeNLP:
        asc = ""
        for d in palabra:
            cad = str(ord(d))
            asc += cad
        asc = int(asc)
        bin = decimal_a_binario(asc)
        TCPU = len(palabra) * 2  # Tiempos de CPU
        CRELOJ = 4 * TCPU  # Ciclos de reloj
        print("UNIDAD DE ANÁLISIS: ", palabra)
        print("ASCII: ", asc)
        print("TIEMPO CPU ", TCPU)
        print("CICLOS RELOJ: ", CRELOJ)
        print("BINARIO: ", bin)
        print("---------------------")

NPL_Ascii_BIN(cadena)

def totales(mensajeNLP):
    Tiempo_cpu_total = 0
    ciclo_reloj_total = 0
    for palabra in mensajeNLP:
        TCPU = len(palabra) * 2  # Tiempos de CPU
        CRELOJ = 4 * TCPU  # Ciclos de reloj
        Tiempo_cpu_total += TCPU
        ciclo_reloj_total += CRELOJ
    print(f"Total Tiempo CPU: {Tiempo_cpu_total}")
    print(f"Total Ciclo de reloj: {ciclo_reloj_total:.2f}")  # Mostrar dos decimales
    return Tiempo_cpu_total, ciclo_reloj_total  # Devolver los valores

# Asegurarse de que cadena no esté vacía antes de llamar a totales
if cadena:
    Tiempo_cpu_total, ciclo_reloj_total = totales(cadena)
else:
    Tiempo_cpu_total, ciclo_reloj_total = 0, 0

def recomendacion_procesador(Tiempo_cpu_total, ciclo_reloj_total):
    #Velocidad del procesador
    v_procesador = ciclo_reloj_total / Tiempo_cpu_total
    #Unidades de medida
    if v_procesador < 1000:
        print(f"La velocidad del procesador es: {v_procesador:.2f} Hz")
        print("Se recomienda un procesador de gama baja.") 
    elif v_procesador >= 1000 and v_procesador < 3000:
        v_procesador /= 1000  # Convertir a kHz
        print(f"La velocidad del procesador es: {v_procesador:.2f} kHz")
        print("Se recomienda un procesador de gama media.")
    else:
        v_procesador /= 1000  # Convertir a kHz
        print(f"La velocidad del procesador es: {v_procesador:.2f} kHz")
        print("Se recomienda un procesador de gama alta")
recomendacion_procesador(Tiempo_cpu_total, ciclo_reloj_total)
