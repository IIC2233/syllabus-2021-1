from abc import ABC, abstractmethod
import random


# Completar
class Persona:

    def __init__(self, nombre, edad, contagiado):
        # No modificar
        self.nombre = nombre
        self.edad = edad
        self.contagiado = contagiado

    def saludar(self):
        pass


# Completar
class Cliente:

    def __init__(self, nombre, edad, contagiado, nombre_local_favorito, dinero):
        # Completar
        pass

    def saludar(self):
        # No modificar
        print(f"Hola me llamo {self.nombre} y mi local favorito es {self.nombre_local_favorito}")


# Completar
class Trabajador:

    def __init__(self, nombre, edad, contagiado, sueldo, nombre_local):
        # Completar
        pass

    def generar_posible_contagio(self):
        # No modificar
        probabilidad_contagio = random.uniform(0, 1)
        if probabilidad_contagio < 0.1:
            self.contagiado = True

    def saludar(self):
        # No modificar
        print((
            f"Hola me llamo {self.nombre}, trabajo en {self.nombre_local}"
            f" y mi sueldo es {self.sueldo}"
        ))
