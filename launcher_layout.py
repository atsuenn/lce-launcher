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
        if launcher_logic.check_if_installed() == True:
            main_btn = QPushButton("Play")
            main_btn.clicked.connect(launcher_logic.launch_game)
        else:
            main_btn = QPushButton("Install")
            main_btn.clicked.connect(launcher_logic.install_game)
            main_btn.clicked.connect(self.update_ui)
        main_btn.setFixedSize(150, 50)
        font.setPointSize(16)
        main_btn.setFont(font)

        self.main_btn = main_btn
            
        version = QLabel("v1.0")

        self.update = QPushButton("Update")
        self.update.setFixedSize(125, 40)
        font.setPointSize(12)
        self.update.setFont(font)

        mainlayout.addWidget(title, alignment=Qt.AlignCenter)
        innerlayout.addWidget(main_btn, alignment=Qt.AlignCenter)
        innerlayout.addWidget(self.update, alignment=Qt.AlignCenter)
        if launcher_logic.check_if_installed() == False:
            self.update.hide()

        mainlayout.addLayout(innerlayout)
        mainlayout.addWidget(version, alignment=Qt.AlignBottom | Qt.AlignLeft)

        self.setLayout(mainlayout)
    
    def update_ui(self):
        self.update.show()
        self.main_btn.text()