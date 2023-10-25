import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit


class MiniCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(350, 300, 500, 250)
        self.setWindowTitle('Миникалькулятор')

        self.label = QLabel(self)
        self.label.setText("Первое число(целое):")
        self.label.move(40, 25)

        self.label = QLabel(self)
        self.label.setText("Второе число(целое):")
        self.label.move(40, 85)

        self.calculate_button = QPushButton('->', self)
        self.calculate_button.move(200, 70)
        self.calculate_button.clicked.connect(self.run)

        self.number_1 = QLineEdit(self)
        self.number_1.move(40, 40)

        self.number_2 = QLineEdit(self)
        self.number_2.move(40, 100)

        self.sum_label = QLabel(self)
        self.sum_label.setText("Сумма:")
        self.sum_label.move(300, 40)

        self.result_sum = QLCDNumber(self)
        self.result_sum.move(380, 40)

        self.sub_label = QLabel(self)
        self.sub_label.setText("Разность:")
        self.sub_label.move(300, 70)

        self.result_sub = QLCDNumber(self)
        self.result_sub.move(380, 70)

        self.mult_label = QLabel(self)
        self.mult_label.setText("Произведение:")
        self.mult_label.move(290, 100)

        self.result_mul = QLCDNumber(self)
        self.result_mul.move(380, 100)

        self.div_label = QLabel(self)
        self.div_label.setText("Частное:")
        self.div_label.move(300, 130)

        self.result_div = QLCDNumber(self)
        self.result_div.move(380, 130)

    def run(self):
        x, y = int(self.number_1.text()), int(self.number_2.text())
        self.result_sum.display(x + y)
        self.result_sub.display(x - y)
        self.result_mul.display(x * y)
        if y != 0:
            self.result_div.display(round(x / y, 3))
        else:
            self.result_div.display("Error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MiniCalculator()
    ex.show()
    sys.exit(app.exec())
