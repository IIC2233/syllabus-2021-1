from threading import Thread, Lock, Timer
import random
import time

author_2017 = "Joaquin"
modificadores = ("Julio", "Belen", "Pedro")


class Actividad(Thread):

    def __init__(self, ayudantes, max_time):
        # Completar
        self.contador_alumnos = 0

    def spawn_alumnos(self):
        while self.contador_alumnos < 30:
            time.sleep(random.expovariate(0.5))  # ! expovariate es un proceso poisson
            alumno = Alumno(self.ayudantes)   # ? crea los threads
            alumno.start()
            self.contador_alumnos += 1

    def aviso_commit(self):
        print("\n\nPROGRABOT: ¡¡¡ QUEDAN 5 MINUTOS, REALIZEN SUS ADD, COMMIT, PUSH !!! \n\n")

    def run(self):
        # Completar
        pass


class Alumno(Thread):
    names = ("Cristian", "Coti", "Joaquín", "Antonio", "Daniela", "Francisca", "Diego")
    contador_dudas = 0

    def __init__(self, ayudantes):
        # Completar

        self.dudas = ("git", "properties", "threads", "locks", "daemons")
        self.duda_actual = None

    def dudar_sobre_algo(self):
        self.duda = random.choice(self.dudas)
        self.duda_actual = self.contador_dudas
        Alumno.contador_dudas += 1

    def run(self):
        # Completar
        pass


class Ayudante:
    # Representa a un Lock

    def __init__(self, nombre, lentitud):
        self.lentitud = lentitud  # ? lentitud con la que ayuda
        self.nombre = nombre
        self.disponibilidad = Lock()  # ! IMPORTANTE

    def ayudar_alumno(self, alumno):
        print(f"Duda {alumno.duda_actual}: {self.nombre} resolviendo las consultas de " +
              f"{alumno.nombre} sobre {alumno.duda} \n")
        time.sleep(self.lentitud)


if __name__ == "__main__":
    print("*************¡BIENVENIDOS A LA ACTIVIDAD SUMATIVA!******************\n\n")
    ayudantes = [Ayudante("Julio", 6), Ayudante("Belen", 4), Ayudante("Pedro", 3),
                 Ayudante("Ian", 1), Ayudante("Caua", 2)]

    sumativa = Actividad(ayudantes, 20)
    sumativa.start()
    sumativa.join()
