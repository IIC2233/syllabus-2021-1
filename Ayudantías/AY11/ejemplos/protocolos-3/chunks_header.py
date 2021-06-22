import json

# Queremos poder enviar mensajes más complejos, aplicando lo que sabemos de chunks y headers.
HEADER_SIZE = 8
CHUNK_SIZE = 10

# Supongamos la siguiente "base de datos"
json_data = {"MP3": {"Baby Shark": {"NOMBRE": "Baby Shark",
                                    "MUSICA": "du duru duru durú"},
                     "Safaera": {"NOMBRE": "Safaera",
                                 "MUSICA": "Aqui llegó tu tiburón"}
                     },
             "MEME": {"original_meme": {
                 "IMAGEN": "HACKERMAN",
                 "TOP TEXT": "Cuando tienes que inventar un meme para la ayudantía",
                 "BOTTOM TEXT": "bottom text"}}
             }

# Definimos dos funciones para los dos tipos de archivo que tiene nuestra base de datos
def leer_meme(meme):
    print(f"""Recibí un meme!
            {meme["TOP TEXT"]}
            {meme["IMAGEN"]}
            {meme["BOTTOM TEXT"]}
          """)

def leer_cancion(cancion):
    print("recibí una canción!")
    print(f"Ahora escucharemos {cancion['NOMBRE']}:")
    print(cancion["MUSICA"])


# Definiremos una clase que recibe un archivo,
# y realiza una accion sobre el dependiendo de su contenido
class Reader:
    def __init__(self):
        print("estoy esperando que me envíen datos!")

    def recibir_mensaje(self, data_):
        header = data_[:HEADER_SIZE].strip(b'\x00')
        n_chunks = int.from_bytes(header[:4], "little")
        formato = header[4:].decode('utf-8')
        chunks_recibidos = []
        pos_actual = HEADER_SIZE
        while len(chunks_recibidos) < n_chunks:
            chunk = data_[pos_actual:pos_actual + CHUNK_SIZE]
            chunks_recibidos.append(chunk)
            pos_actual += CHUNK_SIZE
        mensaje = b"".join(chunks_recibidos).strip(b"\x00")
        self.leer_mensaje(mensaje, formato)

    def leer_mensaje(self, mensaje_json, formato):
        mensaje = json.loads(mensaje_json, encoding='utf-8')
        if formato == 'MEME':
            leer_meme(mensaje)
        elif formato == 'MP3':
            leer_cancion(mensaje)
        else:
            # Lanzamos una excepción si la información no es legible
            print("formato:", formato)
            raise ValueError("No sé que hacer con esta información unu")


# Ahora creamos una funcion que recibe la información, y la codifica correctamente
def codificar(formato, data_):
    info_codificada = json.dumps(data_).encode(encoding='utf-8')
    while len(info_codificada) % CHUNK_SIZE != 0:
        info_codificada += b'\x00'

    n_chunks = len(info_codificada) // CHUNK_SIZE
    header = n_chunks.to_bytes(4, "little") + formato.encode('utf-8')
    while len(header) % HEADER_SIZE != 0:
        header += b'\x00'
    return header + info_codificada

# Probemos nuestro código!
server_ficticio = Reader()
mensaje1 = codificar("MP3", json_data["MP3"]["Baby Shark"])
mensaje2 = codificar("MEME", json_data["MEME"]["original_meme"])
server_ficticio.recibir_mensaje(mensaje1)
server_ficticio.recibir_mensaje(mensaje2)

