"""
Archivo de parámetros para la interfaz gráfica
"""
import os

DIMENSIONES_VENTANA = (300, 100, 500, 600)
MAX_SIZE_IMAGE = (500, 500)
RUTA_IMAGEN = os.path.join("frontend", "image.bmp")
RUTA_IMAGEN_TEST = os.path.join("testimage.bmp")
RUTA_RR_GIVE_UP = os.path.join(".rrdata", "updata.rr")
RUTA_RR_LET_DOWN = os.path.join(".rrdata", "downdata.rr")

# Filter parameters

MINIMALISM_THRESHOLD = 384
CENSOR_MUTIPLIER = 2.1
ALPHA_PUSH_VALUE = 120
