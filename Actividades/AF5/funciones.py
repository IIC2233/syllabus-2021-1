## Funciones varias
import parametros as p
from time import sleep


def encontrar_preferencia(ingrediente):
    with open(p.ARCHIVO_PREFERENCIAS, "r", encoding='utf-8') as archivo:
        preferencias = archivo.readlines()
    dict_preferencias = {ing: reemplazo for ing, reemplazo in
                         map(lambda x: x.strip().split(','), preferencias)}

    return dict_preferencias.setdefault(ingrediente, 'Agua')


def desencriptar(palabra):
    claves = {n: letra for n, letra in enumerate(p.PALABRA_ENCRIPTACION)}
    nueva_palabra = ""
    for letra in palabra:
        if letra.isdigit() and int(letra) in claves:
            nueva_palabra += claves[int(letra)]
        else:
            nueva_palabra += letra
    return nueva_palabra


def encriptar(palabra):
    claves = {letra: n for n, letra in enumerate(p.PALABRA_ENCRIPTACION)}
    nueva_palabra = ""
    for letra in palabra:
        if letra in claves:
            nueva_palabra += str(claves[letra])
        else:
            nueva_palabra += letra
    return nueva_palabra


def log(anuncio, tipo_anuncio='general'):
    """
    Función que imprime información de acuerdo a un formato específico
    Usado para los diversos pasos de la DCCocina
    :param anuncio: string que se imprimirá
    :param tipo_anuncio: string que define el formato en que se imprimirá el anuncio
    :return: None
    """
    if tipo_anuncio == 'general':
        print(f'-----{anuncio: ^90s}-----')
    elif tipo_anuncio == 'relleno':
        print(f'     {anuncio:-^90s}     ')
    elif tipo_anuncio == 'ingrediente':
        print(f'     {anuncio: ^90s}     ')
    else:
        print(f'|    {anuncio: ^90s}    |')
    sleep(p.LOG_SLEEP_S)


def recibir_input(lista_opciones):
    """
    Recibe input del usuario y lo asigna al valor apropiado
    :return: str que representa la receta seleccionada del usuario.
    """
    respuesta = ""
    while not respuesta:
        try:
            respuesta = input("Ingresa tu respuesta:  ")
            return lista_opciones[int(respuesta)]
        except ValueError:
            print("Error: Porfavor ingresa un número.")
        except IndexError:
            print("Error: Porfavor ingresa un número dentro de las opciones")


def preguntar_rellenos():
    print("¡Bienvenidx a DCCocina!\n¿Que relleno te gustaría utilizar esta vez?")
    for nro, opcion in enumerate(p.STRINGS_RELLENO):
        print(f"{'[' + str(nro) + ']:': >4s} {opcion.title(): <20s}")

    nombre_relleno = ""
    while not nombre_relleno:
        try:
            nombre_relleno = recibir_input(p.STRINGS_RELLENO)
        except ValueError:
            print("Error: Porfavor ingresa un número.")
        except IndexError:
            print("Error: Porfavor ingresa un número dentro de las opciones")

    print(f'Se ha escogido usar {nombre_relleno} como relleno')
    return nombre_relleno
