import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsScene, QGraphicsView
from PyQt5.uic import loadUi
from PyQt5.QtGui import QColor, QBrush, QPainter
from PyQt5.QtCore import Qt
import random


class Circle:
    def __init__(self, diameter):
        self.diameter = diameter


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('1_ui.ui', self)

        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)

        self.addButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(20, 100)
        circle = Circle(diameter)
        brush_color = QColor(Qt.yellow)
        brush = QBrush(brush_color)

        ellipse = self.scene.addEllipse(0, 0, diameter, diameter)
        ellipse.setBrush(brush)

        self.scene.setSceneRect(0, 0, diameter + 10, diameter + 10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
