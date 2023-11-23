import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsScene, QGraphicsView, QVBoxLayout
from PyQt5.QtGui import QBrush, QColor, QPainter
from PyQt5.QtCore import Qt

import random


class Circle:
    def __init__(self, diameter, color):
        self.diameter = diameter
        self.color = color


from PyQt5.QtCore import QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton, QGraphicsView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addButton.setText(_translate("MainWindow", "Add Circle"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.scene = QGraphicsScene(self)
        self.graphicsView = QGraphicsView(self.scene)
        self.setCentralWidget(self.graphicsView)

        self.addButton = QPushButton("Add Circle", self)
        self.addButton.clicked.connect(self.add_circle)

        layout = self.create_layout()
        self.centralWidget().setLayout(layout)

    def create_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.graphicsView)
        return layout

    def add_circle(self):
        diameter = random.randint(20, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        circle = Circle(diameter, color)

        brush = QBrush(circle.color)

        ellipse = self.scene.addEllipse(0, 0, circle.diameter, circle.diameter)
        ellipse.setBrush(brush)

        self.scene.setSceneRect(0, 0, circle.diameter + 10, circle.diameter + 10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
