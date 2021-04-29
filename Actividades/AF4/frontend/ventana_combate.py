from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QProgressBar
from PyQt5.QtCore import pyqtSignal, QTimer, QEventLoop
from PyQt5.QtGui import QPixmap, QMovie, QFont


class VentanaCombate(QLabel):
    # Señal utilizada para abrir la ventana final. Envía el resultado del combate
    senal_abrir_ventana_final = pyqtSignal(bool)
    # Señal que envia comandos al back-end
    senal_envio_info_backend = pyqtSignal(str)

    def __init__(self, ancho, alto, rutas, rutas_iconos, estilo_botones):
        # NO MODIFICAR
        super().__init__()
        self.size = (ancho, alto)
        self.resize(ancho, alto)
        self.boton_patada = QPushButton("Patada")
        self.boton_frio = QPushButton("Frio")
        self.boton_defender = QPushButton("Defender")
        self.en_accion = False
        self.rutas = rutas  # Rutas de sprites
        self.rutas_iconos = {  # Rutas iconos
            f"personaje_{i}": ruta
            for i, ruta in enumerate(rutas_iconos, start=1)
        }
        self.estilo_botones = estilo_botones
        self.init_gui()

    def conectar_botones(self):
        # COMPLETAR
        pass

    def cambiar_estado_defensa(self, defendiendo):
        # COMPLETAR
        pass

    # --- Método necesario para completar la actividad (NO MODIFICAR) ---
    def cambiar_animacion_defensa(self, defendiendo):
        # NO MODIFICAR
        if defendiendo:
            gif_defensa = QMovie(self.rutas["defensa"])
            self.jugador.setMovie(gif_defensa)
            gif_defensa.start()
        else:
            self.jugador.setMovie(self.gif_jugador)

    # ----------------------------------------------------------------
    # -------------------- NO MODIFICAR DESDE ACA --------------------
    # ----------------------------------------------------------------
    def init_gui(self):
        """
        Inicia la interfaz de la ventana de combate
        """
        self.setWindowTitle("El duelo de DCCarate ha comenzado!")
        # Fondo
        self.setPixmap(QPixmap(self.rutas['fondo']))
        self.setScaledContents(True)

        self.layout_principal = QVBoxLayout(self)

        # ---- Definicion de la barra superior ----
        contenedor_info = QVBoxLayout()  # Contenedor de la info superior
        # Label nombre jugador
        self.label_nombre = QLabel()
        font = QFont()
        font.setPointSize(22)
        font.setCapitalization(True)
        font.setFamily("Fantasy")
        self.label_nombre.setFont(font)
        self.label_nombre.setStyleSheet("color: rgb(244, 223, 9)")
        # Label icono jugador
        self.label_icono = QLabel(self)

        # Barras de vida
        self.barra_vida_enemigo = QProgressBar()
        self.barra_vida_enemigo.setTextVisible(False)
        self.barra_vida_enemigo.setStyleSheet('QProgressBar{background-color: rgb(255, 0, 0);'
                                              'border-style:solid;}')
        self.barra_vida_enemigo.setValue(100)
        self.barra_vida_jugador = QProgressBar()
        self.barra_vida_jugador.setTextVisible(False)
        self.barra_vida_jugador.setStyleSheet('QProgressBar{background-color: rgb(255, 0, 0);'
                                              'border-style:solid;}')
        self.barra_vida_jugador.setValue(100)

        # Contenedor horizontal del icono y el nombre
        hbox_superior = QHBoxLayout()
        hbox_superior.addWidget(self.label_icono)
        hbox_superior.addWidget(self.label_nombre)
        contenedor_info.addLayout(hbox_superior)

        # Contenedor horizontal de las barras de vida
        hbox_vidas = QHBoxLayout()
        hbox_vidas.addWidget(self.barra_vida_jugador)
        hbox_vidas.addWidget(self.barra_vida_enemigo)
        contenedor_info.addLayout(hbox_vidas)

        self.layout_principal.addLayout(contenedor_info)
        self.layout_principal.addStretch()

        # ---- Definicion del area de combate ----
        # Imagenes jugadores
        self.jugador = QLabel(self)
        self.jugador.setFixedSize(91.75 * 1.1, 187.5 * 1.1)
        self.gif_jugador = QMovie(self.rutas['jugador'])
        self.jugador.setMovie(self.gif_jugador)
        self.jugador.setScaledContents(True)
        self.gif_jugador.start()
        self.jugador.move(60, 270)

        self.enemigo = QLabel(self)
        self.enemigo.setFixedSize(91.75 * 1.1, 187.5 * 1.1)
        self.enemigo.setPixmap(QPixmap(self.rutas['enemigo']))
        self.enemigo.setScaledContents(True)

        self.enemigo.move(540, 270)

        # ---- Definicion de los controles inferiores ----
        # Contenedor horizontal de los controles
        contenedor_controles = QHBoxLayout()
        # Agregamos los botones al layout
        contenedor_controles.addWidget(self.boton_patada)
        contenedor_controles.addWidget(self.boton_frio)
        contenedor_controles.addWidget(self.boton_defender)
        # Definimos el estilo de los botones
        self.boton_patada.setStyleSheet(self.estilo_botones)
        self.boton_frio.setStyleSheet(self.estilo_botones)
        self.boton_defender.setStyleSheet(self.estilo_botones)
        # Apretamos los botones hacia la izquierda y agregamos el contenedor a la ventana principal
        contenedor_controles.addStretch()
        self.layout_principal.addLayout(contenedor_controles)
        # Llamamos al método que tienen que implementar
        self.conectar_botones()
        self.repaint()

    def recibir_comando_actualizacion(self, data):
        """
        Este método recibe señales del back-end contendiendo un diccionario y llama a los métodos
        correspondientes
        """
        comando = data["comando"]
        if comando == "dano_enemigo":
            self.enemigo_golpeado(data["valor"])
        elif comando == "preparar_enemigo":
            self.enemigo_prepara()
        elif comando == "dano_jugador":
            self.jugador_golpeado(data["valor"])
        elif comando == "defender":
            self.cambiar_estado_defensa(data["valor"])
        elif comando == "ganar":
            self.terminar_combate(True)
        elif comando == "perder":
            self.terminar_combate(False)

    # -------------- PENDIENTE COMENTAR Y ORDENAR ------------------
    def combatir(self, nombre, personaje):
        self.senal_envio_info_backend.emit("iniciar")
        self.label_nombre.setText(nombre)
        self.label_icono.setPixmap(QPixmap(self.rutas_iconos[personaje]))
        self.label_icono.setMaximumSize(40, 40)
        self.label_icono.setScaledContents(True)
        self.show()

    def terminar_combate(self, resultado):
        self.hide()
        self.senal_abrir_ventana_final.emit(resultado)

    def frio(self):
        if self.en_accion:
            return
        self.en_accion = True
        # Mover jugador
        paso = (self.enemigo.x() - self.jugador.x() - 165) / 10
        for _ in range(10):
            self.jugador.move(self.jugador.x() + paso, self.jugador.y())
            self.sleep(0.03)
        gif_frio = QMovie(self.rutas["frio"])
        gif_frio.setSpeed(110)
        self.jugador.setMovie(gif_frio)
        gif_frio.start()
        self.jugador.setFixedSize(207 * 1.3, 145 * 1.43)
        self.sleep(1.18)
        self.jugador.setFixedSize(91.75 * 1.1, 187.5 * 1.1)
        self.jugador.setMovie(self.gif_jugador)
        for _ in range(10):
            self.jugador.move(self.jugador.x() - paso, self.jugador.y())
            self.sleep(0.03)
        # Fin Movida
        self.en_accion = False

        self.senal_envio_info_backend.emit("frio")

    def patear(self):
        if self.en_accion:
            return
        self.en_accion = True
        # Mover jugador
        paso = (self.enemigo.x() - self.jugador.x() - 140) / 10
        for _ in range(10):
            self.jugador.move(self.jugador.x() + paso, self.jugador.y())
            self.sleep(0.03)
        self.jugador.setPixmap(QPixmap(self.rutas["patada"]))
        self.jugador.setFixedSize(143 * 1.4, 137 * 1.4)
        # Shake
        sg = 1
        for _ in range(10):
            self.jugador.move(self.jugador.x() + sg, self.jugador.y() + sg)
            sg *= -1
            self.sleep(0.03)
        self.senal_envio_info_backend.emit("patada")
        self.jugador.setFixedSize(91.75 * 1.1, 187.5 * 1.1)
        self.jugador.setMovie(self.gif_jugador)
        for _ in range(10):
            self.jugador.move(self.jugador.x() - paso, self.jugador.y())
            self.sleep(0.03)
        # Fin Movida
        self.en_accion = False

    def enemigo_golpeado(self, vida):
        self.barra_vida_enemigo.setValue(vida)

    def enemigo_prepara(self):
        self.enemigo.setPixmap(QPixmap(self.rutas["enemigo_prepara"]))
        self.enemigo.setFixedSize(174 * 0.9, 193 * 0.9)
        self.enemigo.move(self.enemigo.x(), self.enemigo.y() + 20)
        self.timer = QTimer()
        self.timer.singleShot(1900, self.enemigo_deja_preparacion)

    def enemigo_deja_preparacion(self):
        self.enemigo.move(self.enemigo.x(), self.enemigo.y() - 20)
        self.enemigo.setPixmap(QPixmap(self.rutas['enemigo']))
        self.enemigo.setFixedSize(91.75 * 1.1, 187.5 * 1.1)

    def jugador_golpeado(self, vida):
        # Movimiento
        paso = (self.enemigo.x() - self.jugador.x() - 300) / 5
        for _ in range(5):
            self.enemigo.move(self.enemigo.x() - paso, self.enemigo.y())
            self.sleep(0.04)
        # Animacion
        gif_combo = QMovie(self.rutas["enemigo_golpea"])
        gif_combo.setSpeed(200)
        self.enemigo.setMovie(gif_combo)
        self.enemigo.setFixedSize(256*1.8, 188*1.8)
        self.enemigo.move(self.enemigo.x() - 300, self.enemigo.y() - 100)
        gif_combo.start()
        self.sleep(2.2)
        self.enemigo.move(self.enemigo.x() + 300, self.enemigo.y() + 100)
        self.enemigo.setPixmap(QPixmap(self.rutas['enemigo']))
        self.enemigo.setFixedSize(91.75 * 1.1, 187.5 * 1.1)
        self.barra_vida_jugador.setValue(vida)
        # Vuelta
        for _ in range(5):
            self.enemigo.move(self.enemigo.x() + paso, self.enemigo.y())
            self.sleep(0.02)

    def método_defender(self):
        if self.en_accion:
            return
        self.senal_envio_info_backend.emit("defender")

    def sleep(self, secs):
        loop = QEventLoop()
        QTimer.singleShot(secs * 1000, loop.quit)
        loop.exec_()
