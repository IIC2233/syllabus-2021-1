from collections import namedtuple


def cargar_mafiosos(path_mafiosos):
    # NO MODIFICAR
    # Crea un diccionario cuyas key son los nombres de los mafiosos
    # y su value es una tupla con el nombre de su conocido y su frase
    dic_mafiosos = {}
    nombre_cabeza = None
    with open(path_mafiosos, "r", encoding="UTF-8") as archivo:
        lineas = archivo.readlines()
        for linea in lineas[1:]:
            nombre, frase, nombre_conocido = linea.strip().split(',')
            dic_mafiosos[nombre] = (nombre_conocido, frase)
            if nombre_cabeza is None:
                nombre_cabeza = nombre
            if not nombre_conocido:
                nombre_conocido = None

    return dic_mafiosos, nombre_cabeza


def cargar_lugares(path_lugares, path_conexiones, diccionario_mafiosos):
    # NO MODIFICAR
    # Crea un diccionario que contiene a los lugares y los mafiosos que hay en ellos
    # y una lista con las conexiones entre los lugares
    dict_lugares = {}
    Mafioso = namedtuple("Mafioso", ["nombre", "frase"])
    with open(path_lugares, "r", encoding="UTF-8") as archivo:
        lineas = archivo.readlines()
        for linea in lineas[1:]:
            nombre_lugar, info_mafiosos = linea.strip().split(',')
            mafiosos = [
                Mafioso(
                    nombre=nombre_mafioso,
                    frase=diccionario_mafiosos[nombre_mafioso][1]
                ) for nombre_mafioso in info_mafiosos.split(';')
            ]
            dict_lugares[nombre_lugar] = mafiosos

    conexiones = list()
    with open(path_conexiones, "r", encoding="UTF-8") as archivo:
        lineas = archivo.readlines()
        for linea in lineas[1:]:
            lugar_1, lugar_2, peso = linea.strip().split(',')
            conexiones.append((lugar_1, lugar_2, int(peso)))

    return dict_lugares, conexiones
