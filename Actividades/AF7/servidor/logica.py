"""
Este módulo contiene la clase Logica
"""
import json
from threading import Lock
from base64 import b64encode
from datetime import datetime
from random import choice
from usuario import cargar_usuarios, leer_likes, leer_mensajes


class Logica:
    """
    Clase Logica: Funciona como "backend" del servidor. Posee métodos y atributos que describen
    y ejecutan la lógica del programa.

    Atributos:
        log_activado: bool, indica si se deben mostrar los logs en la consola
        usuarios_activos: diccionario de la forma { id : nombre_usuario }, donde el id corresponde
            al identificador de un cliente conectado, y nombre_usuario al usuario con el cual está
            logeado ese cliente
        diccionario_usuarios: diccionario de la forma { nombre_usuario : instancia_usuario }, que
            contiene y mantiene la información cargada de la base de datos.
    """

    # Evita que dos usuarios entren con el mismo nombre al mismo tiempo.
    ingreso_lock = Lock()
    # Administra el acceso a usuarios_activos para evitar que se produzcan errores.
    usuarios_activos_lock = Lock()

    def __init__(self, log_activado=True):
        self.log_activado = log_activado

        # Crear diccionario de usuarios activos de la forma { id : nombre_usuario }
        self.usuarios_activos = dict()

        # Cargar diccionario de usuarios y likes
        self.diccionario_usuarios = cargar_usuarios("./db/usuarios.json")
        leer_likes("./db/likes.csv", self.diccionario_usuarios)
        leer_mensajes("./db/mensajes.csv", self.diccionario_usuarios)

    def validar_nombre_usuario(self, nombre_usuario):
        """
        Recibe un nombre de usuario, y revisa si este ya está activo (conectado) o no.
        """
        with self.usuarios_activos_lock:
            # Revisar nombre en los usuarios activos
            if nombre_usuario in self.usuarios_activos.values():
                return False, "Este usuario está siendo usado por otro cliente"
            # Revisar nombre en los usuarios registrados
            if nombre_usuario not in self.diccionario_usuarios:
                return False, "Este usuario no está registrado en la base de datos"

            return True, None

    def desconectar_usuario(self, id_cliente):
        """
        Recibe una id de un cliente desde el servidor y la saca junto a su usuario asociado
        de el diccionario de usuarios activos.
        """
        with self.usuarios_activos_lock:
            try:
                del self.usuarios_activos[id_cliente]
                self.log(f"Se ha eliminado al cliente {id_cliente} de la lista de usuarios activos")
            except KeyError:
                self.log(f"El cliente {id_cliente} no figura como usuario activo")

    @staticmethod
    def obtener_bytes_imagen(ruta):
        """
        Recibe un ruta de una imagen, y codifica sus bytes a un string utf-8
        """
        with open(ruta, "rb") as archivo_imagen:
            imagen_bytes = archivo_imagen.read()
            imagen_codificada = b64encode(imagen_bytes).decode(encoding='ASCII')
        return imagen_codificada

    def elegir_posible_match(self, usuario):
        """
        Recibe una instancia de usuario, y retorna otro posible usuario para mostrárselo.
        Este posible usuario debe cumplir las siguientes condiciones:
         - No ser el usuario original
         - No estar en la lista de likes
        """
        usuarios_con_like = set(usuario.lista_likes) | {usuario.nombre}
        posibles_usuarios = set(self.diccionario_usuarios.keys())
        lista_posibles_usuarios = list(posibles_usuarios - usuarios_con_like)
        return choice(lista_posibles_usuarios)

    def manejar_mensaje(self, mensaje, id_cliente):
        """
        Maneja un mensaje recibido desde el cliente.
        """
        try:
            comando = mensaje["comando"]
        except KeyError:
            self.log(f"ERROR: mensaje de cliente {id_cliente} no cumple el formato.")
            return dict()
        respuesta = dict()
        destinatarios = [id_cliente]
        if comando == "ingreso":
            nombre_usuario = mensaje["nombre_usuario"]
            with self.ingreso_lock:
                resultado, comentario = self.validar_nombre_usuario(nombre_usuario)
                if resultado:
                    with self.usuarios_activos_lock:
                        self.usuarios_activos[id_cliente] = nombre_usuario
                    respuesta = {
                        "comando": "ingreso_aceptado",
                        "nombre_usuario": nombre_usuario,
                    }
                else:
                    respuesta = {
                        "comando": "ingreso_rechazado",
                        "comentario": comentario,
                    }
        elif comando == "salida":
            self.desconectar_usuario(id_cliente)
        elif comando == "obtener_datos_usuario":
            usuario = self.diccionario_usuarios.get(self.usuarios_activos[id_cliente])
            if usuario:
                imagen_bytes = self.obtener_bytes_imagen(usuario.ruta_imagen)
                respuesta = {
                    "comando": "datos_perfil_usuario",
                    "nombre_usuario": usuario.nombre,
                    "edad": usuario.edad,
                    "bio": usuario.bio,
                    "imagen_bytes": imagen_bytes,
                }
        elif comando == "actualizar_bio":
            usuario = self.diccionario_usuarios.get(self.usuarios_activos[id_cliente])
            if usuario:
                usuario.bio = mensaje["bio"]
        elif comando == "obtener_matches_usuario":
            usuario = self.diccionario_usuarios.get(self.usuarios_activos[id_cliente])
            if usuario:
                lista_matches = []
                for liked in usuario.lista_likes:
                    liked_user = self.diccionario_usuarios.get(liked)
                    if liked_user and (usuario.nombre in liked_user.lista_likes):
                        lista_matches.append(liked_user.nombre)
                respuesta = {
                    "comando": "datos_matches_usuario",
                    "nombre_usuario": usuario.nombre,
                    "matches": lista_matches,
                }
        elif comando == "obtener_perfil_aleatorio":
            usuario = self.diccionario_usuarios.get(self.usuarios_activos[id_cliente])
            if usuario:
                posible_match_nombre = self.elegir_posible_match(usuario)
                if posible_match_nombre:
                    posible_match = self.diccionario_usuarios.get(posible_match_nombre)
                    imagen_bytes = self.obtener_bytes_imagen(posible_match.ruta_imagen)
                    respuesta = {
                        "comando": "datos_perfil_aleatorio",
                        "nombre_usuario": posible_match.nombre,
                        "edad": posible_match.edad,
                        "bio": posible_match.bio,
                        "imagen_bytes": imagen_bytes,
                    }
                else:
                    respuesta = {
                        "comando": "datos_perfil_aleatorio",
                        "nombre_usuario": "",
                    }
        elif comando == "dar_like_usuario":
            usuario = self.diccionario_usuarios.get(self.usuarios_activos[id_cliente])
            if usuario:
                usuario.lista_likes.append(mensaje["nombre_usuario_like"])
        elif comando == "obtener_mensajes":
            usuario = self.diccionario_usuarios.get(self.usuarios_activos[id_cliente])
            destinatario = self.diccionario_usuarios.get(mensaje["destinatario"])
            if usuario and destinatario:
                mensajes = usuario.mensajes[destinatario.nombre] + \
                    destinatario.mensajes[usuario.nombre]
                respuesta = {
                    "comando": "datos_mensajes",
                    "mensajes": mensajes
                }
        elif comando == "enviar_mensaje_chat":
            usuario = self.diccionario_usuarios.get(self.usuarios_activos[id_cliente])
            destinatario = self.diccionario_usuarios.get(mensaje["destinatario"])
            if usuario and destinatario:
                respuesta = {
                    "comando": "recibir_mensaje_chat",
                    "emisor": str(usuario.nombre),
                    "receptor": str(usuario.nombre),
                    "texto": ">" + str(usuario.nombre) + ": " + mensaje["texto"]
                }
                tup = (usuario.nombre, str(datetime.now()), mensaje["texto"])
                usuario.mensajes[destinatario.nombre].append(tup)
                if destinatario.nombre in self.usuarios_activos.values():
                    idx_destinatario = list(self.usuarios_activos.values()
                                            ).index(destinatario.nombre)
                    id_destinatario = list(self.usuarios_activos.keys())[idx_destinatario]
                    destinatarios = [id_cliente, id_destinatario]
        else:
            self.log(f"Error: comando {comando} inválido")
        return respuesta, destinatarios

    def guardar_variables(self):
        """
        Pasa los contenidos de las variables almacenadas en RAM al disco (archivos de texto en el
        directorio db/)
        """
        # usuarios.json (guardar bio)
        with open("db/usuarios.json", "w", encoding='utf-8') as archivo:
            dict_usuarios = dict()
            for key in self.diccionario_usuarios:
                usuario = self.diccionario_usuarios[key]
                dict_usuarios[key] = {
                    "bio": usuario.bio,
                    "edad": usuario.edad,
                    "nombre": usuario.nombre,
                    "ruta_imagen": usuario.ruta_imagen,
                }
            json.dump(dict_usuarios, archivo, indent=4, sort_keys=True)
            del dict_usuarios
        # likes.csv
        with open("db/likes.csv", "w", encoding='utf-8') as archivo:
            archivo.write("usuario_da,usuario_recibe\n")
            for key in self.diccionario_usuarios:
                usuario = self.diccionario_usuarios[key]
                for liked_user in usuario.lista_likes:
                    archivo.write(f"{usuario.nombre},{liked_user}\n")
        # mensajes.csv
        with open("db/mensajes.csv", "w", encoding='utf-8') as archivo:
            archivo.write("usuario_envia,usuario_recibe,fecha,mensaje\n")
            for key in self.diccionario_usuarios:
                usuario = self.diccionario_usuarios[key]
                for destinatario_user in usuario.mensajes:
                    for tup_mensaje in usuario.mensajes[destinatario_user]:
                        out = f"{tup_mensaje[0]},{destinatario_user},{tup_mensaje[1]},{tup_mensaje[2]}\n"
                        archivo.write(out)

    def log(self, mensaje_consola):
        """Imprime un mensaje a la consola, sólo si la funcionalidad está activada.

        Argumentos:
            mensaje_consola (str): mensaje a imprimir.
        """
        if self.log_activado:
            print(mensaje_consola)
