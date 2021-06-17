"""
Este módulo corresponde a la parte Pickle/Bytes.
Su propósito es decodificar las clases entregadas para hacer funcionar la
interfaz.

NO DEBES MODIFICARLO
"""
import sys
from PyQt5.QtWidgets import QApplication
from frontend.interfaz import VentanaChats

from mensajes import Mensaje, cargar_mensajes

if __name__ == "__main__":

    def hook(type_, value, traceback):
        """Hook para excepciones"""
        print(value, type_)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication(sys.argv)

    # Cargar mensajes
    cargar_mensajes("mensajes.json")
    Mensaje.ordenar_mensajes()

    # Instanciar ventana
    ventana_chats = VentanaChats()

    # Iniciar interfaz
    ventana_chats.show()

    sys.exit(app.exec_())
