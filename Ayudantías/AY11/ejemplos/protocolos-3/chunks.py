# Los mensajes de este ejemplo serán relativamente cortos
# por lo que usaremos chunks bastante pequeños.

mensaje = """Hola soy un mensaje! Porfavor recíbeme correctamente uwu. 
En caso de que ocurra un error explotaré!"""

# Un mensaje tan delicado debe ser manejado con completo cuidado!

# Para propósitos del ejemplo, crearemos una clase que recibe el mensaje
# Como protocolo definimos chunks de tamaño 5.
# Además, cada mensaje parte con un header que indica la cantidad de chunks
# El header corresponde a 4 bytes codificada según Big Endian
CHUNK_SIZE = 5


class Remitente:
    def __init__(self):
        self.mensaje_recibido = ""

    def recibir_mensaje(self, nuevo_mensaje):
        chunks_recibidos = []
        n_chunks = int.from_bytes(nuevo_mensaje[:4], "big")
        actual = 4
        while len(chunks_recibidos) < n_chunks:
            chunk = nuevo_mensaje[actual:actual + CHUNK_SIZE]
            print(chunk)
            chunks_recibidos.append(chunk)
            actual += CHUNK_SIZE
        self.completar_menaje(chunks_recibidos)

    def completar_menaje(self, chunks_recibidos):
        mensaje_final = b"".join(chunks_recibidos).strip(b"\x00")
        self.mensaje_recibido = mensaje_final.decode(encoding="UTF-8")
        print("Recibí el siguiente mensaje:\n", self.mensaje_recibido)


# Ahora enviaremos el mensaje. Lo primero que hacemos es convertirlo a bytes!
# Dado que es sólo un string, podemos usar su método "encode".
# Con objetos más complicados debemos usar pickle o json.

bytes_mensaje = mensaje.encode(encoding='UTF-8')

# Queremos que cada chunk del mensaje tenga la misma cantidad de bytes.
# Entonces, agregamos 0s alfinal, hasta que el mensaje sea múltiplo de CHUNK_SIZE
while len(bytes_mensaje) % CHUNK_SIZE != 0:
    bytes_mensaje += b'\x00'

# Luego obtenemos la cantidad de chunks
n_chunks = len(bytes_mensaje) // CHUNK_SIZE

# Ahora debemos convertir esta cantidad a bytes, y agregarlas al inicio del mensaje.
n_chunks_bytes = n_chunks.to_bytes(4, "big")
mensaje_final = n_chunks_bytes + bytes_mensaje
print(mensaje_final)
# luego usamos enviamos el mensaje a la clase!
remitente_object = Remitente()
remitente_object.recibir_mensaje(mensaje_final)


## IMPORTANTE
# Este procedimiento es algo inútil y tedioso cuando trabajamos en un sólo módulo.
# Pero es esencial realizarlo cuando trabajemos con networking.
