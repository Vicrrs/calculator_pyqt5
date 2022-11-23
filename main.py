import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.setWindowTitle('Calculadora do Roza')
        self.setFixedSize(400, 400)

        self.btn = QPushButton("Texto do Botão")
        self.btn.setStyleSheet('font-size: 20px')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        self.btn.clicked.connect(lambda: print("Olá mundo!"))

        self.setCentralWidget(self.cw)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
