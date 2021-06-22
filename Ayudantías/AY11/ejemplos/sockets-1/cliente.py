import socket

# sock será nuestro socket instanciado. Usará dirección de tipo ipv4 y será TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtenemos la dirección de ip del computador y definimos un puerto de forma arbitraria.
# En este ejemplo, el socket servidor estará en el mismo computador, por eso obtenemos la dirección de esta forma.
# si el servidor está en otro computador, tendríamos que poner su ip correspondiente.
HOST = socket.gethostname()
PORT = 5000

# Ahora intentamos conectarnos a nuestro servidor
# Utilizamos un try porque cuando no se logra la conexión, se levanta una excepción.
try:
    # Con connect intentamos establecer la conexión con otro socket que esté escuchando la dirección y puerto dado.
    sock.connect((HOST, PORT))  # OJO: se tiene que entregar una tupla con los parámetros!

    sock.send('Mensaje bien bacan'.encode())
    # Alternativamente:
    # sock.send(b'Mensaje bien bacan')
    # en general es bueno hacer un protocolo personalizado de comunicación

except ConnectionError as error:
    # Cuando entramos acá, es porque no había un socket escuchando en la dirección dada, o se desconectó en el proceso.
    print('La conexión falló :O')
    print(error)
finally:
    # Dejamos un finally para cerrar el socket, haya error o no. Esto siempre es deseable, como cerrar un archivo!
    sock.close()
