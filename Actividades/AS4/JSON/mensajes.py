"""
Este módulo contiene la clase mensaje, y funciones que permiten trabajar con
el archivo JSON que contiene sus datos.
"""
import json
from datetime import datetime
from collections import defaultdict

FECHA_ACTUAL = datetime(2021, 6, 17, 17, 0, 0)


class Mensaje:
    """
    Esta clase describe un mensaje y almacena sus atributos
    """

    grupos = defaultdict(list)

    def __init__(self, mensaje, usuario, fecha, grupo):
        if not isinstance(fecha, datetime):
            raise TypeError("La fecha tiene el tipo incorrecto")
        self.mensaje = mensaje
        self.usuario = usuario
        self.fecha = fecha
        self.grupo = grupo
        self.sospechoso = False

    @classmethod
    def ordenar_mensajes(cls):
        """
        Ordena los mensajes en la variable de clase 'grupos'
        """
        try:
            for grupo in cls.grupos:
                cls.grupos[grupo].sort(key=lambda x: x.fecha)
        except AttributeError as err:
            print(err)

    def __repr__(self):
        return f"[{self.fecha}] {self.usuario}: {self.mensaje}"


def string_a_fecha(string_):
    """
    Argumentos:
        string_ (str): contiene una fecha en formato string

    Returns:
        datetime.datetime: fecha parseada
    """
    return datetime.strptime(string_, "%d/%m/%Y %H:%M:%S")


def decodificar_mensaje(dict_):
    """
    Crea una instancia de Mensaje según la información que se encuentre en dict_

    Argumentos:
        dict_ (dict): Diccionario conteniendo la información de un mensaje.

    Retorna:
        Mensaje: instancia construída a partir de la información del diccionario
    """
    # COMPLETAR


def cargar_mensajes(path):
    """
    Carga el archivo JSON en path, y lo decodifica de manera personalizada.

    Argumentos:
        path (str): Path del archivo a decodificar (encoded.json)

    Retorna:
        list[Mensaje]: Resultado de cargar y decodificar el archivo JSON con la
            decodificación personalizada. Contiene las instancias de los
            mensajes
    """
    # COMPLETAR


if __name__ == "__main__":
    cargar_mensajes("mensajes.json")
    Mensaje.ordenar_mensajes()
    for grupo in Mensaje.grupos:
        print("-------------", grupo, "-------------")
        for mensaje in Mensaje.grupos[grupo]:
            print(mensaje)
