# No modificar este archivo

from entidades import Mascota, Comida
from parametros import RUTA_ANIMALES, RUTA_COMIDAS


def cargar_mascotas(ruta):
    with open(ruta, 'r', encoding='utf-8') as file:
        for row in file:
            if row.split(';')[0] != 'nombre':
                datos = row.strip().split(';')
                nombre = datos[0]
                especie = datos[1]
                raza = datos[2]
                edad = int(datos[3])
                estatura = float(datos[4])
                precio = int(datos[5])
                yield Mascota(nombre, especie, raza, edad, estatura, precio)


def cargar_comidas(ruta):
    with open(ruta, 'r', encoding='utf-8') as file:
        for row in file:
            if row.split(';')[0] != 'nombre':
                datos = row.strip().split(';')
                nombre = datos[0]
                especie = datos[1]
                raza = datos[2]
                precio = int(datos[3])
                # si disponible == "True" entonces disponible será igual a True
                # en caso contrario, disponible será igual a False
                disponible = (datos[4] == "True")
                yield Comida(nombre, especie, raza, precio, disponible)


if __name__ == '__main__':
    generador_mascotas = cargar_mascotas(RUTA_ANIMALES)
    generador_comidas = cargar_comidas(RUTA_COMIDAS)
    for mascota in generador_mascotas:
        print(mascota.nombre)
    for comida in generador_comidas:
        print(comida.nombre)
