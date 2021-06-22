"""
Interfaz de la ventana de los matches del usuario del programa
"""
from functools import partial
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QLabel,
)
from PyQt5.QtCore import pyqtSignal
from ventanas.chat_widget import ChatWidget


class VentanaMatches(QMainWindow):
    """
    Interfaz gráfica de ventana de matches
    """

    volver_signal = pyqtSignal()
    obtener_matches_usuario_signal = pyqtSignal(dict)
    obtener_mensajes_signal = pyqtSignal(dict)
    enviar_mensaje_signal = pyqtSignal(dict)
    recibir_mensaje_signal = pyqtSignal(dict)
    cargar_mensajes_signal = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.nombre_usuario = None
        self.chat_widget = None

        self.__init_ui()
        self.__connect_events()
        self.__retranslate_ui()

    def __init_ui(self):

        # Main widget declaration
        self.central_widget = QWidget(self)
        self.main_horizontal_layout = QHBoxLayout(self.central_widget)
        self.left_vertical_layout = QVBoxLayout()
        self.right_vertical_layout = QVBoxLayout()
        self.top_horizontal_layout = QHBoxLayout()
        self.matches_vertical_layout = QVBoxLayout()
        self.title_label = QLabel(self.central_widget)
        self.volver_button = QPushButton(self.central_widget)

        # Add widgets to layout
        self.top_horizontal_layout.addWidget(self.title_label)
        self.top_horizontal_layout.addStretch(1)
        self.top_horizontal_layout.addWidget(self.volver_button)
        self.left_vertical_layout.addLayout(self.top_horizontal_layout)
        self.left_vertical_layout.addLayout(self.matches_vertical_layout)
        self.main_horizontal_layout.addLayout(self.left_vertical_layout)
        self.main_horizontal_layout.addLayout(self.right_vertical_layout)

        # Set layout
        self.setCentralWidget(self.central_widget)

    def __retranslate_ui(self):
        self.setWindowTitle("DCCitas \U0001F498 - Mis matches")
        self.title_label.setText("Matches de USER")
        self.volver_button.setText("Volver")

    def __connect_events(self):
        self.volver_button.clicked.connect(self.volver_event)
        self.obtener_matches_usuario_signal.connect(self.actualizar_matches)
        self.recibir_mensaje_signal.connect(self.recibir_mensaje)
        self.cargar_mensajes_signal.connect(self.cargar_mensajes)

    def actualizar_matches(self, datos_matches):
        """
        Actualiza los elementos gráficos de la interfaz según los matches recibidos para el
        usuario específico.
        """
        self.nombre_usuario = datos_matches['nombre_usuario']
        self.title_label.setText(f"Matches de {datos_matches['nombre_usuario']}")
        # Borrar labels anteriores del layout:
        self.borrar_items_layout(self.matches_vertical_layout)
        for matched_user in datos_matches['matches']:
            line_horizontal_layout = QHBoxLayout()
            label = QLabel(matched_user)
            button = QPushButton("Chat")
            button.clicked.connect(partial(self.empezar_chat, matched_user))
            line_horizontal_layout.addWidget(label)
            line_horizontal_layout.addStretch(1)
            line_horizontal_layout.addWidget(button)
            self.matches_vertical_layout.addLayout(line_horizontal_layout)

    def borrar_items_layout(self, layout):
        """
        Borra recursivamente todos los contenidos de un layout
        """
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
                else:
                    self.borrar_items_layout(item.layout())

    def empezar_chat(self, usuario):
        """
        Crea una nueva instancia del Widget de chat (o la reemplaza) para empezar un chat
        con el usuario especificado. Recupera los mensajes ya enviados desde el servidor.
        """
        if self.chat_widget:
            self.chat_widget.setParent(None)
        self.chat_widget = ChatWidget(usuario, self.central_widget)
        self.chat_widget.enviar_texto_signal.connect(self.redirigir_mensaje)
        self.right_vertical_layout.addWidget(self.chat_widget)
        dict_ = {
            "comando": "obtener_mensajes",
            "destinatario": usuario
        }
        self.obtener_mensajes_signal.emit(dict_)

    def cargar_mensajes(self, dict_):
        """
        Recibe desde el servidor los mensajes entre el usuario actual y el objetivo, y los carga en
        el widget correspondiente.
        """
        if self.chat_widget:
            for mensaje in dict_["mensajes"]:
                self.chat_widget.add_message(f">{mensaje[0]}: {mensaje[2]}")

    def redirigir_mensaje(self, dict_):
        """
        Hace que la señal del widget de chat sea estática, y no se pierda la conexión de esta
        cada vez que se renueva el widget.
        """
        self.enviar_mensaje_signal.emit(dict_)

    def recibir_mensaje(self, dict_):
        """
        Redirige un mensaje recibido desde el cliente hacia el widget correspondiente
        """
        if self.chat_widget and dict_["emisor"] in [self.nombre_usuario, self.chat_widget.target]:
            self.chat_widget.add_message(dict_["texto"])

    def volver_event(self):
        """
        Cierra/elimina el widget del chat antes de emitir la señal para volver.
        """
        if self.chat_widget:
            self.chat_widget.setParent(None)
        self.volver_signal.emit()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = VentanaMatches()
    window.show()
    sys.exit(app.exec_())
