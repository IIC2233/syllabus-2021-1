from personas import Cliente, Trabajador
from locales import Entretenimiento, Comida, Tienda, Casino, Supermercado


def cargar_locales(ruta_locales, ruta_trabajadores):
    dict_locales = {}
    lista_trabajadores = cargar_trabajadores(ruta_trabajadores)
    clases_locales = {
        "entretenimiento": Entretenimiento,
        "comida": Comida,
        "tienda": Tienda,
        "casino": Casino,
        "supermercado": Supermercado
    }
    with open(ruta_locales, "r", encoding="UTF-8") as archivo:
        datos_locales = archivo.readlines()
        for fila in datos_locales[1:]:
            fila = fila.strip().split(",")
            lista_productos = fila[-1].split("-")
            dict_productos = {}
            for producto in lista_productos:
                llave, valor = producto.split(":")
                dict_productos[llave] = int(valor)
            for trabajador in lista_trabajadores:
                if trabajador.nombre_local == fila[1]:
                    nuevo_trabajador = trabajador
            nuevo_local = clases_locales[fila[0]](
                dict_productos, fila[1], int(fila[2]), nuevo_trabajador,
            )
            dict_locales[nuevo_local.nombre] = nuevo_local
    return dict_locales


def cargar_clientes(ruta_clientes):
    lista_clientes = []
    with open(ruta_clientes, "r", encoding="UTF-8") as archivo:
        datos_clientes = archivo.readlines()
        for fila in datos_clientes[1:]:
            fila = fila.strip().split(",")
            nuevo_cliente = Cliente(fila[0], int(fila[1]), bool(
                int(fila[2])), fila[3], int(fila[4]))
            lista_clientes.append(nuevo_cliente)
    return lista_clientes


def cargar_trabajadores(ruta):
    lista_trabajadores = []
    with open(ruta, "r", encoding="UTF-8") as archivo:
        datos_trabajadores = archivo.readlines()
        for fila in datos_trabajadores[1:]:
            fila = fila.strip().split(",")
            trabajador = Trabajador(
                fila[0], int(fila[1]), bool(int(fila[2])), int(fila[3]), fila[4],
            )
            lista_trabajadores.append(trabajador)
    return lista_trabajadores
