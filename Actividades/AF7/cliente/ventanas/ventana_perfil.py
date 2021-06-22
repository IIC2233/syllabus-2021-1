"""
Interfaz de la ventana del perfil de usuario del programa
"""
from base64 import b64decode
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QTextEdit, QHBoxLayout, QPushButton, QLabel,
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, Qt


class VentanaPerfil(QMainWindow):
    """
    Interfaz gráfica de ventana de perfil
    """

    volver_signal = pyqtSignal()
    obtener_perfil_signal = pyqtSignal(dict)
    actualizar_bio_signal = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.nombre_usuario = None

        self.setMaximumHeight(1000)
        self.setMaximumWidth(600)

        self.__init_ui()
        self.__connect_events()
        self.__retranslate_ui()

    def __init_ui(self):

        # Main widget declaration
        self.central_widget = QWidget(self)
        self.main_vertical_layout = QVBoxLayout(self.central_widget)
        self.top_horizontal_layout = QHBoxLayout()
        self.profile_label = QLabel(self.central_widget)
        self.picture_label = QLabel(self.central_widget)
        self.bio_text_box = QTextEdit(self.central_widget)
        self.volver_button = QPushButton(self.central_widget)
        self.submit_changes_button = QPushButton(self.central_widget)

        # Add widgets to layout
        self.top_horizontal_layout.addWidget(self.profile_label)
        self.top_horizontal_layout.addStretch(1)
        self.top_horizontal_layout.addWidget(self.volver_button)
        self.main_vertical_layout.addLayout(self.top_horizontal_layout)
        self.main_vertical_layout.addWidget(self.picture_label)
        self.main_vertical_layout.addWidget(self.bio_text_box)
        self.main_vertical_layout.addWidget(self.submit_changes_button)

        # Set layout
        self.setCentralWidget(self.central_widget)

    def __retranslate_ui(self):
        self.setWindowTitle("DCCitas \U0001F498 - Mi Perfil")
        self.profile_label.setText("Perfil de USER, EDAD")
        self.bio_text_box.setText("USER BIO")
        self.volver_button.setText("Volver")
        self.submit_changes_button.setText("Guardar cambios")

    def __connect_events(self):
        self.volver_button.clicked.connect(self.volver_signal.emit)
        self.submit_changes_button.clicked.connect(self.actualizar_bio)
        self.obtener_perfil_signal.connect(self.actualizar_perfil)

    def actualizar_perfil(self, datos_perfil):
        """
        Actualiza los elementos gráficos de la interfaz según los datos del perfil recibidos como
        argumento desde el cliente.
        """
        self.nombre_usuario = datos_perfil['nombre_usuario']
        imagen_bytes = b64decode(datos_perfil['imagen_bytes'])
        profile_pixmap = QPixmap()
        profile_pixmap.loadFromData(imagen_bytes, "PNG")
        profile_pixmap = profile_pixmap.scaled(600, 600, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.profile_label.setText(
            f"Perfil de {datos_perfil['nombre_usuario']}, {datos_perfil['edad']}")
        self.picture_label.setPixmap(profile_pixmap)
        self.bio_text_box.setText(datos_perfil["bio"])

    def actualizar_bio(self):
        """
        Envía al servidor (a través del cliente) un mensaje para actualizar los cambios a la
        bio del usuario.
        """
        dict_ = {
            "comando": "actualizar_bio",
            "bio": self.bio_text_box.toPlainText()
        }
        self.actualizar_bio_signal.emit(dict_)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = VentanaPerfil()
    window.show()
    sys.exit(app.exec_())
