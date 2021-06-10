import parametros as p
import cargar_archivos as c


class NodoChismoso:

    def __init__(self, nombre, frase):
        # NO MODIFICAR
        self.nombre = nombre
        self.frase = frase
        self.conocido = None


def construir_nodo_chismoso(nombre, diccionario_mafiosos):
    # NO MODIFICAR
    if not nombre:
        return None

    print(f"El nombre es {nombre}")
    nombre_siguiente, frase = diccionario_mafiosos[nombre]
    nodo = NodoChismoso(nombre, frase)
    nodo_siguiente = construir_nodo_chismoso(nombre_siguiente, diccionario_mafiosos)
    nodo.conocido = nodo_siguiente
    return nodo


def encontrar_secretario(nodo):
    # Recorre la lista ligada hasta encontrar el secretario
    # COMPLETAR
    pass


if __name__ == "__main__":
    # Puedes probar tu avance ejecutando este módulo
    diccionario_mafiosos, nombre_cabeza = c.cargar_mafiosos(p.path_mafioso)
    print("\n-> Identificando mafiosos...")
    cabeza = construir_nodo_chismoso(nombre_cabeza, diccionario_mafiosos)
    print("\n-> Buscando al secretario...")
    secretario = encontrar_secretario(cabeza)

    if secretario is not None:
        print(f"\nHaz atrapado al secretario!! Era {secretario.nombre}")
        print("Es hora de -t̶o̶r̶t̶u̶r̶a̶r̶l̶o̶- incentivarlo a" +
              " darnos el mapa de la organización\n")
    else:
        print(f"No haz logrado encontrar al secretario aún\n")
