################################################################################################
# Programa que genera un archivo binario con los valores de los bits a 1 si la posición corresponde a un número primo
# y 0 en caso de no serlo.
# Las variables rango_inicio y rango_final determinan la cantidad de números que va a comprender dicha bbdd.
# El archivo resultante 'numeros.bin' es usado como tabla en el script 'comprobar_primo.py'
#
# by @as_informatico
# 18-10-2023
################################################################################################

import time

def criva_de_eratostenes(limite):
    primos = [True] * (limite + 1)
    primos[0] = primos[1] = False
    for i in range(2, int(limite**0.5) + 1):
        if primos[i]:
            for j in range(i*i, limite + 1, i):
                primos[j] = False
    return primos

def generar_archivo_binario(archivo, inicio, final):
    if inicio < 0 or final < inicio:
        print("Error: Rango no válido.")
        return

    limite = max(final, 2)

    primos = criva_de_eratostenes(limite)
    with open(archivo, 'wb') as file:
        byte = 0
        bit_posicion = 0
        for i in range(inicio, min(final + 1, len(primos))):
            es_primo = primos[i]
            if es_primo:
                byte |= (1 << bit_posicion)

            bit_posicion += 1
            if bit_posicion == 8:
                file.write(byte.to_bytes(1, byteorder='big'))
                byte = 0
                bit_posicion = 0

        if bit_posicion > 0:
            file.write(byte.to_bytes(1, byteorder='big'))

rango_inicio = 0
rango_final = 1000000000
archivo = f'numeros.bin'
tiempo_inicio = time.time()
generar_archivo_binario(archivo, rango_inicio, rango_final)
print(f"Archivo {archivo} generado exitosamente.")
tiempo_transcurrido = time.time() - tiempo_inicio
print(f'Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos.\n')
