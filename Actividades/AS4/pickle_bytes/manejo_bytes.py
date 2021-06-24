"""
Este módulo contiene funciones para el manejo general de los bytes de las
imágenes

Corresponde a la parte de Bytes
"""


def int_desde_bytes(bytes_):
    """
    Decodifica el valor de un bytearray a un int con codificación little endian

    Argumentos:
        bytes_ (bytearray): Los bytes a decodificar

    Retorna:
        int: valor numérico correspondiente a los bytes
    """
    return int.from_bytes(bytes_, byteorder="little")


def tuplas_desde_bytes(bytes_):
    """
    Recibe un bytearray proveniente de una imagen, que representa la información
    condensada de cada pixel. Se deben separar los pixeles (un pixel son 4 bytes
    en el bytearray) en una lista de tuplas.

    Argumentos:
        bytes_ (bytearray): La información a separar en tuplas.

    Retorna:
        list[tuple[int]]: lista de tuplas separadas
    """
    # COMPLETAR


def bytes_desde_tuplas(tuplas):
    """
    Recibe una lista de tuplas, y las transforma en un bytearray. Realiza la
    función inversa de tuples_from_bytes.

    Argumentos:
        tuplas (list[tuple[int]]): Lista de tuplas a juntar

    Retorna:
        bytearray: bytes resultantes de juntar las información de las tuplas
    """
    # COMPLETAR


def recuperar_contenido(bytes_corrompidos):
    """
    Recibe un bytearray. Debes crear un nuevo bytearray modificado
    según las especificaciones del enunciado y retornarlo

    Argumentos:
        bytes_corrompidos (bytearray): Estructura de bytes que se encuentran corrompidos, a reparar
            según los pasos del enunciado

    Retorna:
        bytearray: bytes reparados según la lógica pedida en el enunciado
    """
    # COMPLETAR


def organizar_bmp(info_bytes):
    """
    Separa la información de la imagen en formato bmp en sus componentes
    principales

    Argumentos:
        info_bytes (bytearray): bytes representando la info de la imagen bmp

    Retorna:
        tuple[bytearray]: contiene el header, DIB Header, los pixeles, y el EOF
    """
    header = info_bytes[:15]
    dib_header = info_bytes[15:125]
    pixel_data = info_bytes[125:-1]
    eof = [info_bytes[-1]]
    return header, dib_header, pixel_data, eof


if __name__ == "__main__":
    print("-"*30, "TESTS", "-"*30)
    print("-" * 20, "TESTS tuplas_desde_bytes y bytes_desde_tuplas", "-"*20)

    input_bytes_tuplas = bytearray("qwertyui", 'ascii')
    print("Bytearray inicial:", input_bytes_tuplas)
    test_tuplas = tuplas_desde_bytes(input_bytes_tuplas)
    print("OUTPUT tuplas_desde_bytes:", test_tuplas)
    test_bytes_out = bytes_desde_tuplas(test_tuplas)
    print("OUTPUT bytes_desde_tuplas:", test_bytes_out)
    if not isinstance(test_tuplas, list) or not isinstance(test_tuplas[0], tuple):
        raise AssertionError("tuplas_desde_bytes entrega un tipo incorrecto!")
    if not isinstance(test_bytes_out, bytearray):
        raise AssertionError("bytes_desde_tuplas entrega un tipo incorrecto!")
    if test_bytes_out != input_bytes_tuplas:
        raise AssertionError("Ups! Hay un error en tuplas_desde_bytes o bytes_desde_tuplas!")
    print("tuplas_desde_bytes y bytes_desde_tuplas parecen ser correctas!")

    print("-" * 20, "TEST recuperar_contenido", "-"*20)

    input_recuperar_contenido = bytearray(b'\x00\x00\x02\x01\x00\x01\x07\x01\x00\x04')
    print("Bytearray inicial:", input_recuperar_contenido)
    output_recuperar_contenido = recuperar_contenido(input_recuperar_contenido)
    print("OUTPUT recuperar_contenido:", output_recuperar_contenido)
    if not isinstance(output_recuperar_contenido, bytearray):
        raise AssertionError("recuperar_contenido entrega un tipo incorrecto!")
    if output_recuperar_contenido != bytearray(b'\x00\x05\x02\x0F\x08'):
        raise AssertionError("Ups! Hay un error en recuperar_contenido!")
    print("recuperar_contenido parece ser correcto!")
