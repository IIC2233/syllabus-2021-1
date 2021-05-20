from decoradores_cocina import desencriptar_receta, encriptar_receta, ingredientes_infectados
from decoradores_cocinero import improvisar_toppings, capa_relleno, revisar_ingredientes
import parametros as p
from funciones import log, recibir_input, preguntar_rellenos
from random import choice


class DCCocina:
    def __init__(self):
        log('Activando Cocina')
        self.tortas = []
        self.recetas = self.leer_recetas(p.ARCHIVO_RECETAS)
        ingredientes = self.revisar_despensa(p.ARCHIVO_INGREDIENTES)
        self.chef = DCChef(ingredientes)

    def leer_recetas(self, archivo):
        """
        Método que lee el archivo recetas y lo transforma en un diccionario, el cual retorna
        :param archivo: nombre del archivo (parámetro)
        :return: diccionario de recetas
        """
        with open(archivo, "r", encoding="utf-8") as archivo_recetas:
            lista_recetas = [linea.strip().split(",") for linea in archivo_recetas.readlines()[1:]]

        return {linea[0]: linea[1:] for linea in lista_recetas}

    def revisar_despensa(self, archivo: str):
        """
        Lee el archivo ingredientes y los guarda en un diccionario
        :param archivo: nombre del archivo
        :return: diccionario de ingredientes
        """
        log('Revisando Despensa')
        with open(archivo, "r", encoding="utf-8") as archivo_ingredientes:
            lista_ingredientes = [item.strip().split(',')
                                  for item in archivo_ingredientes.readlines()]

        return {ing: int(cantidad) for ing, cantidad in lista_ingredientes}

    def escribir_receta(self, receta):
        """
        Guarda en el csv de recetas nuevas la receta recibida
        :param receta: lista de ingredientes
        :return: None
        """
        with open(p.ARCHIVO_NUEVAS_RECETAS, "a", encoding='utf-8') as archivo:
            archivo.write(f"{receta},{','.join(receta[1::2])}\n")

    def simular_cocina(self):
        """
        Método central donde se desarrolla el flujo de la actividad
        """
        nombres_receta = list(self.recetas.keys())
        cocinando = True

        while cocinando:
            print("Escoge una torta para cocinar!")
            self.print_seleccion(nombres_receta)
            nombre_receta = recibir_input([p.PALABRA_TERMINAR] + nombres_receta)

            if nombre_receta == p.PALABRA_TERMINAR:
                cocinando = False
            else:
                try:
                    torta = self.chef.cocinar_torta(nombre_receta, self.recetas[nombre_receta])
                except ValueError:
                    log('¡Se nos acabaron los ingredientes! Es hora de presentar las tortas.')
                    cocinando = False
                else:
                    log(f'Se ha cocinado la torta {torta}!!')
                    log(f'Quedan {self.chef.relleno_restante} capas de {self.chef.tipo_relleno}')
                    self.tortas.append(torta)

            if self.chef.relleno_restante <= 0:
                log("¡Se nos acabó el relleno! Es hora de presentar las tortas.")
                cocinando = False

        if len(self.tortas) > 0:
            print('En esta instancia de Hells DCCocina, '
                  'hemos logrado cocinar las siguientes tortas:')
            for torta in self.tortas:
                self.escribir_receta(torta)
                print(f" -{torta}")
        else:
            print("No se ha cocinado ninguna torta en esta ocación :(")

    @staticmethod
    def print_seleccion(nombres_receta):
        nro_torta = 1
        columna = 0
        for torta in nombres_receta:
            print(f"{'[' + str(nro_torta) + ']:': >5s} {torta: ^45.45s}  ", end='')
            columna += 1
            if columna == 3:
                columna = 0
                print()
            nro_torta += 1
        print(f"\n[0]: {p.PALABRA_TERMINAR}")


class Torta(list):
    # Como lista representa los ingredientes agregados
    def __init__(self, name, *args):
        super().__init__(*args)
        self.finalizada = False
        self.name = name

    def __str__(self):
        return self.name


class DCChef:
    tipo_relleno = preguntar_rellenos()

    def __init__(self, ingredientes_disponibles):
        self.ingredientes_disponibles = ingredientes_disponibles
        self.relleno_restante = p.CANTIDAD_RELLENO

    def __str__(self):
        return "DCChef"

    def agregar_topping(self, nombre_ingrediente, torta):
        """
        Método que recibe un ingrediente, y lo agrega al final de la torta
        :param nombre_ingrediente: string que representa un ingrediente
        :param torta: objeto Torta
        :return: None
        """
        if self.ingredientes_disponibles[nombre_ingrediente] > 0:
            torta.append(nombre_ingrediente)
            self.ingredientes_disponibles[nombre_ingrediente] -= 1
            log(f"Agregando {nombre_ingrediente} a torta.", 'ingrediente')
        else:
            torta.finalizada = True
            log(f"No queda suficiente {nombre_ingrediente}. Se procederá a terminar la torta.")

    def cocinar_torta(self, name, receta):
        """
        Método que instancia una Torta e itera sobre los ingredientes de la receta
        con "agregar_topping" hasta cocinar la torta, o que se acaben los ingredientes.
        :param name: Nombre de la torta
        :param receta: lista de ingredientes en forma de strings
        :return: objeto torta
        """
        log(f"Comencemos a cocinar la {choice(('exquisita', 'famosa', 'sublime'))} torta {name}")
        torta = Torta(name)
        iterador_ingredientes = iter(receta)
        current_iter = 0
        while not torta.finalizada:
            if current_iter < len(receta):
                ingrediente = next(iterador_ingredientes)
                self.agregar_topping(ingrediente, torta)
                current_iter += 1
            else:
                torta.finalizada = True

        return torta
