import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QFileDialog, QLabel, QSlider


class  AlphaManagement(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100,100,400,500)
        self.image_label = QLabel(self)
        pixmap = QPixmap('orig.jpg')
        self.image_label.setPixmap(pixmap)

        self.alpha = QSlider(Qt.Vertical)
        self.alpha.setMinimum(0)
        self.alpha.setMaximum(255)
        self.alpha.setValue(255)
        self.alpha.valueChanged.connect(self.on_slider_value_changed)
    def on_slider_value_changed(self):
        image = self.image_label.pixmap().toImage()
        image.setAlphaChannel(self.alpha.value())
        pixmap = QPixmap.fromImage(image)
        self.image_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AlphaManagement()
    ex.show()
    sys.exit(app.exec_())
