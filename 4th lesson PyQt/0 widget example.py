import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLCDNumber


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.n = 0

        self.initUI()

    def initUI(self):
        self.setGeometry(400, 300, 500, 300)
        # первая пара отвечает за удаленность от верхнего левого угла экрана, а вторая пара - размер окна
        self.setWindowTitle('Первая программа')
        self.btn = QPushButton('0', self)
        self.btn.resize(200, 100)
        self.btn.move(150, 100)
        self.btn.clicked.connect(self.push)
        self.label = QLabel(self)
        self.label.setText(f"clicks:{self.n + 1}")
        self.label.move(150, 10)
        self.LCD_count = QLCDNumber(self)
        self.LCD_count.move(230, 200)

    def push(self):
        self.n += 1
        self.btn.move(0, 100)
        self.btn.setText(f"{int(self.btn.text()) + 1}")
        self.LCD_count.display(self.n)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
