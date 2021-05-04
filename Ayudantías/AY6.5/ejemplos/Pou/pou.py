import os
import parameters as p
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer, QEventLoop


class PouF(QWidget):

    def __init__(self, width, height, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = (width, height)
        self.init_gui()
        self.corona = False

    def init_gui(self):
        self.setWindowTitle("Pou")
        self.setGeometry(400, 100, *self.size)
        
        ''' Creamos una etiqueta para simular un fondo (se puede hacer con StyleSheets) en QMainWindow'''
        self.background = QLabel(self)
        self.background.setGeometry(0, 0, *self.size)
        self.background.setPixmap(QPixmap("img/bg.jpg"))
        self.background.setScaledContents(True)

        '''El Pou se define como una QLabel con una imagen que inicialmente corresponde a la imagen del Pou limpio'''
        self.pou = QLabel(self)
        self.pou.setGeometry(100, self.size[1] - 200, p.pou_width, p.pou_height)
        self.pou.setPixmap(QPixmap("img/pou_limpio.png"))
        self.pou.setScaledContents(True)

        '''Creamos los botones para que el Pou baile y para poder limpiarlo'''
        self.dance_button = QPushButton("Bailar", self)
        self.dance_button.setMinimumSize(100, 50)
        self.dance_button.clicked.connect(self.dance)

        self.clean_button = QPushButton("Limpiar", self)
        self.clean_button.setMinimumSize(100, 50)
        self.clean_button.setEnabled(False)
        self.clean_button.clicked.connect(self.clean)

        '''Definimos un QWidget que contendrá al VLayout, el que a su vez tendrá en su interior los botones antes creados'''
        container = QWidget(self)
        container.setGeometry(650, 50, 150, 200)
        vbox = QVBoxLayout()

        vbox.addWidget(self.dance_button)
        vbox.addWidget(self.clean_button)

        container.setLayout(vbox)

    def dance(self):
        '''Cuando el Pou baila, se deshabilita el botón de bailar y luego continúan los movimientos'''
        self.dance_button.setEnabled(False)          

        for i in range(5):
            self.pou.move(self.pou.x() + 40 * i, self.pou.y())
            self.sleep(0.1)

        for i in range(5):
            self.pou.move(self.pou.x(), self.pou.y() - 40 * i)
            self.sleep(0.1)

        for i in range(5):
            self.pou.move(self.pou.x() - 40 * i, self.pou.y())
            self.sleep(0.1)

        for i in range(5):
            self.pou.move(self.pou.x(), self.pou.y() +  40 * i)
            self.sleep(0.1)

        ''' Una vez terminada la "animación" el Pou queda sucio y se habilita el botón de limpiar'''
        self.pou.setPixmap(QPixmap("img/pou_sucio.png"))
        self.clean_button.setEnabled(True)

    def clean(self):
        ''' Se deshabilita el botón para limpiar, luego se actualiza la imagen al Pou limpio y se habilita el de baile'''
        self.clean_button.setEnabled(False)
        self.pou.setPixmap(QPixmap("img/pou_limpio.png"))
        self.dance_button.setEnabled(True)

    def keyReleaseEvent(self, event):
        ''' El método keyReleaseEvent se llama cuando se suelta (release) una tecla (key). El método key() nos permite 
        obtener cuál fue la tecla presionada. Si la tecla es F queremos que se enferme o sane según su estado original.
        Por otra parte, si se presiona la W queremos simular una especie de salto.'''

        if event.key() == Qt.Key_F:
            if not self.corona:
                self.pou.setPixmap(QPixmap("img/pou_corona.png"))
                self.corona = True
            else:
                self.pou.setPixmap(QPixmap("img/pou_limpio.png"))
                self.corona = False
        
        elif event.key() == Qt.Key_W:
            for _ in range(5):
                self.pou.move(self.pou.x(), self.pou.y() - 5)
                self.sleep(0.05)

            for _ in range(5):
                self.pou.move(self.pou.x(), self.pou.y() + 5)
                self.sleep(0.05)

    def sleep(self, secs):
        ''' Equivalente a time.sleep(secs) compatible con PyQt5'''
        loop = QEventLoop()
        QTimer.singleShot(secs * 1000, loop.quit)
        loop.exec_()
        