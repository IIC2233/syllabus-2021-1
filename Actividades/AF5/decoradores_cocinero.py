from funciones import encontrar_preferencia, log


# Debes completar este archivo

def improvisar_toppings(metodo_original):
    """
    Este decorador se encarga de escoger un topping nuevo en caso de que no quede del
    que pide el método original
    """
    pass


def capa_relleno(tipo_relleno):
    def decorador(metodo_original):
        """
        Este decorador chequea que quede del relleno pedido, si los hay, lo agrega,
        si no, termina la torta
        """
        pass

    return decorador


def revisar_ingredientes(metodo_original):
    """
    Este decorador revisa que hayan suficientes ingredientes antes de empezar una torta.
    En caso contrario, debe levantar una excepción del tipo ValueError
    """
    pass
