import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QVBoxLayout, QPushButton, QLineEdit


class Shuffle(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Shuffle')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout(self)

        self.text_browser = QTextBrowser(self)
        layout.addWidget(self.text_browser)

        self.button = QPushButton('Загрузить строки', self)
        layout.addWidget(self.button)

        self.text_field = QLineEdit(self)
        layout.addWidget(self.text_field)

        self.button.clicked.connect(self.load_and_shuffle)

    def load_and_shuffle(self):
        file_path = self.text_field.text()

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

            even_lines = [line.strip() for i, line in enumerate(lines) if i % 2 == 0]
            odd_lines = [line.strip() for i, line in enumerate(lines) if i % 2 != 0]

            result_lines = even_lines + odd_lines
            shuffled_text = '\n'.join(result_lines)

            self.text_browser.setPlainText(shuffled_text)
        except Exception as e:
            self.text_browser.setPlainText(str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Shuffle()
    window.show()
    sys.exit(app.exec_())
