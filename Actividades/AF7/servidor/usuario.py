"""
Este módulo contiene la clase Usuario y funciones para cargarlos desde la
base de datos.
"""
import json
from collections import defaultdict


class Usuario:
    """.
    Clase Usuario: Almacena la información relativa a un usuario específico. Se genera/carga desde
        la base de datos.

    Atributos:
        nombre: string.
        edad: int.
        bio: string.
        ruta_imagen: string.
        lista_likes: lista de strings, contiene los nombres de los usuarios a los cuales el
            usuario actual les ha dado like dentro de la aplicación.
        mensajes: defaultdict de la forma { nombre_destinatario : lista de tuplas }, con tuplas de
            la forma (nombre_usuario, fecha, mensaje).
    """

    def __init__(self, nombre, edad, bio, ruta_imagen):
        self.nombre = nombre
        self.edad = edad
        self.bio = bio
        self.ruta_imagen = ruta_imagen
        self.lista_likes = []
        self.mensajes = defaultdict(list)

    def __repr__(self):
        return f"{self.nombre} ({self.edad})"


def cargar_usuarios(ruta):
    """
    Recibe el ruta del archivo de usuarios.
    Retorna una lista con los objetos correspondientes.
    """
    diccionario_usuarios = dict()
    with open(ruta, encoding='utf-8') as archivo:
        for usuario in json.load(archivo).values():
            diccionario_usuarios[usuario['nombre']] = Usuario(**usuario)
    return diccionario_usuarios


def leer_likes(ruta, usuarios):
    """
    Recibe el ruta del archivo de likes, y el diccionario con los objetos de usuarios.
    Carga en cada usuario sus likes correspondientes.
    """
    with open(ruta, encoding='utf-8') as archivo:
        archivo.readline()
        for linea in archivo:
            linea = linea.strip()
            if linea:
                usuario_1, usuario_2 = linea.split(",")
                usuarios[usuario_1].lista_likes.append(usuario_2)


def leer_mensajes(ruta, usuarios):
    """
    Recibe el ruta del archivo de mensajes, y el diccionario con los objetos de usuarios.
    Carga en cada usuario un diccionario con los mensajes que ha enviado a cada usuario, con las
    keys siendo el nombre de usuario del receptor, y el valor la lista con los mensajes.
    """
    with open(ruta, encoding='utf-8') as archivo:
        archivo.readline()
        for linea in archivo:
            linea = linea.strip()
            if linea:
                usuario_1, usuario_2, fecha, mensaje = linea.split(",", 3)
                usuarios[usuario_1].mensajes[usuario_2].append((usuario_1, fecha, mensaje))
