from PyQt5.QtCore import QObject, pyqtSignal


class CalculatorB(QObject):

    new_operation_signal = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numb_1 = None
        self.numb_2 = None
        self.operator = None

        self.diccionario_operaciones = {
            '+': self.suma,
            '-': self.resta,
            '*': self.multiplicacion,
            '/': self.division
        }

    def suma(self):
        resultado = self.numb_1 + self.numb_2
        self.new_operation_signal.emit(str(resultado))

    def resta(self):
        resultado = self.numb_1 - self.numb_2
        self.new_operation_signal.emit(str(resultado))

    def multiplicacion(self):
        resultado = self.numb_1 * self.numb_2
        self.new_operation_signal.emit(str(resultado))

    def division(self):
        resultado = self.numb_1 / self.numb_2
        self.new_operation_signal.emit(str(resultado))

    def refresh_operation(self, operacion):
        for operador in self.diccionario_operaciones.keys():
            if operador in operacion:
                self.operator = operador
                numeros = operacion.split(operador)
                self.numb_1 = float(numeros[0])
                self.numb_2 = float(numeros[1])
                break
        else:
            print("Ocurrió un error detectando el operador")
            return
        self.diccionario_operaciones[self.operator]()
