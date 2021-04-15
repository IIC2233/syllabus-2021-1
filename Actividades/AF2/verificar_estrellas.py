from cargar_datos import cargar_estrellas, cargar_nombres_estrellas_cercanas


def verificar_alias_estrella(estrella):
    pass


def corregir_alias_estrella(estrella):
    pass


def verificar_distancia_estrella(estrella):
    pass


def corregir_distancia_estrella(estrella):
    pass


def verificar_magnitud_estrella(estrella):
    pass


def corregir_magnitud_estrella(estrella):
    pass


def dar_alerta_estrella_cercana(nombre_estrella, diccionario_estrellas):
    pass



if __name__ == "__main__":
    diccionario_estrellas = cargar_estrellas("estrellas.csv")
    nombres_estrellas = cargar_nombres_estrellas_cercanas("estrellas_cercanas.txt")

    # Descomenta las funciones que quieras probar de la actividad
    print("Revisando posibles errores en las estrellas...\n")
    for estrella in diccionario_estrellas.values():
        # corregir_alias_estrella(estrella)
        # corregir_distancia_estrella(estrella)
        # corregir_magnitud_estrella(estrella)
        pass

    print("Revisando estrellas inexistentes...\n")
    for nombre_estrella in nombres_estrellas:
        # dar_alerta_estrella_cercana(nombre_estrella, diccionario_estrellas)
        pass
