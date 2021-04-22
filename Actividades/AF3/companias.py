from threading import Lock


# Maneja los recursos, utiliza un Lock para esto
class CompaniaServicio:

    def __init__(self, tipo, recursos_max):
        self.capacidad_maxima = recursos_max[tipo]
        self.stock = self.capacidad_maxima
        self.disponibilidad = Lock()
        self.tipo = tipo

    def solicitar(self, cantidad):
        if self.stock < cantidad:
            print(f"recargando {self.tipo}... \n")
            self.stock = self.capacidad_maxima

        self.stock -= cantidad
