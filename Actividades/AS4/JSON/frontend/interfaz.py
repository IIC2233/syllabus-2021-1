"""
Este módulo contiene la implementación de la interfaz gráfica en PyQt5

NO DEBES MODIFICARLO
"""
from functools import partial
from PyQt5.QtWidgets import (QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QTextEdit, QCheckBox)
from mensajes import Mensaje


class VentanaChats(QWidget):
    """
    Esta clase representa la ventana de la interfaz gráfica que da acceso a los
    mensajes de la parte JSON.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filtrar_mensajes = False
        self.mostrando_grupo = None
        self.__init_gui()
        self.__retranslate_ui()
        self.cargar_botones()

    def __init_gui(self):
        # Main widget declaration
        self.title_label = QLabel(self)
        self.text_area = QTextEdit(self)
        self.filter_toggle = QCheckBox(self)
        self.main_horizontal_layout = QHBoxLayout(self)
        self.buttons_layout = QGridLayout()
        self.right_layout = QVBoxLayout()

        # Add widgets to layout
        self.main_horizontal_layout.addLayout(self.buttons_layout)
        self.main_horizontal_layout.addLayout(self.right_layout)
        self.right_layout.addWidget(self.title_label)
        self.right_layout.addWidget(self.text_area)
        self.right_layout.addWidget(self.filter_toggle)
        self.text_area.setMinimumWidth(600)
        self.text_area.setMinimumHeight(400)

        self.text_area.setReadOnly(True)

        self.filter_toggle.setCheckState(self.filtrar_mensajes)
        self.filter_toggle.toggled.connect(self.filterToggleEvent)

    def __retranslate_ui(self):
        self.setWindowTitle("DCChatApp 2 [v. beta 0.8.2] - Chats")
        self.title_label.setText("Selecciona un chat")
        self.filter_toggle.setText("Filtrar mensajes sospechosos")

    def cargar_botones(self):
        """
        Carga los botones a mostrar según los grupos existentes
        """
        if not Mensaje.grupos:
            label = QLabel("\u26A0 Acceso denegado \u26A0 \n\nNo se detectaron grupos", self)
            self.buttons_layout.addWidget(label)
            return
        i, j = 0, -1
        for grupo in Mensaje.grupos:
            if i % 2 == 0:
                j += 1
            col, row = i % 2, j
            button = QPushButton(grupo)
            button.clicked.connect(partial(self.cargar_mensajes_grupo, grupo))
            self.buttons_layout.addWidget(button, row, col)
            i += 1

    def cargar_mensajes_grupo(self, grupo):
        """
        Conectado a botones, carga mensajes del grupo correspondiente
        Imprime mensajes en QTextBox
        """
        texto = ""
        for mensaje in Mensaje.grupos[grupo]:
            if not self.filtrar_mensajes or mensaje.sospechoso:
                if mensaje.sospechoso:
                    texto += f"<p style=\"color: red\">{mensaje}<p/>"
                else:
                    texto += f"<p>{mensaje}<p/>"

        self.text_area.setHtml(texto)
        self.title_label.setText(f"Chat grupal: {grupo}")
        self.mostrando_grupo = grupo

    def filterToggleEvent(self, event):
        """
        Conectado a QCheckBox, cambia el estado del filtro y refresca mensajes
        """
        self.filtrar_mensajes = event
        if self.mostrando_grupo:
            self.cargar_mensajes_grupo(self.mostrando_grupo)
