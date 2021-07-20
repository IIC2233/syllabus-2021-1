from consultas import (
    consulta_1, consulta_2, consulta_3, consulta_4, consulta_5, consulta_6
)
from consultas import (
    PATRON_1, PATRON_2, PATRON_3, PATRON_4, PATRON_5, PATRON_6
)


class Test:

    def __init__(self, argumentos, output_esperado, funcion):

        self.argumentos = argumentos
        self.output_esperado = output_esperado
        self.funcion = funcion
        self.resultados = []

    def probar_casos(self):

        self.resultados = []
        print(f"\n{'-' * 16}",
              f"Probando CONSULTA {self.funcion.__name__}",
              f"{'-' * 16}\n")

        # El resultado de cada función debe ser una lista de tuplas,
        # donde cada tupla es (match, inicio, fin)

        for i, (args, output_esperado) in enumerate(zip(
            self.argumentos, self.output_esperado
        )):
            try:
                # Intentamos ejecutar la función a testear para obtener
                # la respuesta
                respuesta = self.funcion(*args)
            except Exception as e:
                # En caso de error, se imprime, se salta al siguiente test,
                # y se agrega un None a los resultados
                print(f"Error al ejecutar función en test #{i}: {e}\n")
                self.resultados.append(None)
                continue

            # Ahora se compara si está correcto
            try:
                # Se compara el resultado con el output esperado en otro método
                correcto = self.comparar(respuesta, output_esperado)
                if correcto:
                    mensaje = f"Respuestas en test #{i} coinciden"
                else:
                    mensaje = f"ERROR: no coinciden respuestas en test #{i}"
                print(mensaje)
            except Exception as e:
                # En caso de error al comparar, se imprime y la respuesta
                # es incorrecta
                print(f"Error al comparar respuestas en test #{i}: {e}")
                correcto = False
            finally:
                # Se guarda el resultado
                self.resultados.append(correcto)
                print()

        # Se imprimen el resumen
        print(f"Casos probados: {len(self.argumentos)}")
        print(f"Correctos: {sum(1 if r is True else 0 for r in self.resultados)}")
        print(f"Incorrectos: {sum(1 if r is False else 0 for r in self.resultados)}")
        print(f"Errores: {sum(1 if r is None else 0 for r in self.resultados)}")

    def comparar(self, respuesta, output_esperado):

        if isinstance(respuesta, list) and isinstance(output_esperado, list):
            if len(respuesta) != len(output_esperado):
                return False

            # Quitamos None para ordenar sin problemas
            respuesta = [e for e in respuesta if e is not None]
            output_esperado = [e for e in output_esperado if e is not None]

            # Comparamos largo nuevamente
            if len(respuesta) != len(output_esperado):
                return False

            # En las listas ignoramos el orden
            return self.comparar(
                tuple(sorted(respuesta)), tuple(sorted(output_esperado))
            )

        elif isinstance(respuesta, tuple) and isinstance(output_esperado, tuple):
            if len(respuesta) != len(output_esperado):
                return False
            return all(
                self.comparar(respuesta[i], output_esperado[i]) for i in range(len(respuesta))
            )
        return respuesta == output_esperado


if __name__ == "__main__":

    with open("documento.md") as f:
        textoREADME = f.read()

    argumentos_1 = [
        (textoREADME, PATRON_1)
    ]

    argumentos_2 = [
        (textoREADME, PATRON_2)
    ]

    argumentos_3 = [
        (textoREADME, PATRON_3)
    ]

    argumentos_4 = [
        (textoREADME, PATRON_4)
    ]

    argumentos_5 = [
        (textoREADME, PATRON_5)
    ]

    argumentos_6 = [
        (textoREADME, PATRON_6)
    ]

    output_esperado_1 = [
        [{"contenido": "Titulo", "posicion": (2, 8)}],
    ]

    output_esperado_2 = [
        [{"contenido": "Una subseccion", "posicion": (251, 265)}],
    ]

    output_esperado_3 = [
        [{"contenido": "https://picsum.photos/id/320/2689/1795", "posicion": (202, 240)}],
    ]

    output_esperado_4 = [
        [{"contenido": "python", "posicion": (334, 370)}],
    ]

    output_esperado_5 = [
        [{"contenido": "Un elemento completado", "posicion": (123, 145)}],
    ]

    output_esperado_6 = [
        [{"contenido": "Un parrafo con un [link a la pagina del curso](https://iic2233.github.io/) y tambien", "posicion": (57, 83)}],
    ]

    # Prueba cada consulta
    test_1 = Test(argumentos_1, output_esperado_1, consulta_1)
    test_1.probar_casos()

    test_2 = Test(argumentos_2, output_esperado_2, consulta_2)
    test_2.probar_casos()

    test_3 = Test(argumentos_3, output_esperado_3, consulta_3)
    test_3.probar_casos()

    test_4 = Test(argumentos_4, output_esperado_4, consulta_4)
    test_4.probar_casos()

    test_5 = Test(argumentos_5, output_esperado_5, consulta_5)
    test_5.probar_casos()

    test_6 = Test(argumentos_6, output_esperado_6, consulta_6)
    test_6.probar_casos()
