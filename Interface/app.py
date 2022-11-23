import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.setWindowTitle('Calculadora do Roza')
        self.setFixedSize(400, 400)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: white; color: #000; font-size: 30px}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_botao(QPushButton('7'), 1, 0, 1, 1)
        self.add_botao(QPushButton('8'), 1, 1, 1, 1)
        self.add_botao(QPushButton('9'), 1, 2, 1, 1)
        self.add_botao(QPushButton('+'), 1, 3, 1, 1)
        self.add_botao(QPushButton('C'), 1, 4, 1, 1, lambda: self.display.setText(''),
                       'background: red; color: #fff; font-weight: 700;')

        self.add_botao(QPushButton('4'), 2, 0, 1, 1)
        self.add_botao(QPushButton('5'), 2, 1, 1, 1)
        self.add_botao(QPushButton('6'), 2, 2, 1, 1)
        self.add_botao(QPushButton('-'), 2, 3, 1, 1)
        self.add_botao(QPushButton('<-'), 2, 4, 1, 1, lambda: self.display.setText(self.display.text()[:-1]),
                       'background: orange; color: #fff; font-weight: 700;')

        self.add_botao(QPushButton('1'), 3, 0, 1, 1)
        self.add_botao(QPushButton('2'), 3, 1, 1, 1)
        self.add_botao(QPushButton('3'), 3, 2, 1, 1)
        self.add_botao(QPushButton('/'), 3, 3, 1, 1)
        self.add_botao(QPushButton(''), 3, 4, 1, 1)

        self.add_botao(QPushButton('.'), 4, 0, 1, 1)
        self.add_botao(QPushButton('0'), 4, 1, 1, 1)
        self.add_botao(QPushButton(''), 4, 2, 1, 1)
        self.add_botao(QPushButton('*'), 4, 3, 1, 1)
        self.add_botao(QPushButton('='), 4, 4, 1, 1, self.igual,
                       'background: navy; color: #fff; font-weight: 700;')

        self.setCentralWidget(self.cw)

    def add_botao(self, botao, row, col, rowspan, colspan, func=None, style=None):
        self.grid.addWidget(botao, row, col, rowspan, colspan)

        if not func:
            botao.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + botao.text()
                )
            )
        else:
            botao.clicked.connect(func)

        if style:
            botao.setStyleSheet(style)

        botao.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except Exception as e:
            self.display.setText('Conta inválida')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = Calculadora()
    app.show()
    qt.exec_()
