# NO MODIFICAR ESTE ARCHIVO

from cargar_datos import cargar_estrellas, cargar_nombres_estrellas_cercanas
from verificar_estrellas import (
    corregir_alias_estrella,
    corregir_magnitud_estrella,
    corregir_distancia_estrella,
    dar_alerta_estrella_cercana
)
from calcular_ruta import generar_ruta_estrellas


if __name__ == "__main__":

    diccionario_estrellas = cargar_estrellas("estrellas.csv")
    nombres_estrellas = cargar_nombres_estrellas_cercanas("estrellas_cercanas.txt")

    print("Revisando posibles errores en las estrellas...\n")
    for estrella in diccionario_estrellas.values():
        corregir_alias_estrella(estrella)
        corregir_distancia_estrella(estrella)
        corregir_magnitud_estrella(estrella)

    print("Revisando estrellas inexistentes...\n")
    for nombre_estrella in nombres_estrellas:
        dar_alerta_estrella_cercana(nombre_estrella, diccionario_estrellas)

    print("Generando ruta de estrellas...\n")
    ruta_de_estrellas = generar_ruta_estrellas(diccionario_estrellas.values())


    print(58*u'\xb7')
    print('¡Enhorabuena! ¡Te has salvado de las estrellas peligrosas!\n')
    print(u'\u2554' + 5*u'\u2550' + ' RUTA DE ESTRELLAS ' + 5*u'\u2550' + u'\u2557')
    for estrella in ruta_de_estrellas:
        dif = 29 - len(estrella)
        if dif % 2 == 0:
            espacio1 = int(dif/2)
            espacio2 = int(dif/2)
        else:
            espacio1 = dif//2
            espacio2 = (dif//2) + 1
        print(u'\u2551' + espacio1*' ' + estrella + espacio2*' ' + u'\u2551')
    print(u'\u255a' + 29*u'\u2550' + u'\u255d')
    print('\nBUEN VIAJE AMIGUE ESPACIAL' + u'\x03')
