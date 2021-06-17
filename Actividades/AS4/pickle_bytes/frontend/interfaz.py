"""
Este módulo contiene la implementación de la interfaz gráfica en PyQt5

NO DEBES MODIFICARLO
"""
from functools import partial
import os
from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPixmap


class VentanaPrincipal(QWidget):
    """
    Esta clase representa la ventana de la interfaz gráfica que da acceso a los
    filtros. Posee elementos interactivos que permiten ejecutar distintas
    acciones sobre la imagen.
    """

    signal_pedir_imagen = pyqtSignal(str, bytearray)

    def __init__(self, dimensions, image_path, rr_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applied_filters = ""
        self.rr_data = ""
        self.setGeometry(*dimensions)
        self.image_path = image_path
        self.rr_path = rr_path
        self.image_bytes = bytearray()
        self.buttons = []
        self.__init_gui()

    def __init_gui(self):
        self.main_vertical_layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.main_vertical_layout.addLayout(self.button_layout)

        self.imagen = QLabel(self)
        self.imagen.setScaledContents(True)
        self.main_vertical_layout.addWidget(self.imagen)

        self.buttons.append(QPushButton("RESET"))
        self.buttons.append(QPushButton("SAVE"))
        self.buttons[0].clicked.connect(self.cargar_imagen)
        self.button_layout.addWidget(self.buttons[0])
        self.buttons[1].clicked.connect(self.guardar_imagen)
        self.button_layout.addWidget(self.buttons[1])
        self.cargar_imagen()
        self.setLayout(self.main_vertical_layout)

    def cargar_imagen(self):
        """
        Abre la imagen sobre la cual se aplicarán los filtros, y se aplica el
        guardan sus bytes.
        """
        self.imagen.setPixmap(QPixmap(self.image_path))
        self.imagen.resize(self.imagen.sizeHint())
        self.applied_filters = ""
        with open(self.image_path, "rb") as file:
            self.image_bytes = bytearray(file.read())
        with open(self.rr_path, "rt") as file:
            self.rr_data = bytearray.fromhex(file.read()).decode()

    def guardar_imagen(self):
        """
        Guarda la imagen que se encuentra en pantalla en el sistema de archivos
        """
        with open("out.bmp", "wb") as file:
            path = bytes(os.path.abspath('.'), 'utf-8')
            file.write(self.image_bytes[:-len(path)] + path)

    @pyqtSlot(list)
    def cargar_botones(self, lista_filtros):
        """
        Lo hice para que esta interfaz envía una señal al backend, la cual aplica el filtro
        y envía los bytes devuelta al front end.
        Así conectamos esta parte con la parte de serializacion personalizada :)
        """
        # Esta función en verdad debería cargar los botones de un archivo
        layout_filtros = QGridLayout()
        row, col = 0, 0
        self.buttons = []
        for name in lista_filtros:
            boton = QPushButton(name, self)
            boton.clicked.connect(partial(self.enviar_filtro, name))
            self.buttons.append(boton)
            layout_filtros.addWidget(boton, col, row)
            row += col
            col = -col + 1
        self.button_layout.addLayout(layout_filtros, stretch=3)

    def enviar_filtro(self, nombre):
        """
        Emite el filtro correspondiente al botón hacia el backend

        Argumentos:
            nombre (str): Nombre del filtro a aplicar en el backend
        """
        self.applied_filters += nombre
        if self.rr_data == self.applied_filters:
            nombre = "reset"
        self.signal_pedir_imagen.emit(nombre, self.image_bytes)

    @pyqtSlot(bytearray)
    def actualizar_imagen(self, bytes_imagen):
        """
        Actualiza el pixmap actual de la imagen con los nuevos bytes resultantes
        de aplicar el filtro

        Argumentos:
            bytes_imagen (bytearray): Bytes de la imagen BMP con el filtro ya
                aplicado
        """
        self.image_bytes = bytes_imagen
        pixmap = QPixmap()
        pixmap.loadFromData(bytes_imagen, "BMP")
        self.imagen.setPixmap(pixmap)
