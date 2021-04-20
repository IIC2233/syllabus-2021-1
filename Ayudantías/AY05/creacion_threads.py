import threading
from time import sleep

#######################
# AYUDANTÍA THREADING #
#######################

##################################
# Nuestros programas hasta ahora #
##################################

# print("\n")
# print("Zoom - Chatear".center(30))
# print("-- Bienvenidos a la ayudantía --\n")
# mensaje = input("Escribir mensaje aquí: ")
# print("Pedro:", mensaje, "\n")

###################
# Creando Threads #
###################


def mi_primer_thread(nombre):
    sleep(5)
    print("\n")
    print(f"Hola, soy {nombre} y este es mi primer Thread\n")

# 1 - Importar la librería "threading"
# 2 - Crear el Thread
# 3 - Iniciarlo


# mi_thread = threading.Thread(target=mi_primer_thread, kwargs={"nombre": "Pedro"})


# mi_thread.start()

#######################
# Thread como clases  #
#######################

# print(type(5))
# 1 - Heredar de Thread
# 2 - Sobreescribir el método RUN
# Crear y ejecutar

class Ayudante(threading.Thread):

    def __init__(self, nombre, edad):
        super().__init__()
        self.nombre = nombre
        self.edad = edad
        # self.daemon = True

    def run(self):
        #sleep(3)
        print(f"Hola, soy {self.nombre} y este es mi Thread en una clase")
        print(f"Además, tengo {self.edad} años")


# mi_thread_clase = Ayudante("Pedro", 20)
# mi_thread_clase.start()

for i in range(4):
    print("Este es el Thread Principal")

###############
# Uso de JOIN #
###############
