import sys

from views import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QFileDialog

class MyPillow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        uic.loadUi('01.ui', self)

    def initUI(self):
        self.setWindowTitle('PIL 2.0')
        self.setGeometry(400, 300, 400, 70)
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.trick_button.clicked.connect(self.push)

    def push(self):

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec_())
