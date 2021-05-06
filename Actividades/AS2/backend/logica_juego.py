import random
import sys

from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QThread
from PyQt5.QtWidgets import QApplication

import parametros as p
from utils import coordenadas_figuras


class Juego(QObject):
    # DEBES MODIFICAR ESTA CLASE

    def __init__(self):
        # NO MODIFICAR
        super().__init__()
        self.ancho = p.ANCHO_GRILLA
        self.alto = p.ALTO_GRILLA
        self.tiempo_de_avance = p.TIEMPO_AVANCE
        self.diccionario_figuras = coordenadas_figuras()
        self.bloques = []
        self.puntaje = 0
        self.diccionario_grilla = {}
        self.crear_grilla()

    #ACA SE ENCUENTRAN LOS MÉTODOS A MODIFICAR

    def comenzar_partida(self):
        # COMPLETAR
       pass

    def actualizar_grilla(self):
        # COMPLETAR
        self.vaciar_grilla()
        for bloque in self.bloques:
            x, y = bloque.posicion_x, bloque.posicion_y
            self.diccionario_grilla[(x, y)] = bloque.color

        # DESDE ACA DEBES EDITAR
        pass

    def actualizar_puntaje(self):
        # COMPLETAR
        pass

    def game_over(self):
        # COMPLETAR
        pass

    # NO MODIFICAR ESTOS MÉTODOS
    
    def crear_grilla(self):
        # NO MODIFICAR
        for fila in range(self.alto):
            for columna in range(self.ancho):
                self.diccionario_grilla[(columna, fila)] = 'transparent'

    def mover_bloque(self, event):
        # NO MODIFICAR
        direccion = event['direccion']
        dict_dirrecion = {'left': -1, 'right': 1}
        bloques_moviendose = []
        for bloque in self.bloques:
            if bloque.moviendose:
                bloques_moviendose.append(bloque)
        colision = False
        for bloque in bloques_moviendose:
            nuevo_x = bloque.posicion_x + dict_dirrecion[direccion]
            nuevo_y = bloque.posicion_y

            if nuevo_x >= 0 and nuevo_x < self.ancho:
                if self.diccionario_grilla[(nuevo_x, nuevo_y)] != 'transparent':
                    for bloque_colisionado in self.bloques:
                        if bloque_colisionado.posicion_x == nuevo_x and \
                                bloque_colisionado.posicion_y == nuevo_y and \
                                    bloque_colisionado.moviendose is False:
                            colision = True

            else:
                colision = True

        if colision is False:
            for bloque in bloques_moviendose:
                bloque.moverse(dict_dirrecion[direccion])

    def enviar_bloque(self):
        # NO MODIFICAR
        colores = ['red', 'lightgreen', 'cyan', 'yellow', 'magenta']
        color = colores[random.randint(0, len(colores) - 1)]
        x = random.randint(4, self.ancho - 5)
        figuras = list(self.diccionario_figuras.keys())
        figura = figuras[random.randint(0, len(figuras) - 1)]
        for coordenadas in self.diccionario_figuras[figura]:
            x_bloque = coordenadas[0] + x
            y_bloque = coordenadas[1]
            mi_bloque = Bloque(color, x_bloque, y_bloque, self)
            self.bloques.append(mi_bloque)

    def avanzar_bloques(self):
        # NO MODIFICAR
        fin_partida = False
        choque = False
        for bloque in self.bloques:
            if bloque.moviendose:
                if self.revisar_colisiones(bloque) is True:
                    choque = True
        if choque is True:
            self.verificar_linea()
            for bloque in self.bloques:
                if bloque.moviendose:
                    bloque.moviendose = False
                    if bloque.posicion_y == 0:
                        self.game_over()
                        fin_partida = True
            if fin_partida is False:
                self.enviar_bloque()
        else:
            for bloque in self.bloques:
                if bloque.moviendose:
                    bloque.avanzar()
            self.actualizar_grilla()

    def revisar_colisiones(self, bloque):
        # NO MODIFICAR
        posicion_x = bloque.posicion_x
        posicion_y = bloque.posicion_y
        nuevo_x = posicion_x
        nuevo_y = bloque.posicion_y + 1
        if posicion_y >= self.alto - 1:
            return True
        elif self.diccionario_grilla[(nuevo_x, nuevo_y)] != 'transparent':
            for bloque_colisionado in self.bloques:
                if bloque_colisionado.posicion_x == nuevo_x and \
                        bloque_colisionado.posicion_y == nuevo_y:
                    if bloque_colisionado.moviendose is False:
                        return True
        return False

    def vaciar_grilla(self):
        # NO MODIFICAR
        for key in self.diccionario_grilla.keys():
            self.diccionario_grilla[key] = 'transparent'


    def verificar_linea(self):
        # NO MODIFICAR
        fila = 0
        while fila < self.alto:
            fila_completa = [
                self.diccionario_grilla[(columna, fila)]
                for columna in range(0, self.ancho)
            ]
            llena = True
            if "transparent" in fila_completa:
                llena = False
            if llena:
                self.eliminar_linea(fila)
            else:
                fila += 1

    def eliminar_linea(self, fila_eliminada):
        # NO MODIFICAR
        fila = 0
        while fila < len(self.bloques):
            if self.bloques[fila].posicion_y == fila_eliminada:
                self.bloques.pop(fila)
            elif self.bloques[fila].posicion_y < fila_eliminada:
                self.bloques[fila].avanzar()
                fila += 1
            else:
                fila += 1
        self.actualizar_grilla()
        self.actualizar_puntaje()



class Bloque():
    # NO DEBES MODIFICAR ESTA CLASE

    def __init__(self, color, x, y, padre):
        self.padre = padre
        self.color = color
        self.posicion_x = x
        self.posicion_y = y
        self.moviendose = True

    def avanzar(self):
        self.posicion_y += 1

    def moverse(self, sentido):
        self.posicion_x += sentido

