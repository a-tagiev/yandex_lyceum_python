import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class MorseCode(QWidget):
    def __init__(self):
        super().__init__()
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.MorseDict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                          'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                          'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
                          'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 300, 600, 200)
        cnt = 0

        for i in self.alphabet:
            cnt += 1
            self.letter = QPushButton(i, self)
            self.letter.resize(20, 20)
            self.letter.move(cnt * 20, 20)
            self.letter.clicked.connect(self.push)
        self.result = QLineEdit('', self)
        self.result.move(30, 50)

    def push(self):
        send = self.sender()
        txt_prev = self.result.text()
        self.result.setText(txt_prev + self.MorseDict[send.text()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MorseCode()
    ex.show()
    sys.exit(app.exec())
