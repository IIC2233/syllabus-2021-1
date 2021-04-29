import os
import sys
from PyQt5.QtWidgets import (
    QLabel, QWidget, QLineEdit, QHBoxLayout,
    QVBoxLayout, QPushButton, QApplication,
)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap


class VentanaInicio(QWidget):
    """
    Ventana de log-in para el juego. Consta de una imagen, un campo de texto y un boton para
    ingresar. Es la primera ventana que se ve en el programa
    """
    senal_abrir_eleccion_personaje = pyqtSignal(str)  # Señal que abre la ventana de eleccion
    senal_elegir_nombre = pyqtSignal(str)  # Señal para enviar el nombre al back-end para verificar

    def __init__(self, ancho, alto, ruta_logo):
        # NO MODIFICAR
        super().__init__()
        self.size = (ancho, alto)
        self.resize(ancho, alto)

        self.setWindowTitle("Ventana Inicio")

        self.init_gui(ruta_logo)  # Llamada a la funcion que inicia la interfaz

    def init_gui(self, ruta_logo):
        # COMPLETAR
        pass

    def enviar_nombre(self):
        # COMPLETAR
        pass

    def recibir_validacion(self, validado):
        # NO MODIFICAR
        """
        Este método recibe desde el back-end una señal que indica si el nombre enviado es
        valido o no. De ser valido, se sigue a la siguiente ventana. En el caso contrario, se borra
        el texto del QLine y se notifica que el nombre es invalido
        """
        if validado:
            self.hide()
            self.senal_abrir_eleccion_personaje.emit(self.line_edit_nombre.text())
        else:
            self.line_edit_nombre.clear()
            self.line_edit_nombre.setPlaceholderText("Nombre inválido")
