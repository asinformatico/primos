################################################################################################
# Programa que comprueba si el número introducido es primo.
# Actualmente comprueba cualquier número entre 0 y 1.000.000.000
# Este es el valor máximo del archivo binario usado como tabla de verificación 'numeros.bin'.
# El resultado es instantáneo.
#
# by @as_informatico
# 18-10-2023
################################################################################################

import time

def leer_bit_en_posicion(archivo, posicion):
    byte_posicion = posicion // 8
    bit_posicion = posicion % 8

    with open(archivo, 'rb') as file:
        file.seek(byte_posicion)
        byte = file.read(1)

    if not byte:
        print(f"Error: No se puede leer más allá de la posición {posicion} en el archivo.")
        return None

    bit_valor = (byte[0] >> bit_posicion) & 1
    return bit_valor

archivo = 'numeros.bin'

while True:
    try:
        posicion_a_comprobar = int(input(">>>> >>> Ingrese la posición (comenzando desde 0): "))
        tiempo_inicio = time.time()
        bit_valor = leer_bit_en_posicion(archivo, posicion_a_comprobar)
        if bit_valor == 1:
            es_primo = "ES PRIMO"
        else:
            es_primo = "no es primo"

        if bit_valor is not None:
            print(f"El valor del bit en la posición {posicion_a_comprobar} es {bit_valor} por lo que el número {posicion_a_comprobar} {es_primo}")

        tiempo_transcurrido = time.time() - tiempo_inicio
        print(f'Tiempo transcurrido: {tiempo_transcurrido:.6f} segundos.\n')
    except ValueError:
        print("Finalizando el programa por petición del usuario")
        break
