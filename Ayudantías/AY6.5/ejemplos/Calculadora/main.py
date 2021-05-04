import sys
from calc_front import CalculatorF
from calc_back import CalculatorB
from PyQt5.QtWidgets import QApplication


def hook(type_error, traceback):
    print(type_error)
    print(traceback)


if __name__ == '__main__':
    sys.__excepthook__ = hook
    app = QApplication(sys.argv)
    front = CalculatorF(700, 900)
    back = CalculatorB()

    # Conexion de senales
    front.button_clicked_signal.connect(back.refresh_operation)
    back.new_operation_signal.connect(front.refresh_screen)

    app.exec()
