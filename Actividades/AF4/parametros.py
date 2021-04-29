from os.path import join


# Rutas de assets
RUTA_LOGO = join("frontend", "assets", "logo.jpg")
RUTA_SELECCION = join("frontend", "assets", "seleccion.png")
RUTAS_VTN_FINAL = {
    "fiesta": join("frontend", "assets", "fiesta.gif"),
    "smoke": join("frontend", "assets", "sad_smoke.gif"),
    "cumbia": join("frontend", "assets", "kumbia.mp3"),
    "sad": join("frontend", "assets", "flauta_sad.mp3")
}
RUTAS_COMBATE = {
    "enemigo": join("frontend", "assets", "jugador.png"),
    "jugador": join("frontend", "assets", "enemigo.gif"),
    "patada": join("frontend", "assets", "patada_alta_nobg.png"),
    "frio": join("frontend", "assets", "frio.gif"),
    "defensa": join("frontend", "assets", "defensa.gif"),
    "enemigo_prepara": join("frontend", "assets", "enemigo_prepara.png"),
    "enemigo_golpea": join("frontend", "assets", "combo.gif"),
    "fondo": join("frontend", "assets", "fondo_carate.jpg")
}
RUTAS_PERSONAJES = [
    join("frontend", "assets", "personaje_1.jpg"),
    join("frontend", "assets", "personaje_2.jpg"),
    join("frontend", "assets", "personaje_3.jpg"),
    join("frontend", "assets", "personaje_4.jpg"),
    join("frontend", "assets", "personaje_5.jpg"),
    join("frontend", "assets", "personaje_6.jpg"),
    join("frontend", "assets", "personaje_7.jpg"),
    join("frontend", "assets", "personaje_8.jpg"),
    join("frontend", "assets", "personaje_9.jpg"),
    join("frontend", "assets", "personaje_10.jpg"),
    join("frontend", "assets", "personaje_11.jpg"),
    join("frontend", "assets", "personaje_12.jpg"),
]

# Arreglos adicionales para front-end
ESTILO_BOTONES = """
    background-color: rgb(175, 53, 55);
    border-style: solid;
    border-width: 2px;
    border-radius: 25px;
    border-color: black;
    max-width: 50px;
    max-height: 50x;
    min-width: 50px;
    min-height: 50px;
"""

# Tamaño de ventanas
ANCHO = 700
ALTO = 500
ANCHO_FINAL = 600
ALTO_FINAL = 400

# Volumen de audio
VOLUMEN = 10
