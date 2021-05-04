import sys
import parameters as p
from pou import PouF
from PyQt5.QtWidgets import QApplication


def hook(type_error, traceback):
    print(type_error)
    print(traceback)


if __name__ == '__main__':
    sys.__excepthook__ = hook
    app = QApplication(sys.argv)
    front = PouF(p.width, p.height)
    front.show()
    app.exec()
