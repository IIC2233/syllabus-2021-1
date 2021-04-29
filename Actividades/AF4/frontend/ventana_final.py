import sys
import os
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import pyqtSignal, QUrl, QSize
from PyQt5.QtGui import QMovie, QFont
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer


# ----- NO EDITAR -----
class VentanaFinal(QWidget):

    def __init__(self, ancho, alto, volumen, ruta_fiesta, ruta_smoke, ruta_victoria, ruta_derrota):
        # Definición de atributos
        super().__init__()

        self.tamano = (ancho, alto)
        self.setFixedSize(*self.tamano)

        self.volumen = volumen
        self.init_gui(ruta_fiesta, ruta_smoke, ruta_victoria, ruta_derrota)

    def init_gui(self, ruta_fiesta, ruta_smoke, ruta_victoria, ruta_derrota):
        # Reproductor de musica
        url_victoria = QUrl.fromLocalFile(ruta_victoria)
        self.kumbia = QMediaContent(url_victoria)
        url_derrota = QUrl.fromLocalFile(ruta_derrota)
        self.flauta_sad = QMediaContent(url_derrota)
        self.reproductor = QMediaPlayer()
        self.reproductor.setVolume(self.volumen)

        # Letras
        letra1 = QFont()
        letra1.setFamily("Agency FB")
        letra1.setPointSize(70)
        letra1.setBold(True)
        letra2 = QFont()
        letra2.setFamily("Agency FB")
        letra2.setPointSize(75)
        letra2.setBold(True)

        # Gifs
        self.label_gif = QLabel('', self)
        self.gif_fiesta = QMovie(ruta_fiesta)
        self.gif_smoke = QMovie(ruta_smoke)

        # Texto
        self.label_borde = QLabel('', self)
        self.label_borde.setFont(letra2)
        self.label_texto = QLabel('', self)
        self.label_texto.setFont(letra1)

    def actualizar_pantalla(self, gif, texto, musica):
        # Setea el gif, texto y musica correspondiente a la ventana.
        self.label_gif.setMovie(gif)
        gif.setScaledSize(QSize(*self.tamano))
        self.label_gif.resize(*self.tamano)
        self.reproductor.setMedia(musica)
        self.label_texto.setText(texto)
        self.label_texto.resize(self.label_texto.sizeHint())
        self.label_borde.setText(texto)
        self.label_borde.resize(self.label_borde.sizeHint())

    def mostrar_final(self, victoria):
        # Realiza cambios especificos a las situaciones de victoria o derrota a la ventana.
        # Son diferencias puramente esteticas.
        # Comienza la reproducion del GIF y la musica y muestra la ventana.
        if victoria:
            self.actualizar_pantalla(self.gif_fiesta, 'YOU WIN', self.kumbia)
            self.label_borde.setStyleSheet('color: rgb(255, 225, 225);')
            self.label_texto.setStyleSheet('color: rgb(255, 51, 102);')
            self.label_texto.move((self.width() - self.label_texto.width()) // 2, 30)
            self.label_borde.move((self.width() - self.label_borde.width()) // 2, 30)
            self.gif_fiesta.start()
        else:
            self.actualizar_pantalla(self.gif_smoke, 'YOU LOSE', self.flauta_sad)
            self.label_borde.setStyleSheet('color: rgb(0, 0, 0);')
            self.label_texto.setStyleSheet('color: rgb(255, 225, 225);')
            self.label_texto.move((self.width() - self.label_texto.width()) // 2,
                                  self.height() - 150)
            self.label_borde.move((self.width() - self.label_borde.width()) // 2,
                                  self.height() - 150)
            self.gif_smoke.start()
        self.reproductor.play()
        self.show()
