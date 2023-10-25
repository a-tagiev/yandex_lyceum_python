import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QCheckBox


class WidgetsHideNSeek(QWidget):
    def __init__(self):
        super().__init__()
        self.edit4 = None
        self.checkbox4 = None
        self.edit3 = None
        self.checkbox3 = None
        self.edit2 = None
        self.checkbox2 = None
        self.edit1 = None
        self.checkbox1 = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Прятки для виджетов')
        self.setGeometry(400, 300, 300, 200)
        self.checkbox1 = QCheckBox('edit1', self)
        self.checkbox1.move(10, 25)
        self.edit1 = QLineEdit(self)
        self.edit1.setText("Поле edit1")
        self.edit1.move(70, 20)
        self.checkbox1.setChecked(True)
        self.edit1.setVisible(True)
        self.checkbox1.stateChanged.connect(self.push)

        self.checkbox2 = QCheckBox('edit2', self)
        self.checkbox2.move(10, 55)
        self.edit2 = QLineEdit(self)
        self.edit2.setText("Поле edit2")
        self.edit2.move(70, 50)
        self.checkbox2.setChecked(True)
        self.edit2.setVisible(True)
        self.checkbox2.stateChanged.connect(self.push)

        self.checkbox3 = QCheckBox('edit3', self)
        self.checkbox3.move(10, 85)
        self.edit3 = QLineEdit(self)
        self.edit3.setText("Поле edit3")
        self.edit3.move(70, 80)
        self.checkbox3.setChecked(True)
        self.edit3.setVisible(True)
        self.checkbox3.stateChanged.connect(self.push)

        self.checkbox4 = QCheckBox('edit4', self)
        self.checkbox4.move(10, 115)
        self.edit4 = QLineEdit(self)
        self.edit4.setText("Поле edit4")
        self.edit4.move(70, 110)
        self.checkbox4.setChecked(True)
        self.edit4.setVisible(True)
        self.checkbox4.stateChanged.connect(self.push)
        self.widgets = []
        self.widgets.append((self.checkbox1, self.edit1))
        self.widgets.append((self.checkbox2, self.edit2))
        self.widgets.append((self.checkbox3, self.edit3))
        self.widgets.append((self.checkbox4, self.edit4))

    def push(self, n):
        sender = self.sender()
        for checkbox, edit in self.widgets:
            if sender == checkbox:
                if n == 2:
                    edit.show()
                else:
                    edit.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WidgetsHideNSeek()
    ex.show()
    sys.exit(app.exec())
