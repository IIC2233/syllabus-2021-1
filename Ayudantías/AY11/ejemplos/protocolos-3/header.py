# A continuación realizaremos una versión "human readable" de como funcionan los headers.

# Establecemos el tamaño del header global.
header_size = 10

mensaje = "¡Hay zombies afuera de mi casa!"
# Dado que el header es de máximo 10 caracteres, y los computadores manejan mejor la información cuando es concisa,
# reducimos nuestros "header" a las palabras esenciales.
# Como que no todos los header necesariamente tendrán 10 caracteres,
# establecemos en el protocolo que deben llenarse con 0s hasta alcanzar esa cantidad. Para esto es muy útil el método zfill()!
header1 = "Minecraft".zfill(header_size)
header2 = "Ventana".zfill(header_size)
mensaje1 = header1 + mensaje
mensaje2 = header2 + mensaje


# Crearemos una función que se encarga de recibir los mensajes
def recibir_mensaje(mensaje):
    header = mensaje[:header_size].strip("0")
    contenido = mensaje[header_size:]
    print(f'header:{header}\ncontenido: {contenido}')


recibir_mensaje(mensaje1)
recibir_mensaje(mensaje2)
print()

# Probemos como llegarían los mensajes si no siguieramos el protocolo de comunicación...
header1 = "Ventana"
mensaje1 = header1 + mensaje
recibir_mensaje(mensaje1)



