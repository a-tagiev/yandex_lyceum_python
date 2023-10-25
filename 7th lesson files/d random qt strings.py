import random
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget


class RandomString(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Случайная строка из файла')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.text_field = QTextEdit(self)
        self.text_field.setReadOnly(True)
        layout.addWidget(self.text_field)

        self.button = QPushButton('Случайная строка', self)
        self.button.clicked.connect(self.load_random_string)
        layout.addWidget(self.button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_random_string(self):
        try:
            with open('lines.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
                lines = [line.strip() for line in lines if line.strip()]
            if lines:
                random_line = random.choice(lines)
                self.text_field.setPlainText(random_line)
        except FileNotFoundError:
            self.text_field.setPlainText('Файл не найден')


def main():
    app = QApplication(sys.argv)
    window = RandomString()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
