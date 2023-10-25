import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget, QStatusBar

class AntiPlagiarism(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Проверка на антиплагиат")
        self.setGeometry(100, 100, 600, 400)

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
        self.checkBtn.clicked.connect(self.check_plagiarism)
        layout.addWidget(self.checkBtn)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def check_plagiarism(self):
        text1 = self.text1.toPlainText()
        text2 = self.text2.toPlainText()
        threshold = self.alert_value.value()

        lines1 = set(text1.splitlines())
        lines2 = set(text2.splitlines())
        common_lines = lines1.intersection(lines2)

        if len(lines1) == 0 or len(lines2) == 0:
            similarity_percentage = 0.00
        else:
            similarity_percentage = (len(common_lines) / max(len(lines1), len(lines2))) * 100

        if similarity_percentage >= threshold:
            message = f"Тексты похожи на {similarity_percentage:.2f}%, плагиат"
        else:
            message = f"Тексты похожи на {similarity_percentage:.2f}%, не плагиат"

        self.statusBar.showMessage(message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AntiPlagiarism()
    window.show()
    sys.exit(app.exec_())
