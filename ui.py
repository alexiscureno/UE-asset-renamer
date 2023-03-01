import sys
import unreal
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QCheckBox
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QSize
from PyQt5.QtGui import QImage, QPixmap, QMouseEvent
from PyQt5 import uic, QtCore


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("asset-renamer-ui.ui", self)

        # LineEdits
        self.replace_le = self.findChild(QLineEdit, "lineEdit")
        self.with_le = self.findChild(QLineEdit, "lineEdit_2")

        # Checkbox
        self.case_check = self.findChild(QCheckBox, "checkBox")

        # Buttons
        self.ok_bttn = self.findChild(QPushButton, "pushButton")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
