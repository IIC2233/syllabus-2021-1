from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QGridLayout
from PyQt5.QtCore import pyqtSignal


# Clase CalculatorF es una Widget que se preocupa de implementar el Front-end de la calculadora
class CalculatorF(QWidget):
    # La calculadora debe tener una señal personalizada para enviar información
    button_clicked_signal = pyqtSignal(str)

    def __init__(self, width, height, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tamano = (width, height)
        # Matriz que representa la posición y el contenido de los botones
        self.matriz_botones = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["0", "+", "-"],
            ["*", "/", "="],
        ]

        self.init_gui()

    def init_gui(self):
        # Se determina el tamano y la posicion de la ventana
        self.setGeometry(400, 100, *self.tamano)
        self.resize(*self.tamano)
        # Se crean la pantalla y el contenedor de los botones
        self.pantalla = QLabel(self)
        self.grilla = QGridLayout()
        # Estilo de la pantalla
        self.pantalla.setStyleSheet("background-color: black; color: white; font-size: 22px")
        # Se crea el Layout principal y se agregan los objetos correspondientes
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.pantalla)
        vbox.addLayout(self.grilla)

        self.cargar_teclado()

        self.show()

    def cargar_teclado(self):
        # Obtenemos el rango de la matriz para la iteracion
        ctd_filas = len(self.matriz_botones)
        ctd_columnas = len(self.matriz_botones[0])
        # Para cada indice de la matriz, se inserta un boton en esa posicion, con el texto igual
        # al string en esa posición de la matriz.
        for fila in range(ctd_filas):
            for columna in range(ctd_columnas):
                boton = QPushButton(self.matriz_botones[fila][columna])
                boton.setMinimumHeight(100)

                # Conectamos el evento click a la funcion adecuada
                boton.clicked.connect(self.boton_clickeado)

                self.grilla.addWidget(boton, fila, columna)
        # Creamos finalmente el boton de borrar, que ocupa toda la ultima fila
        boton_c = QPushButton("C")
        boton_c.setMinimumHeight(50)
        boton_c.clicked.connect(self.boton_clickeado)
        # El add de 5 argumentos toma: widget, from_row, from_column, rowSpan, columnSpan
        # El argumento rowSpan, columnSpan determina cuantas filas/columnas se ocuparan desde la
        # posicion
        self.grilla.addWidget(boton_c, 5, 0, 1, 3)

    def boton_clickeado(self):
        # Capturamos el texto del boton clickeado y el texto actual en pantalla
        texto_boton = self.sender().text()
        texto_actual = self.pantalla.text()
        # Si el boton es =, entonces enviamos el texto actual al back-end
        if texto_boton == "=":
            self.button_clicked_signal.emit(texto_actual)
        # Si el boton es C, entonces borramos todo en pantalla
        elif texto_boton == "C":
            self.pantalla.setText("")
        # De lo contrario es un numero o un operador, por lo que lo agregamos a la pantalla.
        else:
            self.pantalla.setText(texto_actual + texto_boton)

    # Se llama a este metodo cada vez que el back-end envia un resultado
    def refresh_screen(self, operacion):
        self.pantalla.setText(operacion)
