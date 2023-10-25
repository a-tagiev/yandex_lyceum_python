import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel


class Arifmometr(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 300, 400, 200)
        self.first_value = QLineEdit('0', self)
        self.add_button = QPushButton('+', self)
        self.second_value = QLineEdit('0', self)
        self.result = QLineEdit('0', self)
        self.substract_button = QPushButton('-', self)
        self.multiply_button = QPushButton('*', self)
        self.add_button.resize(20, 20)
        self.add_button.move(70, 20)
        self.substract_button.resize(20, 20)
        self.substract_button.move(100, 20)
        self.multiply_button.resize(20, 20)
        self.multiply_button.move(130, 20)
        self.eq = QLabel('=', self)
        self.eq.move(210, 20)

        self.first_value.move(10, 20)
        self.first_value.resize(50, 20)
        self.second_value.move(160, 20)
        self.second_value.resize(50, 20)
        self.result.move(220, 20)
        self.result.resize(50, 20)
        self.add_button.clicked.connect(self.push)
        self.substract_button.clicked.connect(self.push)
        self.multiply_button.clicked.connect(self.push)

    def sum_numbers(self):
        self.result.setText(str(int(self.first_value.text()) + int(self.second_value.text())))

    def multiply_numbers(self):
        self.result.setText(str(int(self.first_value.text()) * int(self.second_value.text())))

    def substract_numbers(self):
        self.result.setText(str(int(self.first_value.text()) - int(self.second_value.text())))

    def push(self):
        sender = self.sender()
        if sender == self.multiply_button:
            self.multiply_numbers()
        if sender == self.add_button:
            self.sum_numbers()
        if sender == self.substract_button:
            self.substract_numbers()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Arifmometr()
    ex.show()
    sys.exit(app.exec())
