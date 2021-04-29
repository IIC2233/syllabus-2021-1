import sys
from PyQt5.QtWidgets import QApplication
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_seleccion import VentanaSeleccion
from frontend.ventana_combate import VentanaCombate
from frontend.ventana_final import VentanaFinal

from backend.logica_menus import LogicaInicio, LogicaCombate

import parametros as p


def hook(type_error, traceback):
    print(type_error)
    print(traceback)


if __name__ == '__main__':
    # Inicialización de la aplicación
    sys.__excepthook__ = hook
    app = QApplication(sys.argv)

    # Ventana y lógica de inicio
    ventana_inicio = VentanaInicio(p.ANCHO, p.ALTO, p.RUTA_LOGO)
    logica_inicio = LogicaInicio()
    # Conexion señal para validar nombre
    ventana_inicio.senal_elegir_nombre.connect(logica_inicio.comprobar_nombre)
    logica_inicio.senal_respuesta_validacion.connect(ventana_inicio.recibir_validacion)
    # Mostrar ventana de inicio
    ventana_inicio.show()

    # Ventana de selección
    ventana_seleccion = VentanaSeleccion(
        p.ANCHO, p.ALTO, p.RUTAS_PERSONAJES, p.RUTA_SELECCION,
    )
    # Conexión señal para abrir ventana
    ventana_inicio.senal_abrir_eleccion_personaje.connect(ventana_seleccion.abrir_ventana)

    # Ventana y lógica de combate
    ventana_combate = VentanaCombate(
        p.ANCHO, p.ALTO, p.RUTAS_COMBATE, p.RUTAS_PERSONAJES, p.ESTILO_BOTONES,
    )
    logica_combate = LogicaCombate()
    # ----------------------------
    # CONECTA LA SEÑAL PEDIDA EN LA PARTE 2 AQUI

    # ----------------------------
    # Conexión señales adicionales al combatir 
    logica_combate.senal_enviar_actualizacion.connect(ventana_combate.recibir_comando_actualizacion)
    ventana_combate.senal_envio_info_backend.connect(logica_combate.recibir_senal)

    # Ventana final
    ventana_final = VentanaFinal(
        p.ANCHO_FINAL, p.ALTO_FINAL, p.VOLUMEN, *p.RUTAS_VTN_FINAL.values(),
    )
    # Conexión señal para abrir ventana
    ventana_combate.senal_abrir_ventana_final.connect(ventana_final.mostrar_final)

    sys.exit(app.exec())
