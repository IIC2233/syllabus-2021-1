from funciones import desencriptar, encriptar, log
from random import uniform


def desencriptar_receta(metodo_original):
    """
    Este decorador debe hacer que el método "leer_recetas" retorne las recetas desencriptadas
    """

    def wrapper(*args, **kwargs):
        pass
    return wrapper


def encriptar_receta(metodo_original):
    """
    Este decorador debe hacer que el método "escribir_recetas" encripte las
    recetas antes de escribirlas
    """
    def wrapper(*args):
        pass
    return wrapper


def ingredientes_infectados(probabilidad_infectado):
    def decorador(metodo_original):
        """
        Este decorador debe hacer que el método "revisar_despensa" elmine los ingredientes
        que pueden estar infectados, según la probabilidad dada.
         """
        def wrapper(*args, **kwargs):
            pass
        return wrapper
    return decorador
