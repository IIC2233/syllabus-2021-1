from emergencias import Incendio, Choque
from random import shuffle, randint
from time import sleep
from parametros import PATH_CSV


class DCCatastrofe:
    def __init__(self, path_archivo):
        self.emergencias = []
        self.path_archivo = path_archivo
    # Método que carga archivo .txt (ya implementado). Retorna lista de listas de emergencias
    # tipo [["incendio", "ha ocurrido un..."], ["choque", "alguien ha interceptado..."]]

    # NO MODIFICAR
    def cargar_emergencias(self):
        with open(self.path_archivo, encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            emergencias = [linea.strip().split(",") for linea in lineas]
            emergencias = [(linea[0], linea[1]) for linea in emergencias]
            shuffle(emergencias)
            return emergencias

    # Método a completar, inicia simulación
    def iniciar_simulacion(self):
        # Completar





        print('Felicidades! No han habido' + ' ̶-h̶e̶r̶i̶d̶o̶s̶ ̶g̶r̶a̶v̶e̶s̶  ' + 'muertos!')


if __name__ == "__main__":
    central = DCCatastrofe(PATH_CSV)
    central.iniciar_simulacion()
