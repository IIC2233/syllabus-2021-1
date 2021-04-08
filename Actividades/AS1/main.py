from mall import Mall
from cargar_datos import cargar_locales, cargar_clientes
from parametros import RUTA_CLIENTES, RUTA_LOCALES, RUTA_TRABAJADORES


if __name__ == "__main__":
    # No modificar
    lista_clientes = cargar_clientes(RUTA_CLIENTES)
    dict_locales = cargar_locales(RUTA_LOCALES, RUTA_TRABAJADORES)
    dcostanera_center = Mall(lista_clientes, dict_locales)
    dcostanera_center.iniciar_simulacion()
