"""
IMPORTANTE: hay muchísimas formas de implementar una arquitectura cliente-servidor en python, y depende enormemente de
lo que quieras lograr con tu programa. Te recomendamos fuertemente entender este ejemplo y el de clases (el cual hace una
implementación alternativa), para poder así editarlos a las necesidades de tu programa en el futuro. No tengas miedo a
experimentar ;)
"""
import json
import socket
import threading


class Servidor:

    def __init__(self, host, port):
        # host en el que está corriendo el servidor
        self.host = host
        # puerto donde se escucharán las conexiones
        self.port = port
        # Crear socket con dirección IPv4 y protocolo TCP
        print("Iniciando servidor...")
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Ligar host y port
        self.socket_servidor.bind((self.host, self.port))
        # Empezar a escuchar conexiones
        self.socket_servidor.listen()
        # Crear y empezar thread encargado de aceptar conexiones
        thread = threading.Thread(target=self.aceptar_clientes)
        thread.start()

    def aceptar_clientes(self):
        print("Escuchando clientes...")
        while True:
            # Comenzar a aceptar clientes
            # (socket, (dirección IP, puerto)) = accept()
            socket_cliente, address = self.socket_servidor.accept()
            print("Conexión aceptada: ", address)
            # Crear y empezar un thread para escuchar a cada cliente
            thread_cliente = threading.Thread(target=self.escuchar_cliente, args=(socket_cliente,), daemon=True)
            thread_cliente.start()

    def escuchar_cliente(self, socket_cliente):
        try:
            while True:
                # Recibir y manejar mensajes del cliente
                mensaje = self.recibir(socket_cliente)
                print("Mensaje recibido: ", mensaje)
                if mensaje != "":
                    respuesta = self.manejar_mensaje_recibido(mensaje, socket_cliente)
                    self.enviar(respuesta, socket_cliente)
        except ConnectionResetError:
            print("Error de conexión con el cliente")

    def recibir(self, socket_cliente):
        # Recibir largo del mensaje
        largo_bytes_mensaje = socket_cliente.recv(4)
        # Decodificar largo del mensaje
        largo_mensaje = int.from_bytes(largo_bytes_mensaje, byteorder="big")
        # Recibir mensaje
        bytes_mensaje = bytearray()
        while len(bytes_mensaje) < largo_mensaje:
            bytes_a_recibir = min(4096, largo_mensaje - len(bytes_mensaje))
            bytes_mensaje += socket_cliente.recv(bytes_a_recibir)
        # Decodificar mensaje
        mensaje = self.decodificar_mensaje(bytes_mensaje)
        return mensaje

    def enviar(self, mensaje, socket_jugador):
        # Codificar mensaje
        bytes_mensaje = self.codificar_mensaje(mensaje)
        # Codificar largo del mensaje
        largo_bytes_mensaje = len(bytes_mensaje).to_bytes(4, byteorder="big")
        # Enviar largo del mensaje + mensaje
        socket_jugador.sendall(largo_bytes_mensaje + bytes_mensaje)

    def codificar_mensaje(self, mensaje):
        try:
            # Serializar el mensaje
            mensaje_json = json.dumps(mensaje)
            # Codificar el mensaje serializado
            bytes_mensaje = mensaje_json.encode("utf-8")
            return bytes_mensaje
        except json.JSONDecodeError:
            print("No se pudo codificar el mensaje")
            return b""

    def decodificar_mensaje(self, bytes_mensaje):
        try:
            # Deserializar el mensaje
            mensaje = json.loads(bytes_mensaje)
            return mensaje
        except json.JSONDecodeError:
            print("No se pudo decodificar el mensaje")
            return dict()

    def manejar_mensaje_recibido(self, mensaje, socket_cliente):
        # De acuerdo al mensaje que se reciba de parte del cliente se debería generar una respuesta acorde
        respuesta = f"[Respuesta de servidor asociada al mensaje: {mensaje}]"
        print("Enviando respuesta al cliente: ", respuesta)
        return respuesta


if __name__ == "__main__":
    host = "localhost"
    port = 5000
    servidor = Servidor(host, port)

