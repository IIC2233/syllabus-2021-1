"""
IMPORTANTE: hay muchísimas formas de implementar una arquitectura cliente-servidor en python, y depende enormemente de
lo que quieras lograr con tu programa. Te recomendamos fuertemente entender este ejemplo y el de clases (el cual hace una
implementación alternativa), para poder así editarlos a las necesidades de tu programa en el futuro. No tengas miedo a
experimentar ;)
"""

import json
import socket
import threading


class Cliente:

    def __init__(self, host, port):
        # Dirección IP del host destinatario
        self.host = host
        # Puerto al que nos queremos conectar
        self.port = port
        # Crear socket con dirección IPv4 y protocolo TCP
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Conectarse al servidor
            self.socket_cliente.connect((self.host, self.port))
            # Crear y empezar thread encargado de escuchar al servidor
            thread = threading.Thread(target=self.escuchar_servidor, daemon=True)
            thread.start()
            print("Conexión exitosa")
            # Ingresar mensaje a enviar al servidor
            self.recibir_input()
        except ConnectionRefusedError:
            print("Error en la conexión")
            self.socket_cliente.close()

    def escuchar_servidor(self):
        try:
            while True:
                # Recibir y manejar mensajes del servidor
                mensaje = self.recibir()
                print("Mensaje recibido del servidor: ", mensaje)
                if mensaje != "":
                    self.manejar_mensaje_recibido(mensaje)
        except ConnectionResetError:
            print("Error de conexión con el servidor")
        finally:
            # Cerrar socket
            self.socket_cliente.close()

    def recibir(self):
        # Recibir largo del mensaje
        largo_bytes_mensaje = self.socket_cliente.recv(4)
        # Decodificar largo del mensaje
        largo_mensaje = int.from_bytes(largo_bytes_mensaje, byteorder="big")
        # Recibir mensaje
        bytes_mensaje = bytearray()
        while len(bytes_mensaje) < largo_mensaje:
            bytes_a_recibir = min(4096, largo_mensaje - len(bytes_mensaje))
            bytes_mensaje += self.socket_cliente.recv(bytes_a_recibir)
        # Decodificar mensaje
        mensaje = self.decodificar_mensaje(bytes_mensaje)
        return mensaje

    def enviar(self, mensaje):
        print("Enviando al servidor el mensaje: ", mensaje)
        # Codificar mensaje
        bytes_mensaje = self.codificar_mensaje(mensaje)
        # Codificar largo del mensaje
        largo_bytes_mensaje = len(bytes_mensaje).to_bytes(4, byteorder="big")
        # Enviar largo del mensaje + mensaje
        self.socket_jugador.sendall(largo_bytes_mensaje + bytes_mensaje)

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

    def manejar_mensaje_recibido(self, mensaje):
        # De acuerdo al mensaje que se reciba de parte del servidor se debería generar una acción acorde.
        accion = f"Realizando acción asociada al mensaje: {mensaje}"
        print(accion)

    def recibir_input(self):
        while True:
            mensaje = input()
            self.enviar(mensaje)


if __name__ == "__main__":
    host = "localhost"
    port = 5000
    cliente = Cliente(host, port)