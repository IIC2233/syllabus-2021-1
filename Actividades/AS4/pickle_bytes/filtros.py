"""
Este módulo contiene a la clase FilterBox y la función obtener_paquete_secreto
Contiene la lógica necesaria para aplicar los filtros a las imágenes

Corresponde a la parte de Pickle y Bytes
"""
import pickle
from manejo_bytes import int_desde_bytes, tuplas_desde_bytes, bytes_desde_tuplas, organizar_bmp
from parametros import MINIMALISM_THRESHOLD, CENSOR_MUTIPLIER, RUTA_IMAGEN, ALPHA_PUSH_VALUE
from math import sqrt
from os import path


def obtener_paquete_secreto():
    """
    Crea una instancia de la clase FilterBox, y la serializa

    Retorna:
        bytes: resultado de serializar la instancia de FilterBox, corresponde
            al paquete secreto
    """
    # Debes completar esta función
    pass


class FilterBox:
    """
    Clase FilterBox, representa al paquete de filtros que se acceden desde la
    interfaz del programa
    """

    def __init__(self, *args, **kwargs):
        # NO MODIFICAR
        super().__init__(*args, **kwargs)
        self.diccionario_filtros = {
            "lighten": self.lighten,
            "darken": self.darken,
            "shuffle": self.shuffle,
            "colorflip": self.colorflip,
            "pepawave": self.pepawave_init,
            "MrStark": self.mr_stark_init,
            "iDontWannaGo": self.idont_wanna_go_init,
            "censor": self.censor_init,
            "minimalism": self.minimalism,
            "v-flip": self.vertical_flip,
            "alphaShuffle": self.alpha_shuffle
        }
        self.filtros_especiales = ['pepawave', 'MrStark', 'v-flip', 'iDontWannaGo', "censor"]
        self.step_actual = 0
        self.tamano_step = 0
        self.datos_imagen = {'w': 0, 'h': 0}

    # //-//-//-//-//-//-//-//-//
    # \\ Métodos parte pickle \\
    # //-//-//-//-//-//-//-//-//

    def __getstate__(self):
        """
        supongamos el siguiente orden de instrucciones de codificacón:
         (los cambios se hacen en el atributo diccionario_filtros)
         1- En el diccionario filtros, se reemplazan todos los values por el filtro_bomba
         2- Se agrega una llave "TOP-SECRET", que sus contenidos son una lista de tuplas,
         cuyo primer valor es una llave de diccionario filtros y el segundo la
         funcion correspondiente
         2- Se cambian los keys del dicccinario_metodo al string en reversa.
        :return: dict
        """
        pass

    def __setstate__(self, state):
        pass

    # //-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//
    # \\                          MÉTODOS IMPORTANTES                         \\
    # //-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//

    @staticmethod
    def aumento_seguro(original, increase_factor):
        """
        Aumenta un int reduciendo la cantidad de información perdida.
        :param original: el int a aumentar
        :param increase_factor: factor de aumento
        :return:
        """
        if increase_factor < 0:
            raise ValueError("increase_factor must be a positive float or integer")
        exponential_int = original ** 2
        exponential_int *= increase_factor
        new_value = sqrt(exponential_int)
        return max(min(round(new_value), 255), 0)

    def modificar_bytes(self, nombre_filtro, in_bytes):
        """
        Aplica el filtro indicado a los bytes de la imagen

        Argumentos:
            nombre_filtro (str): El nombre del filtro a aplicar sobre la imagen
            in_bytes (bytes): Bytes originales de la imagen a modificar

        Retorna:
            bytes: Bytes de la imagen ya modificados por el filtro
        """
        header, dib_header, pixel_data, eof = organizar_bmp(in_bytes)

        tuples = tuplas_desde_bytes(pixel_data)
        try:
            function = self.diccionario_filtros[nombre_filtro]
        except KeyError:
            function = self.rr_reader

        if nombre_filtro in self.filtros_especiales:
            self.datos_imagen['w'] = int_desde_bytes(dib_header[4:8])
            self.datos_imagen['h'] = int_desde_bytes(dib_header[8:12])
            self.datos_imagen['size'] = len(tuples)
            resulting_tuples = function(tuples)
        else:
            resulting_tuples = self.aplicar_filtro(tuples, function)
        try:
            resulting_bytes = bytes_desde_tuplas(resulting_tuples)
        except TypeError:
            resulting_bytes = resulting_tuples
        out_data = bytearray()
        out_data.extend(header)
        out_data.extend(dib_header)
        out_data.extend(resulting_bytes)
        out_data.extend(eof)
        return out_data

    @staticmethod
    def aplicar_filtro(tuplas, func):
        """
        Aplica la función representando el filtro a los bytes de la imagen

        Argumentos:
            tuplas (list[tuple]): La información de la imagen en formato de
                lista de tuplas
            func (function): Función (filtro) a aplicar sobre las tuplas

        Retorna:
            list[tuple]: Tuplas de la imagen con filtro ya aplicado
        """
        # NO MODIFICAR
        return list(map(func, tuplas))

    # //-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//
    # \\                               FILTROS                                \\
    # //-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//-//

    # //-//-//-//-//-//-//
    # \\  Filtros color \\
    # //-//-//-//-//-//-//

    def lighten(self, tup):
        return (tup[0],) + tuple((self.aumento_seguro(k, 2) for k in tup[1:]))

    def darken(self, tup):
        return (tup[0],) + tuple((self.aumento_seguro(k, 0.5) for k in tup[1:]))

    @staticmethod
    def shuffle(tup):
        return tup[0], tup[2], tup[3], tup[1]

    @staticmethod
    def colorflip(tup):
        return (tup[0],) + tuple((255 - k for k in tup[1:]))

    def pepawave_init(self, tuples):
        self.step_actual = -127
        self.tamano_step = 255 / self.datos_imagen['size']
        return list(map(self.pepawave, tuples))

    def pepawave(self, tup):
        self.step_actual += self.tamano_step
        diff = abs(round(self.step_actual))
        pos0 = tup[0]
        pos1 = min(255, (tup[1]))
        pos2, pos3 = max(0, tup[2] - diff), max(0, tup[3] - diff)
        return pos0, pos1, pos2, pos3

    # //-//-//-//-//-//-//
    # \\  Filtros alpha \\
    # //-//-//-//-//-//-//

    def idont_wanna_go_init(self, tuples):
        self.step_actual = 0
        self.tamano_step = 255 / self.datos_imagen['size']
        return list(map(self.idont_wanna_go, tuples))

    def idont_wanna_go(self, tup):
        self.step_actual += self.tamano_step
        diff = round(self.step_actual)
        return (min(255, tup[0] + diff),) + tup[1:]

    def mr_stark_init(self, tuples):
        self.step_actual = 255
        self.tamano_step = 255 / self.datos_imagen['size']
        return list(map(self.mr_stark, tuples))

    def mr_stark(self, tup):
        self.step_actual -= self.tamano_step
        diff = round(self.step_actual)
        return (max(0, tup[0] - diff),) + tup[1:]

    @staticmethod
    def alpha_flip(tup):
        return (-tup[0] + 255,) + tup[1:]

    @staticmethod
    def alpha_shuffle(tup):
        return tup[1], tup[2], tup[3], tup[0]

    @staticmethod
    def minimalism(tup):
        if sum(tup[1:]) > MINIMALISM_THRESHOLD:
            return (-tup[0] + 255,) + tup[1:]
        return tup

    def censor_init(self, tuples):
        self.step_actual = 0
        return list(map(self.censor, tuples))

    def censor(self, tup):
        self.step_actual += 1
        multiplier = CENSOR_MUTIPLIER
        alpha_value = ((self.step_actual % (30 * multiplier)) - 15 * multiplier) ** 2
        return (min(tup[0], round(alpha_value / (multiplier ** 2))),) + tup[1:]

    @staticmethod
    def alpha_push(tup):
        return ((tup[0] + ALPHA_PUSH_VALUE) % 255,) + tup[1:]

    # //-//-//-//-//-//-//-//-//
    # \\  Filtros binarios OwO \\
    # //-//-//-//-//-//-//-//-//

    @staticmethod
    def woodstock(tup):
        new_tup = [tup[0]]
        for colour in tup[1:]:
            binary = f"{colour:08b}"
            new_binary = binary[4:] + binary[:4]
            new_tup.append(int(new_binary, 2))
        return tuple(new_tup)

    @staticmethod
    def displace(tup):
        binary_tup = map(lambda x: f"{x:08b}", tup)
        bin_string = "".join(binary_tup)
        switched = bin_string[6:] + bin_string[:6]
        final_tup = (switched[:8], switched[8:16], switched[16:24], switched[24:])
        return tuple(map(lambda x: int(x, 2), final_tup))

    @staticmethod
    def havoc(tup):
        new_tup = [tup[0]]
        for colour in tup[1:]:
            binary = f"{colour:08b}"
            new_binary = binary[::-1]
            new_tup.append(int(new_binary, 2))
        return tuple(new_tup)

    @staticmethod
    def sidestep(tup):
        new_tup = [tup[0]]
        for colour in tup[1:]:
            binary = f"{colour:08b}"
            new_binary = binary[1:] + binary[0]
            new_tup.append(int(new_binary, 2))
        return tuple(new_tup)

    @staticmethod
    def scramble(tup):
        return (tup[0],) + tuple((k ^ tup[0] for k in tup[1:]))

    # //-//-//-//-//-//-//-//-//
    # \\  Filtros misceláneos \\
    # //-//-//-//-//-//-//-//-//

    @staticmethod
    def rr_reader(tup):
        image_path = path.join('.rrdata', 'updata.rr')
        with open(image_path, 'rb') as file:
            reset_bytes = bytearray(file.read())
        return reset_bytes[::-1]

    @staticmethod
    def vertical_flip(tuples):
        return tuples[::-1]

    @staticmethod
    def filtro_bomba(tup):
        """
        ¡Filtro bomba! Causará que el programa se caiga en caso de que alguien
        intente usar el programa sin la serialización correcta.
        """
        # No debes modificar este método
        raise ValueError("Ha explotado el paquete con la información!\n" +
                         "Whatsapp 2 permanecerá en las sombras")


if __name__ == "__main__":
    # Crear filterbox
    filterbox = FilterBox()
    # Codificar
    encoded_filterbox = pickle.dumps(filterbox)
    # Decodificar
    decoded_filterbox = pickle.loads(encoded_filterbox)
    # Probar filtro
    with open(RUTA_IMAGEN, "rb") as bmp_file:
        bytes_imagen = bmp_file.read()
    res = decoded_filterbox.modificar_bytes("pepawave", bytes_imagen)
    with open("test_out.bmp", "wb") as out_file:
        out_file.write(res)
