"""
Interfaz de la ventana de inicio del programa
"""
from os import path
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QLineEdit, QPushButton, QLabel,
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, Qt


class VentanaInicio(QMainWindow):
    """
    Interfaz gráfica de ventana de inicio
    """

    enviar_nombre_usuario_signal = pyqtSignal(dict)
    recibir_feedback_signal = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_ui()
        self.__connect_events()
        self.__retranslate_ui()

    def __init_ui(self):
        self.resize(500, 400)

        # Declaración widget principal
        self.widget_central = QWidget(self)
        self.layout_vertical_principal = QVBoxLayout(self.widget_central)
        self.label_title = QLabel(self.widget_central)
        self.label_logo = QLabel(self.widget_central)
        self.layout_horizontal = QHBoxLayout()
        self.nombre_usuario_line = QLineEdit(self.widget_central)
        self.boton_entrar = QPushButton(self.widget_central)
        self.label_feedback = QLabel(self.widget_central)

        # Añade widgets a layout
        self.layout_vertical_principal.addStretch(1)
        self.layout_vertical_principal.addWidget(self.label_title, 0, Qt.AlignHCenter)
        self.layout_vertical_principal.addStretch(1)
        self.layout_vertical_principal.addWidget(self.label_logo, 0, Qt.AlignHCenter)
        self.layout_vertical_principal.addStretch(1)
        self.layout_horizontal.addWidget(self.nombre_usuario_line)
        self.layout_horizontal.addWidget(self.boton_entrar)
        self.layout_vertical_principal.addLayout(self.layout_horizontal)
        self.layout_vertical_principal.addWidget(self.label_feedback, 0, Qt.AlignHCenter)

        # Setear layout
        self.setCentralWidget(self.widget_central)

    def __retranslate_ui(self):
        # Button
        self.boton_entrar.setStyleSheet(
            "background-color: #000000; color: #ffffff; font-size: 24px"
        )

        # Colocar texto a widgets
        self.setWindowTitle("DCCitas \U0001F498 - Iniciar Sesión")
        self.label_title.setText("DCCitas \U0001F498")
        self.label_title.setStyleSheet("font-size: 62px;")
        self.label_title.setAlignment(Qt.AlignCenter)
        ruta_imagen = path.join("assets", "logo.png")
        image_pixmap = QPixmap(ruta_imagen).scaledToWidth(600)
        self.label_logo.setPixmap(image_pixmap)
        self.nombre_usuario_line.setStyleSheet("font-size: 24px")

        self.nombre_usuario_line.setPlaceholderText("Ingresa un nombre de usuario")
        self.boton_entrar.setText("Entrar")

    def __connect_events(self):
        # Hace que presionar enter tenga mismo comportamiento que botón "Entrar"
        self.nombre_usuario_line.returnPressed.connect(self.enviar_nombre_usuario)
        self.boton_entrar.clicked.connect(self.enviar_nombre_usuario)
        self.boton_entrar.setAutoDefault(True)

        self.recibir_feedback_signal.connect(self.recibir_feedback)

    def enviar_nombre_usuario(self):
        """
        Envía diccionario conteniendo texto en nombre_usuario_line (i.e. nombre_usuario) al
        backend mediante señal enviar_nombre_usuario_signal.
        """
        dict_ = {
            "comando": "ingreso",
            "nombre_usuario": self.nombre_usuario_line.text()
        }
        self.enviar_nombre_usuario_signal.emit(dict_)

    def recibir_feedback(self, dict_):
        """
        Recibe feedback desde backend, luego haber enviado el nombre.
        Actualiza label feedback.
        """
        feedback = dict_["comentario"]
        self.label_feedback.setText(feedback)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = VentanaInicio()
    window.show()
    sys.exit(app.exec_())
