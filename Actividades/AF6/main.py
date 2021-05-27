import random
from cargar import cargar_mascotas
from iterable import IterableDescuentos
from parametros import RUTA_ANIMALES, TAMANOS
from consultas import precio_total, agrupar_por_tamano, comida_ideal, \
                          obtener_comidas, precio_comidas


def obtener_raza_y_especie():
    # Obtiene una raza y especie aleatoria a partir de los animales
    mascotas = cargar_mascotas(RUTA_ANIMALES)
    razas_especies = set([(mascota.raza, mascota.especie) for mascota in mascotas])
    return random.sample(razas_especies, 1)[0]


if __name__ == "__main__":
    raza, especie = obtener_raza_y_especie()

    print(f'\n*** REALIZANDO CONSULTAS PARA {especie.upper()} {raza.upper()} ***\n')

    print(f'\n*** PRECIO TOTAL DE LA ESPECIE ***\n', f'${precio_total(especie)}')

    print(f'\n*** MASCOTAS POR TAMAÑO ***')
    mascotas_por_tamano = agrupar_por_tamano(TAMANOS)
    print(f'\nMascotas pequeñas:')
    for mascota in mascotas_por_tamano[0]:
        print(mascota.nombre)
    print(f'\nMascotas medianas:')
    for mascota in mascotas_por_tamano[1]:
        print(mascota.nombre)
    print(f'\nMascotas grandes:')
    for mascota in mascotas_por_tamano[2]:
        print(mascota.nombre)


    print(f'\n*** COMIDAS IDEALES DISPONIBLES ***\n')
    for comida in list(comida_ideal(raza, especie)):
        print(comida.nombre)

    print(
        f'\n*** PRECIO COMIDAS IDEALES ***\n',
        f'Precio total: ${precio_comidas(raza, especie)}'
    )

    print(f'\n*** COMIDAS EN LA TIENDA ***\n', obtener_comidas())

    # Iterable e Iterador de descuentos
    print('\n---------- DESCUENTOS ----------\n')
    mascotas = list(cargar_mascotas(RUTA_ANIMALES))
    descuentos = IterableDescuentos(mascotas)
    for masc in descuentos:
        print((
            f"La mascota {masc.nombre} tiene un {masc.descuento_por_edad}% de descuento"
            f" y su preció por apadrinar quedó en ${masc.precio}"
        ))