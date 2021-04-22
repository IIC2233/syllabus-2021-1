from time import sleep
from threading import Thread
from random import randint
from companias import CompaniaServicio
from parametros import RECURSOS_MAX


# Completar
class Emergencia:

    companias = {"agua": CompaniaServicio("agua", RECURSOS_MAX),
                 "banditas": CompaniaServicio("banditas", RECURSOS_MAX),
                 "donas": CompaniaServicio("donas", RECURSOS_MAX)}

    def __init__(self) -> None:
        # Completar
        pass


# Completar
class Incendio:

    def __init__(self) -> None:
        pass

    def run(self) -> None:

        # Inicia el incendio
        print(f"Inicio de catastrofe N°{self.numero_catastrofe}:")
        print(f"{self.aviso}\n")

        # NO MODIFICAR
        agua_necesaria, banditas_necesarias = 100 * self.gravedad, 2 * self.gravedad
        agua, banditas = Emergencia.companias["agua"], Emergencia.companias["banditas"]

        # Completar




        print(f"Fin de catastrofe N°{self.numero_catastrofe}\n")

    def llamar_bomberos(self) -> None:
        # Completar
        pass


# Completar
class Choque:

    def __init__(self) -> None:
        pass

    def run(self) -> None:

        # Inicia el choque
        print(f"Inicio de catastrofe N°{self.numero_catastrofe}:")
        print(f"{self.aviso}\n")

        # NO MODIFICAR
        donas_necesarias, banditas_necesarias = 3 * self.gravedad, 2 * self.gravedad
        donas, banditas = Emergencia.companias["donas"], Emergencia.companias["banditas"]

        # Completar






        print(f"Fin de catastrofe N°{self.numero_catastrofe}\n")

    def atender_heridos(self) -> None:
        # Completar
        pass


if __name__ == "__main__":
    incendio_1 = Incendio(aviso="Incendio intencial de prueba, que podria salir mal...\n", 
                         numero_catastrofe=1)
    incendio_2 = Incendio(aviso="Incendio de prueba a la facultad de matematicas \n", 
                         numero_catastrofe=2)

    choque_1 = Choque(aviso="Choque de prueba, abrochence los cinturones !!! \n",
                     numero_catastrofe=3)
    choque_2 = Choque(aviso="Chocare el primer poste que vea >:( \n", 
                     numero_catastrofe=4)

    incendio_1.start()
    incendio_2.start()
    choque_1.start()
    choque_2.start()
