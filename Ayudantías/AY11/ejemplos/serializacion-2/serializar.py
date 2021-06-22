import pickle
import json


# Crearemos un objeto de python (una clase).
class ObjetoPython:
    def __init__(self, nombre):
        self.nombre = nombre
        print("me están inicializando!")

    def saludar(self):
        print(f"Hola soy: {self.nombre}")

    def renombrar(self, nombre):
        self.nombre = nombre


# Creamos un diccionario utilizando tipos genéricos de python
objeto_generico = {
    'ayudante_1': 'Camila',
    2: 'Thom',
    "3": True,
    "cuatro": [1, 2, 3, 4]
}

objeto_python = ObjetoPython("Zanahoria")

# Hora de serializar!
serializacion_pickle = pickle.dumps(objeto_generico)
serializacion_json = json.dumps(objeto_generico)

# No podemos mezclar serializaciones :O
try:
    print(json.load(serializacion_pickle))
except AttributeError as error:
    print(error)
    print("Tratamos de usar json para deserializar un objeto serializado en pickle!")
print()

# Ahora a deserializar de verdad
print('Objeto: ', objeto_python)
serializacion_objeto = pickle.dumps(objeto_python)
print('Bytes de la serialización: ', serializacion_objeto)
objeto_deserializado = pickle.loads(serializacion_objeto)
print('Objeto: ', objeto_deserializado)
objeto_deserializado.saludar()
# Si nos fijamos, no se imprime la línea en el __init__ "me están inicializando!"
# Esto es por que al deserializar un objeto, se crea la nueva instancia sin llamar al inicializador!
# Podemos comprobar que la instancia que serializamos es distinta a la que recibimos con la
#deserialización:
print(objeto_python is objeto_deserializado)
# En efecto, sus atributos son inicialmente los mismos, pero son objeto independientes:
objeto_deserializado.renombrar("San Ahoria")
objeto_deserializado.saludar()
objeto_python.saludar()

# También podemos serializar clases!
clase_serializada = pickle.dumps(ObjetoPython)

#Al deseriaizar la clase, podemos usar el resultado para crear nuevas instancias:

clase_deserializada = pickle.loads(clase_serializada)
objeto_python_nuevo = clase_deserializada("Carrot")
objeto_python_nuevo.saludar()
print()

# Ahora veamos que pasa si intentamos serializar un objeto de python con JSON
try:
    serializacion_objeto = json.dumps(objeto_python)
except TypeError as error:
    print(error)
    print("json es un protocolo de serialización universal, por lo que no puede trabajar "
          "con instancias especificas a un lenguaje :(")
print()

# Para poder serializar objetos en json, tendríamos que usar un Encoder...