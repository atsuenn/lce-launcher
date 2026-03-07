from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt
import launcher_logic

class Launcher(QWidget):
    def __init__(self):
        super().__init__()

        mainlayout = QVBoxLayout()
        innerlayout = QVBoxLayout()

        title = QLabel("Minecraft LCE")
        font = title.font()
        font.setPointSize(40)
        title.setFont(font)

        main_btn = QPushButton()
        if launcher_logic.check_if_installed == True:
            main_btn = QPushButton("Play")
            main_btn.clicked.connect(launcher_logic.launch_game)
        else:
            main_btn = QPushButton("Install")
            main_btn.clicked.connect(launcher_logic.install_game)
        main_btn.setFixedSize(150, 50)
        font.setPointSize(16)
        main_btn.setFont(font)
        
        version = QLabel("v1.0")

        update = QPushButton("Update")
        update.setFixedSize(125, 40)
        font.setPointSize(12)
        update.setFont(font)

        mainlayout.addWidget(title, alignment=Qt.AlignCenter)
        innerlayout.addWidget(main_btn, alignment=Qt.AlignCenter)
        if launcher_logic.check_if_installed == True:
            innerlayout.addWidget(update, alignment=Qt.AlignCenter)
        mainlayout.addLayout(innerlayout)
        mainlayout.addWidget(version, alignment=Qt.AlignBottom | Qt.AlignLeft)

        self.setLayout(mainlayout)