# NO MODIFICAR ESTE ARCHIVO

from estrellas import Estrella


def cargar_estrellas(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf-8") as archivo:
        next(archivo)
        texto = archivo.readlines()

    diccionario_estrellas = {}
    for linea in texto:
        nombre, alias, magnitud, distancia, temperatura, radio, luminosidad = linea.split(',')
        estrella = Estrella(
            nombre, alias, magnitud, float(distancia), float(temperatura),
            float(radio), float(luminosidad)
        )
        diccionario_estrellas[estrella.nombre] = estrella

    return diccionario_estrellas


def cargar_nombres_estrellas_cercanas(nombre_archivo):
    with open(nombre_archivo, 'rt') as archivo:
        nombres = archivo.readlines()

    return [nombre.strip() for nombre in nombres]
