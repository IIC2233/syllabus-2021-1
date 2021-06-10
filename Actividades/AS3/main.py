import parametros as p
from cargar_archivos import cargar_lugares, cargar_mafiosos
from nodo_chismoso import construir_nodo_chismoso, encontrar_secretario
from nodo_lugar import crear_grafo
from recorrido_mafia import recorrer_mafia, minima_peligrosidad


if __name__ == "__main__":

    # Parte 1
    diccionario_mafiosos, nombre_cabeza = cargar_mafiosos(p.path_mafioso)
    print("\n-> Identificando mafiosos...")
    cabeza = construir_nodo_chismoso(nombre_cabeza, diccionario_mafiosos)
    print("\n-> Buscando al secretario...")
    secretario = encontrar_secretario(cabeza)

    if secretario is not None and secretario.frase == p.frase_secretario:
        print(f"\nHaz atrapado al secretario!! Era {secretario.nombre}")
        print("Es hora de -t̶o̶r̶t̶u̶r̶a̶r̶l̶o̶- incentivarlo a" +
              " darnos el mapa de la organización\n")
    else:
        print(f"No haz logrado encontrar al secretario aún\n")

    # Parte 2
    diccionario_lugares, arcos = cargar_lugares(
        p.path_lugares, p.path_conexiones, diccionario_mafiosos
    )
    nodo_inicial = crear_grafo(diccionario_lugares, arcos)
    print("Mapa cargado en forma de grafo!!")
    print("Ahora... a acabar con la mafia!!\n")

    # Parte 3
    lugares_con_lideres = recorrer_mafia(nodo_inicial)
    if lugares_con_lideres and len(lugares_con_lideres):
        nombre_lugares = " y en ".join([nodo_lugar.nombre for nodo_lugar in lugares_con_lideres])
        print("\nFelicitaciones, has logrado desmantelar a la mafia!")
        print(f"Los líderes están en: {nombre_lugares}\n")
        print("¿Será este el fin del DCChisme?\n")
    else:
        print("Aún no encuentras a los líderes\n")

    # Descomenta si deseas hacer el bonus:
    # peligro = minima_peligrosidad(*lugares_con_lideres)
    # print("El camino de menor peligro es de una peligrosidad de:", peligrosidad, "\n")
