from os.path import join
import sys
from PyQt5.QtWidgets import (
    QLabel, QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QApplication, QGridLayout, QSpinBox,
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal


class VentanaSeleccion(QWidget):
    """
    Ventana para seleccionar el personaje que se utilizara en el combate. Contiene un layout tipo
    grid en el centro, conformado por multiples imagenes. Posee un spinbox para elegir un numero
    de personaje y un boton para iniciar el juego con el personaje elegido.
    """
    # Señal para abrir la ventana de combate, envía los parámetros: nombre jugador, nombre personaje
    senal_abrir_ventana_combate = pyqtSignal(str, str)

    def __init__(self, ancho, alto, rutas_personajes, ruta_fondo):
        # NO MODIFICAR
        super().__init__()
        self.size = (ancho, alto)
        self.resize(ancho, alto)
        self.nombre = None
        self.diccionario_personajes = {
            i: f"personaje_{i}"
            for i in range(1, len(rutas_personajes) + 1)
        }
        self.spinbox_personaje = QSpinBox()
        self.rutas = {
            f"personaje_{i}": ruta
            for i, ruta in enumerate(rutas_personajes, start=1)
        }
        self.ruta_fondo = ruta_fondo
        self.grilla_personajes = QLabel(self)
        self.grilla_personajes.setFixedSize(ancho, alto)
        self.init_gui()

    def iniciar_combate(self):
        # COMPLETAR
        pass

    # ----------------------------------------------------------------
    # -------------------- NO MODIFICAR DESDE ACA --------------------
    # ----------------------------------------------------------------

    def init_gui(self):
        # NO MODIFICAR
        self.setWindowTitle("Seleccion personajes")
        # Creamos la grilla central
        grilla = QGridLayout()
        # Definimos los espacios entre elementos para que "calcen" con la imagen de fondo
        grilla.setHorizontalSpacing(4)
        grilla.setVerticalSpacing(8)
        numero_pj = 1  # Contador del elemento
        for fila in range(3):
            for columna in range(4):
                # Creamos una label, le seteamos la foto adecuada, el tamano y el estilo
                foto = QLabel()
                foto.setPixmap(QPixmap(self.rutas[f"personaje_{numero_pj}"]))
                foto.setStyleSheet("border: 4px solid rgb(252, 233, 0)")
                foto.setFixedSize(105, 153)
                # Agregamos la foto en la posicion y vamos al siguiente personaj
                grilla.addWidget(foto, fila, columna)
                numero_pj += 1
        # Creamos un VBox y un Hbox que centre la label de grilla de personajes. Le damos este
        # layout a la label que contiene la grilla
        vbox = QVBoxLayout(self.grilla_personajes)
        vbox.addSpacing(50)
        hbox = QHBoxLayout()
        hbox.addSpacing(45)
        hbox.addLayout(grilla)
        hbox.addSpacing(40)
        vbox.addLayout(hbox)
        # Le damos la imagen de fondo al contenedor de la grilla
        self.grilla_personajes.setPixmap(QPixmap(self.ruta_fondo))
        self.grilla_personajes.setScaledContents(True)
        # Esta es la seccion de botones inferiores.
        self.spinbox_personaje.setRange(1, 12)
        self.boton_comenzar = QPushButton("Iniciar combate")
        # Aqui definimos el layout general
        hbox_inferior = QHBoxLayout()
        hbox_inferior.addStretch()
        hbox_inferior.addWidget(self.spinbox_personaje)
        hbox_inferior.addWidget(self.boton_comenzar)
        vbox_total = QVBoxLayout(self)
        vbox_total.setContentsMargins(0, 0, 0, 0)
        vbox_total.addWidget(self.grilla_personajes)
        vbox_total.addStretch()
        vbox_total.addLayout(hbox_inferior)
        # Por ultimo, conectamos la señal
        self.boton_comenzar.clicked.connect(self.iniciar_combate)

    def abrir_ventana(self, nombre):
        # NO MODIFICAR
        # Método que recibe el nombre del jugador, lo guarda y muestra la ventana
        self.nombre = nombre
        self.show()
