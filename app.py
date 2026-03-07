import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

from launcher_layout import Launcher

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("LCE Launcher")

        widget = (Launcher())
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.resize(600, 300)
window.show()
app.exec()