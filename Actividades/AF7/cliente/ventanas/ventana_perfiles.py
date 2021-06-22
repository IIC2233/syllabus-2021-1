"""
Interfaz de la ventana que muestra perfiles para hacer match al usuario
"""
from base64 import b64decode
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QLabel,
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, Qt


class VentanaPerfiles(QMainWindow):
    """
    Interfaz gráfica de ventana de perfiles
    """

    volver_signal = pyqtSignal()
    obtener_nuevo_usuario_signal = pyqtSignal(dict)
    solicitar_nuevo_usuario_signal = pyqtSignal(dict)
    dar_like_signal = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setMaximumHeight(1000)
        self.setMaximumWidth(600)

        self.nombre_usuario = None
        self.user_actual = None

        self.__init_ui()
        self.__connect_events()
        self.__retranslate_ui()

    def __init_ui(self):

        # Main widget declaration
        self.central_widget = QWidget(self)
        self.main_vertical_layout = QVBoxLayout(self.central_widget)
        self.top_horizontal_layout = QHBoxLayout()
        self.profile_vertical_layout = QVBoxLayout()
        self.bottom_horizontal_layout = QHBoxLayout()
        self.volver_button = QPushButton(self.central_widget)
        self.nombre_usuario_label = QLabel(self.central_widget)
        self.picture_label = QLabel(self.central_widget)
        self.bio_label = QLabel(self.central_widget)
        self.pass_button = QPushButton(self.central_widget)
        self.like_button = QPushButton(self.central_widget)

        self.bio_label.setWordWrap(True)

        # Add widgets to layout
        self.top_horizontal_layout.addStretch(1)
        self.top_horizontal_layout.addWidget(self.volver_button)
        self.main_vertical_layout.addLayout(self.top_horizontal_layout)
        self.profile_vertical_layout.addWidget(self.nombre_usuario_label)
        self.profile_vertical_layout.addWidget(self.picture_label)
        self.profile_vertical_layout.addWidget(self.bio_label)
        self.main_vertical_layout.addLayout(self.profile_vertical_layout)
        self.bottom_horizontal_layout.addWidget(self.pass_button)
        self.bottom_horizontal_layout.addWidget(self.like_button)
        self.main_vertical_layout.addLayout(self.bottom_horizontal_layout)

        # Set layout
        self.setCentralWidget(self.central_widget)

    def __retranslate_ui(self):
        self.setWindowTitle("DCCitas \U0001F498 - Ver Perfiles")
        self.nombre_usuario_label.setText("USER, EDAD")
        self.bio_label.setText("BIO")
        self.volver_button.setText("Volver")
        self.pass_button.setText("PASS")
        self.like_button.setText("LIKE")

    def __connect_events(self):
        self.volver_button.clicked.connect(self.volver_signal.emit)
        self.obtener_nuevo_usuario_signal.connect(self.actualizar_perfil_mostrado)
        self.pass_button.clicked.connect(self.solicitar_nuevo_usuario)
        self.like_button.clicked.connect(self.dar_like)

    def actualizar_perfil_mostrado(self, datos_perfil):
        """
        Actualiza los elementos gráficos de la interfaz el perfil recibido.
        """
        self.user_actual = datos_perfil['nombre_usuario']
        if datos_perfil['nombre_usuario']:
            self.nombre_usuario_label.setText(
                f"{datos_perfil['nombre_usuario']}, {datos_perfil['edad']}")
            self.bio_label.setText(datos_perfil['bio'])
            imagen_bytes = b64decode(datos_perfil['imagen_bytes'])
            profile_pixmap = QPixmap()
            profile_pixmap.loadFromData(imagen_bytes, "PNG")
            profile_pixmap = profile_pixmap.scaled(
                600, 600, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.picture_label.setPixmap(profile_pixmap)
        else:
            self.nombre_usuario_label.setText("No se pudo obtener un usuario \U0001F494")

    def solicitar_nuevo_usuario(self):
        """
        Vuelve a solicitar al servidor un perfil aleatorio para mostrarlo al usuario
        mediante señales.
        """
        dict_ = {
            "comando": "obtener_perfil_aleatorio"
        }
        self.solicitar_nuevo_usuario_signal.emit(dict_)

    def dar_like(self):
        """
        Envía al servidor un mensaje indicando que se le da like al usuario mostrado actualmente.
        """
        dict_ = {
            "comando": "dar_like_usuario",
            "nombre_usuario_like": str(self.user_actual)
        }
        self.dar_like_signal.emit(dict_)
        self.solicitar_nuevo_usuario()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = VentanaPerfiles()
    window.show()
    sys.exit(app.exec_())
