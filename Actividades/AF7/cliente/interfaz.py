"""
Este módulo contiene la clase Controlador
"""
from datetime import datetime
from PyQt5.QtCore import pyqtSignal, QObject
from ventanas.ventana_inicio import VentanaInicio
from ventanas.ventana_principal import VentanaPrincipal
from ventanas.ventana_perfil import VentanaPerfil
from ventanas.ventana_matches import VentanaMatches
from ventanas.ventana_perfiles import VentanaPerfiles


class Controlador(QObject):
    """
    Clase Controlador: Liga el cliente con la interfaz gráfica. Interpreta los mensajes recibidos
    desde el servidor (manejar_mensaje), aplica los cambios correspondientes en la interfaz, y
    genera la respuesta correspondiente al servidor.
    """

    mostrar_ventana_principal_signal = pyqtSignal()
    enviar_signal = pyqtSignal(dict)

    def __init__(self, parent):
        super().__init__()

        self.ventana_inicio = VentanaInicio()
        self.ventana_principal = VentanaPrincipal()
        self.ventana_perfil = VentanaPerfil()
        self.ventana_matches = VentanaMatches()
        self.ventana_perfiles = VentanaPerfiles()

        self.nombre_usuario = None

        self.log = parent.log

        # Conectar señales
        # - General
        self.enviar_signal.connect(parent.enviar)
        # - Ventana inicio
        self.ventana_inicio.enviar_nombre_usuario_signal.connect(parent.enviar)
        # - Ventana principal
        self.mostrar_ventana_principal_signal.connect(self.mostrar_principal)
        self.ventana_principal.volver_signal.connect(
            lambda dict_: (parent.enviar(dict_), self.mostrar_login())
        )
        self.ventana_principal.abrir_perfil_signal.connect(self.mostrar_perfil)
        self.ventana_principal.abrir_matches_signal.connect(self.mostrar_matches)
        self.ventana_principal.ver_perfiles_signal.connect(self.mostrar_perfiles)
        # - Ventana perfil
        self.ventana_perfil.volver_signal.connect(self.mostrar_principal)
        self.ventana_perfil.actualizar_bio_signal.connect(parent.enviar)
        # - Ventana matches
        self.ventana_matches.volver_signal.connect(self.mostrar_principal)
        self.ventana_matches.enviar_mensaje_signal.connect(parent.enviar)
        self.ventana_matches.obtener_mensajes_signal.connect(parent.enviar)
        # - Ventana perfiles
        self.ventana_perfiles.volver_signal.connect(self.mostrar_principal)
        self.ventana_perfiles.solicitar_nuevo_usuario_signal.connect(parent.enviar)
        self.ventana_perfiles.dar_like_signal.connect(parent.enviar)

    def mostrar_login(self):
        """Muestra ventana de login (ventana_inicio)
        """
        self.nombre_usuario = None
        self.ventana_inicio.show()
        self.ventana_principal.close()

    def mostrar_principal(self):
        """Muestra ventana principal o menú principal del programa (ventana_principal)
        """
        self.ventana_principal.show()
        self.ventana_inicio.close()
        self.ventana_perfil.close()
        self.ventana_matches.close()
        self.ventana_perfiles.close()

    def mostrar_perfil(self):
        """Muestra ventana de perfil del usuario logeado (ventana_perfil). Hace fetch desde el
        servidor de la información correspondiente al usuario.
        """
        dict_ = {
            "comando": "obtener_datos_usuario"
        }
        self.enviar_signal.emit(dict_)
        self.ventana_perfil.show()
        self.ventana_principal.close()

    def mostrar_matches(self):
        """Muestra ventana de matches del usuario logeado (ventana_matches). Hace fetch desde el
        servidor de los matches que tiene el usuario.
        """
        dict_ = {
            "comando": "obtener_matches_usuario"
        }
        self.enviar_signal.emit(dict_)
        self.ventana_matches.show()
        self.ventana_principal.close()

    def mostrar_perfiles(self):
        """Muestra ventana de matching, que permite a un usuario dar like o pasar perfiles
        perfiles aleatorios proporcionados por el servidor. Hace fetch desde el servidor del perfil
        aleatorio a mostrar.
        """
        self.ventana_perfiles.nombre_usuario = self.nombre_usuario
        dict_ = {
            "comando": "obtener_perfil_aleatorio"
        }
        self.enviar_signal.emit(dict_)
        self.ventana_perfiles.show()
        self.ventana_principal.close()

    def manejar_mensaje(self, mensaje):
        """
        Maneja un mensaje recibido desde el servidor.
        Genera la respuesta y los cambios en la interfaz correspondientes.

        Argumentos:
            mensaje (dict): Mensaje ya decodificado recibido desde el servidor
        """
        try:
            comando = mensaje["comando"]
        except KeyError:
            return []
        if comando == "ingreso_aceptado":
            self.nombre_usuario = mensaje["nombre_usuario"]
            self.mostrar_ventana_principal_signal.emit()
        elif comando == "ingreso_rechazado":
            self.ventana_inicio.recibir_feedback_signal.emit(mensaje)
        elif comando == "datos_perfil_usuario":
            self.ventana_perfil.obtener_perfil_signal.emit(mensaje)
        elif comando == "datos_matches_usuario":
            self.ventana_matches.obtener_matches_usuario_signal.emit(mensaje)
        elif comando == "datos_perfil_aleatorio":
            self.ventana_perfiles.obtener_nuevo_usuario_signal.emit(mensaje)
        elif comando == "datos_mensajes":
            mensaje["mensajes"].sort(key=lambda x: datetime.fromisoformat(x[1]))
            self.ventana_matches.cargar_mensajes_signal.emit(mensaje)
        elif comando == "recibir_mensaje_chat":
            self.ventana_matches.recibir_mensaje_signal.emit(mensaje)
        else:
            self.log(f"Error: comando {comando} inválido")
