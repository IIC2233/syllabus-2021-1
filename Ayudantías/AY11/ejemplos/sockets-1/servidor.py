import socket
# sock será nuestro socket instanciado. Usará dirección de tipo ipv4 y será TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Obtenemos la dirección de ip del computador y definimos un puerto de forma arbitraria.
HOST = socket.gethostname()
PORT = 5000

# Utilizamos bind para determinar la dirección y puerto que el socket estará escuchando
sock.bind((HOST, PORT))  # OJO: se tiene que entregar una tupla con los parámetros!
# Ahora si, le decimos al socket que empieze a escuchar conexiones entrantes
sock.listen()

# Como queremos que el servidor esté constantemente aceptando clientes, utilizamos un loop infinito.
# La forma exacta de como manejar esto se ve en los siguientes ejemplos.
while True:
    # Aceptamos la dirección entrante, el loop quedará pegado en esta línea hasta que haya una conexión para aceptar
    socket_client, direccion = sock.accept()  # Mira bien que devuelve el metodo accept!
    # Cuando se acepta la conexión, tenemos una referencia al socket del cliente (para enviarle mensajes y recibirlos)
    # además de su dirección ip!
    print("Conexión aceptada desde", direccion)
    # Imprimimos el mensaje que nos envía el cliente, antes de pasar a escuchar nuevas conexiones
    print(socket_client.recv(2**12))  # Para recibir el mensaje, usamos la referencia al socket del cliente
