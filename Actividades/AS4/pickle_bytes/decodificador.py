"""
Este archivo contiene la clase Decoder

NO DEBES MODIFICARLO
"""
import pickle
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal


class Decoder(QObject):
    """
    Esta clase se encarga de almacenar los filtros decodificados, y aplicarlos
    a la imagen según las señales recibidas desde el frontend.
    """

    imagen_actualizada_signal = pyqtSignal(bytearray)
    nombres_filtros_signal = pyqtSignal(list)

    def __init__(self, filtros_serializados, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filtros = pickle.loads(filtros_serializados)

    def startup(self):
        """
        Envía nombres de los filtros al frontend. Ocurre cuando se inicializa
        la interfaz.
        """
        nombres_filtros = list(self.filtros.diccionario_filtros.keys())
        self.nombres_filtros_signal.emit(nombres_filtros)

    @pyqtSlot(str, bytearray)
    def aplicar_filtro(self, tipo_filtro, bytes_imagen):
        """
        Slot para cuando la interfaz apreta un botón de filtro. Se encarga de
        aplicar el efecto, y emite como respuesta una señal conteniendo los
        bytes resultantes.

        Argumentos:
            tipo_filtro (string): El nombre del filtro a aplicar
            bytes_imagen (bytearray): bytes representando la info de la imagen
        """
        final_bytes = self.filtros.modificar_bytes(tipo_filtro, bytes_imagen)
        self.imagen_actualizada_signal.emit(final_bytes)
