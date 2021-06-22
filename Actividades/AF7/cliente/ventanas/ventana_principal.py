"""
Interfaz de la ventana principal del programa
"""
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QHBoxLayout, QVBoxLayout, QPushButton,
)
from PyQt5.QtCore import pyqtSignal


class VentanaPrincipal(QMainWindow):
    """
    Interfaz gráfica de ventana principal
    """

    volver_signal = pyqtSignal(dict)
    abrir_perfil_signal = pyqtSignal()
    abrir_matches_signal = pyqtSignal()
    ver_perfiles_signal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__init_ui()
        self.__connect_events()
        self.__retranslate_ui()

    def __init_ui(self):

        # Main widget declaration
        self.central_widget = QWidget(self)
        self.main_horizontal_layout = QHBoxLayout(self.central_widget)
        self.button_layout = QVBoxLayout()
        self.volver_button = QPushButton(self.central_widget)
        self.profile_button = QPushButton(self.central_widget)
        self.matches_button = QPushButton(self.central_widget)
        self.profiles_button = QPushButton(self.central_widget)

        # Add widgets to layout
        self.button_layout.addWidget(self.volver_button)
        self.button_layout.addWidget(self.profile_button)
        self.button_layout.addWidget(self.matches_button)
        self.button_layout.addWidget(self.profiles_button)
        self.main_horizontal_layout.addLayout(self.button_layout)

        # Set layout
        self.setCentralWidget(self.central_widget)

    def __retranslate_ui(self):
        self.setWindowTitle("DCCitas \U0001F498 - Ventana Principal")
        self.volver_button.setText("Volver")
        self.profile_button.setText("Ver mi perfil")
        self.matches_button.setText("Matches")
        self.profiles_button.setText("Ver perfiles")

    def __connect_events(self):
        self.volver_button.clicked.connect(self.log_out)
        self.profile_button.clicked.connect(self.abrir_perfil_signal.emit)
        self.matches_button.clicked.connect(self.abrir_matches_signal.emit)
        self.profiles_button.clicked.connect(self.ver_perfiles_signal.emit)

    def log_out(self):
        """
        Envía mensaje a servidor comunicando que se cerrará la sesión del usuario
        voluntariamente.
        """
        dict_ = {
            "comando": "salida"
        }
        self.volver_signal.emit(dict_)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec_())
