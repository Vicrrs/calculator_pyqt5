import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout, QLineEdit


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.setWindowTitle('Calculadora do Roza')
        self.setFixedSize(400, 400)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.setDisabled(True)

        self.setCentralWidget(self.cw)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = Calculadora()
    app.show()
    qt.exec_()
