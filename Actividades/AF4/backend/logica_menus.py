from PyQt5.QtCore import QObject, pyqtSignal, QTimer


class LogicaInicio(QObject):
    """
    Lógica back-end utilizada en la ventana de inicio
    """
    senal_respuesta_validacion = pyqtSignal(bool)  # Envía al front-end si el nombre es valido

    def __init__(self):
        # NO MODIFICAR
        super().__init__()

    def comprobar_nombre(self, nombre):
        # NO MODIFICAR
        if nombre.isalnum():
            self.senal_respuesta_validacion.emit(True)
        else:
            self.senal_respuesta_validacion.emit(False)


class LogicaCombate(QObject):
    """
    Lógica back-end utilizada en la ventana de combate
    """
    senal_enviar_actualizacion = pyqtSignal(dict)  # Envía informacion a la ventana de combate

    def __init__(self):
        # NO MODIFICAR
        super().__init__()
        self.vida_jugador = 100
        self.vida_enemigo = 100
        self.jugador_defendiendo = False
        self.timer = QTimer(self)
        self.tick_actual = 0
        self.timer.timeout.connect(self.timer_tick)

    def golpear_jugador(self):
        # COMPLETAR
        pass

    # ----------------------------------------------------------------
    # -------------------- NO MODIFICAR DESDE ACA --------------------
    # ----------------------------------------------------------------
    def recibir_senal(self, comando):
        if comando == "iniciar":
            self.iniciar_combate()
        elif comando in ["frio", "patada"]:
            self.golpear_enemigo(comando)
        elif comando == "defender":
            self.defender()

    def iniciar_combate(self):
        self.timer.start(2000)

    def detener_combate(self):
        self.timer.stop()

    def timer_tick(self):
        self.tick_actual += 1
        if self.tick_actual == 2:
            self.senal_enviar_actualizacion.emit({
                "comando": "preparar_enemigo",
            })
        elif self.tick_actual >= 3:
            self.tick_actual = 0
            self.golpear_jugador()

    def golpear_enemigo(self, tipo):
        if tipo == "frio":
            self.vida_enemigo -= 10
        elif tipo == "patada":
            self.vida_enemigo -= 15

        if self.vida_enemigo > 0:
            self.senal_enviar_actualizacion.emit({
                "comando": "dano_enemigo",
                "valor": self.vida_enemigo,
            })
        else:
            self.timer.stop()
            self.senal_enviar_actualizacion.emit({
                "comando": "ganar",
            })

    def defender(self):
        self.jugador_defendiendo = not self.jugador_defendiendo
        self.senal_enviar_actualizacion.emit({
            "comando": "defender",
            "valor": self.jugador_defendiendo,
        })
