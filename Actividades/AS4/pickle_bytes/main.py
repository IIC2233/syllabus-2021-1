"""
Este módulo corresponde a la parte Pickle/Bytes.
Su propósito es decodificar las clases entregadas para hacer funcionar la
interfaz.

NO DEBES MODIFICARLO
"""
import sys
from PyQt5.QtWidgets import QApplication
from backend.decodificador import Decoder
from frontend.interfaz import VentanaPrincipal
from filtros import obtener_paquete_secreto
from parametros import DIMENSIONES_VENTANA, RUTA_IMAGEN, RUTA_RR_LET_DOWN
from manejo_bytes import recuperar_contenido

if __name__ == "__main__":

    def hook(type_, value, traceback):
        """Hook para excepciones"""
        print(value, type_)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication(sys.argv)

    # Cargar filtros e instanciar decoder
    pickled_filters = obtener_paquete_secreto()
    decoder = Decoder(pickled_filters)

    # Instanciar ventana
    ventana = VentanaPrincipal(DIMENSIONES_VENTANA, RUTA_IMAGEN,
                               RUTA_RR_LET_DOWN, recuperar_contenido)

    # Conectar señales
    ventana.signal_pedir_imagen.connect(decoder.aplicar_filtro)
    decoder.imagen_actualizada_signal.connect(ventana.actualizar_imagen)
    decoder.nombres_filtros_signal.connect(ventana.cargar_botones)

    # Iniciar interfaz
    decoder.startup()
    ventana.show()

    sys.exit(app.exec_())
