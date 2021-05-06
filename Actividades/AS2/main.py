import sys

from PyQt5.QtWidgets import QApplication

from backend.logica_juego import Juego, Bloque
from backend.ventana_inicio_backend import VentanaInicioBackend
from frontend.ventana_inicio import VentanaInicio, VentanaError
from frontend.ventana_juego import VentanaJuego, VentanaFin

import parametros as p


def hook(type_error, traceback):
    print(type_error)
    print(traceback)


if __name__ == '__main__':
    # No modificar ->
    sys.__excepthook__ = hook
    app = QApplication(sys.argv)

    # Ventana inicio (front-end y back-end)
    ventana_inicio = VentanaInicio()
    logica_inicio = VentanaInicioBackend(p.RUTA_CANCION)

    # Ventana juego (front-end y back-end)
    ventana_juego = VentanaJuego()
    logica_juego = Juego()

    # Ventanas adicionales
    ventana_error = VentanaError()
    ventana_fin_juego = VentanaFin()

    # DESDE ACA PUEDES MODIFICAR

    # SEÑALES DE VENTANA DE INICIO (Parte I)
    """
    Debes completar esta sección
    """
    

    # SEÑALES DE VENTANA DE JUEGO (Parte II)
    """
    No modificar estas señales
    """
    ventana_juego.senal_teclas.connect(logica_juego.mover_bloque)
    ventana_juego.empezar_senal_frontend.connect(logica_juego.comenzar_partida)

    """
    Modificar desde acá.
    """

    # FIN DE JUEGO (Parte III)
    """
    Debes completar esta sección
    """

    #NO MODIFICAR
    sys.exit(app.exec_())
    app.exec()
