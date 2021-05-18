import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer, QEventLoop

class VentanaConTodo(QWidget):

    def __init__(self, width, height, *args, **kwargs):
        ''' Se deben pasar los argumentos a la clase madre '''
        super().__init__(*args, **kwargs)
        self.size = (width, height)

        ''' Es buena práctica almacenar todo comando de inicio en un método similar '''
        self.init_gui()

    def init_gui(self):
        ''' Se configura el tamaño y título de la ventana '''
        self.setGeometry(400, 200, *self.size)
        self.setWindowTitle('Ventana con algunas cosas')

        # Comando para cambiar el stylesheet de algún objeto
        self.setStyleSheet("background-color: white")

        ''' Se crea personaje acompañador '''
        self.clip = QLabel(self)
        size_clip = [self.size[0] * 0.1, self.size[1] * 0.4] 
        self.clip.setGeometry(0, 0, *size_clip)
        #self.clip.setText("Algun texto aleatorio")
        self.clip.setPixmap(QPixmap("clip.jpg"))
        self.clip.setScaledContents(True)

        ''' Se crea un editor de texto y boton de búsqueda'''
        self.buscador = QLineEdit(self)
        self.boton_buscador = QPushButton("Buscar", self)
        self.boton_buscador.clicked.connect(self.buscando)

        ''' Labels de instrucciones '''
        self.mostrador = QLabel(self)
        self.mostrador.setText("Aquí se mostrará lo escrito al buscar")
        self.instrucciones_clip = QLabel(self)
        self.instrucciones_clip.setText("Presiona W o clickea el clip para saltar")
        # self.instrucciones_clip.setText("A Clip le gustan los clicks y la W")

        ''' Se ordenan los elementos  de la parte izquierda'''
        self.instrucciones_clip.move(50, 10)
        self.clip.move(100, self.size[1] - size_clip[1] - 5)

        ''' Se ordenan los elementos  de la parte derecha'''
        self.mostrador.move(300, 90)
        self.buscador.move(320, 130)
        self.boton_buscador.move(340, 160)

        ''' Se muestra la ventana, si no se muestra aca podría mostrarse al instanciarla'''
        ''' Si no se hace ninguno no se mostrará '''
        self.show()

    ''' Esto se ejecutará cuando pulsemos el boton buscar '''
    def buscando(self):
        # Se extrae el texto del QLineEdit
        nuevo_texto = self.buscador.text()
        # Se muestra utilizando setText
        self.mostrador.setText(nuevo_texto)

    ''' Esto detectará cuando soltemos una tecla '''
    def keyReleaseEvent(self, event):

        ''' Lo usamos para hacer que el personaje salte'''
        ''' El evento detecta la tecla presionada, y se puede '''
        ''' comparar con objetos Key de Qt'''
        if event.key() == Qt.Key_W:
            self.saltar()
    
    ''' Detectará cuando se presione el mouse '''
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and \
            self.clip.x() < event.x() < self.clip.x() + self.clip.size().width() and \
            self.clip.y() < event.y() < self.clip.y() + self.clip.size().height():
            
            self.saltar()
    
    ''' Mueve nuestro acompañante con el comando move() '''
    def saltar(self):
        for _ in range(30):
            self.clip.move(self.clip.x(), self.clip.y() - 5)
            self.sleep(0.005)

        for _ in range(30):
            self.clip.move(self.clip.x(), self.clip.y() + 5)
            self.sleep(0.005)

    def sleep(self, secs):
        ''' Equivalente a time.sleep(secs) compatible con PyQt5'''
        loop = QEventLoop()
        QTimer.singleShot(secs * 1000, loop.quit)
        loop.exec_()



''' Esto ayuda a levantar excepciones inesperadas '''
def hook(type, value, traceback):
        print(type)
        print(traceback)
sys.__excepthook__ = hook


''' Importantísimo siemore instanciar con UNA QApplication '''
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaConTodo(600, 300)
    sys.exit(app.exec_())