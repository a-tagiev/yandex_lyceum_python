import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class WordTrick(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Перекидыватель слов')
        self.setGeometry(400, 300, 400, 70)
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
        second_text = self.second_value.text()

        self.first_value.setText(second_text)
        self.second_value.setText(first_text)

        if self.trick_button.text() == '->':
            self.trick_button.setText('<-')
            self.first_value.setText('')
            self.second_value.setText(first_text)

        else:
            self.trick_button.setText('->')
            self.first_value.setText(second_text)
            self.second_value.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WordTrick()
    ex.show()
    sys.exit(app.exec_())
