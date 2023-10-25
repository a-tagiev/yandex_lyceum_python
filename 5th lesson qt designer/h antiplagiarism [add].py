import sys

import difflib

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox, QVBoxLayout, QWidget, QPlainTextEdit, \
    QPushButton, QStatusBar
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GGUI.ui', self)
        self.initUI()

    def initUI(self):
        self.checkBtn = QPushButton("Проверить", self)
        self.checkBtn.clicked.connect(self.compare)

    def (self):
        str1 = self.str1.toPlainText()
        str2 = self.str2.toPlainText()

        y = difflib.SequenceMatcher(None, str1.lower(), str2.lower()).ratio() * 100
        if self.Porog.text():
            if int(self.Porog.text()) >= round(y, 2):
                self.label.setText(f"Текст похож на {round(y, 2)}%")
                self.label.setStyleSheet('QLabel {background-color: green;}')
            else:
                self.label.setText(f"Текст похож на {round(y, 2)}%")
                self.label.setStyleSheet('QLabel {background-color: red;}')
        else:
            self.label.setText("Введите порог сравнения")
            self.label.setStyleSheet('QLabel {background-color: red;}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
import sys

import difflib

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox, QVBoxLayout, QWidget, QPlainTextEdit, \
    QPushButton, QStatusBar


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Проверка на антиплагиат")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.alert_value = QDoubleSpinBox(self)
        self.alert_value.setRange(0, 100)
        self.alert_value.setSingleStep(0.01)
        self.alert_value.setValue(50.0)
        layout.addWidget(self.alert_value)
        self.text1 = QPlainTextEdit(self)
        layout.addWidget(self.text1)
        self.text2 = QPlainTextEdit(self)
        layout.addWidget(self.text2)
        self.checkBtn = QPushButton("Проверить", self)
        self.checkBtn.clicked.connect(self.compare)
        layout.addWidget(self.checkBtn)
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)



    def compare(self):
        str1 = self.text1.toPlainText()
        str2 = self.text2.toPlainText()
        lines1 = set(str1.splitlines())
        lines2 = set(str2.splitlines())
        common_lines = lines1.intersection(lines2)
        threshold = self.alert_value.value()
        if len(lines1) == 0 or len(lines2) == 0:
            similarity_percentage = 0.00
        else:
            similarity_percentage = (len(common_lines) / max(len(lines1), len(lines2))) * 100

        if similarity_percentage >= threshold:
            message = f"Тексты похожи на {similarity_percentage:.2f}%, плагиат"
        else:
            message = f"Тексты похожи на {similarity_percentage:.2f}%, не плагиат"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())