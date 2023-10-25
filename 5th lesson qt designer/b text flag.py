import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QButtonGroup, QRadioButton, QPushButton, \
    QWidget


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Текстовый флаг")
        self.setFixedSize(400, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.color_group_1 = QButtonGroup(self)
        self.color_group_2 = QButtonGroup(self)
        self.color_group_3 = QButtonGroup(self)

        color_layout = QVBoxLayout()

        color_label_1 = QLabel("Цвет №1")
        color_layout.addWidget(color_label_1)

        self.blue_btn = QRadioButton("Синий")
        self.red_btn = QRadioButton("Красный")
        self.green_btn = QRadioButton("Зелёный")

        self.color_group_1.addButton(self.blue_btn)
        self.color_group_1.addButton(self.red_btn)
        self.color_group_1.addButton(self.green_btn)

        color_layout.addWidget(self.blue_btn)
        color_layout.addWidget(self.red_btn)
        color_layout.addWidget(self.green_btn)

        color_label_2 = QLabel("Цвет №2")
        color_layout.addWidget(color_label_2)

        self.blue_btn_2 = QRadioButton("Синий")
        self.red_btn_2 = QRadioButton("Красный")
        self.green_btn_2 = QRadioButton("Зелёный")

        self.color_group_2.addButton(self.blue_btn_2)
        self.color_group_2.addButton(self.red_btn_2)
        self.color_group_2.addButton(self.green_btn_2)

        color_layout.addWidget(self.blue_btn_2)
        color_layout.addWidget(self.red_btn_2)
        color_layout.addWidget(self.green_btn_2)

        color_label_3 = QLabel("Цвет №3")
        color_layout.addWidget(color_label_3)

        self.blue_btn_3 = QRadioButton("Синий")
        self.red_btn_3 = QRadioButton("Красный")
        self.green_btn_3 = QRadioButton("Зелёный")

        self.color_group_3.addButton(self.blue_btn_3)
        self.color_group_3.addButton(self.red_btn_3)
        self.color_group_3.addButton(self.green_btn_3)

        color_layout.addWidget(self.blue_btn_3)
        color_layout.addWidget(self.red_btn_3)
        color_layout.addWidget(self.green_btn_3)

        layout.addLayout(color_layout)

        self.make_flag = QPushButton("Сделать флаг", self)
        self.make_flag.clicked.connect(self.generate_flag)
        layout.addWidget(self.make_flag)

        self.result = QLabel(self)
        layout.addWidget(self.result)

    def generate_flag(self):
        color_1 = self.color_group_1.checkedButton().text()
        color_2 = self.color_group_2.checkedButton().text()
        color_3 = self.color_group_3.checkedButton().text()

        flag_text = f"Цвета: {color_1}, {color_2} и {color_3}"
        self.result.setText(flag_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FlagMaker()
    window.show()
    sys.exit(app.exec_())
