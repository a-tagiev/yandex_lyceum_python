import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class Evaluator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Вычисление выражений')
        self.setGeometry(100, 100, 400, 100)
        self.first_value = QLineEdit(self)
        self.trick_button = QPushButton('->', self)
        self.second_value = QLineEdit(self)
        self.trick_button.resize(50, 50)
        self.trick_button.move(175, 10)
        self.first_value.move(10, 10)
        self.first_value.resize(150, 50)
        self.second_value.move(240, 10)
        self.second_value.resize(150, 50)
        self.trick_button.clicked.connect(self.push)

    def push(self):
        first_text = self.first_value.text()
        self.second_value.setText(str(eval(first_text)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Evaluator()
    ex.show()
    sys.exit(app.exec())
