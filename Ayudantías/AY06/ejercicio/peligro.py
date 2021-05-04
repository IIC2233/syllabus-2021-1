import sys
import os

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QMovie

"""
Creamos nuestra ventana principal heredando desde la GUI creada con Designer.
La función loadUiType retorna una tupla en donde el primer elemento
corresponde al nombre de la ventana definido en QtDesigner, y el segundo
elemento a la clase base de la GUI.
"""

window_name, base_class = uic.loadUiType("peligro.ui")


class MainWindow(window_name, base_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.widget_sorpresa.hide()

        # Label de la sorpresa final
        self.label_gif = QLabel('', self.centralwidget)
        self.label_gif.move(0, 0)
        self.label_gif.resize(self.widget_sorpresa.size())
        ruta = os.path.join('tenor.gif')
        self.gif = QMovie(ruta)
        self.label_gif.setMovie(self.gif)
        self.gif.setScaledSize(self.label_gif.size())
        self.label_gif.hide()

        # Conectando un botón dentro del Ui con un elemento fuera de este
        self.boton_adopcion.clicked.connect(self.boom)

    def boom(self):
        # Boom
        self.gif.start()
        self.label_gif.show()


if __name__ == '__main__':
    app = QApplication([])
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
