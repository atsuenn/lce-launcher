import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QProgressBar)

from PySide6.QtCore import Qt

class Launcher(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Minecraft LCE Launcher")
        self.setFixedSize(600, 300)

        main_layout = QVBoxLayout()

        # title stuff
        title = QLabel("Minecraft LCE")
        title_font = title.font()
        title_font.setPointSize(32)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)

        # main btns
        play_button = QPushButton("Play")
        play_button.setFixedSize(150, 50)

        update_button = QPushButton("Update")
        update_button.setFixedSize(150, 50)

        # progress bar
        self.progress = QProgressBar()
        self.progress.setValue(0)
        self.progress.setFixedWidth(300)

        self.progress_subheading = QLabel()

        # centre layout for btns + progress
        center_layout = QVBoxLayout()
        center_layout.addWidget(play_button, alignment=Qt.AlignCenter)
        center_layout.addWidget(update_button, alignment=Qt.AlignCenter)

        # progress stuff
        center_layout.addWidget(self.progress, alignment=Qt.AlignCenter)
        center_layout.addWidget(self.progress_subheading, alignment=Qt.AlignCenter)


        # bottom sec.
        bottom_layout = QHBoxLayout()

        version = QLabel("v1.0")
        settings = QPushButton("Settings")
        
        bottom_layout.addWidget(version)
        bottom_layout.addStretch()
        bottom_layout.addWidget(settings)

        # assemble all dem
        main_layout.addWidget(title)
        main_layout.addStretch()
        main_layout.addLayout(center_layout)
        main_layout.addStretch()
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)
    
    def show_hide_progress(self, show_or_hide: bool):
        """Checks if True or False. \n
        If True, progress UI is shown, if False they are hidden.
        """
        print(show_or_hide)
        if show_or_hide:
            print("showing")
            self.progress.show()
            self.progress_subheading.show()
        elif not show_or_hide:
            print("hiding")
            self.progress.hide()
            self.progress_subheading.hide()


    def set_progress(self, value: int, subheading: str):
        """Sets the visual progress bar and subheading text."""
        self.progress.value(value)
        self.progress_subheading.text = subheading

if __name__ == '__main__':
    # create the app
    app = QApplication(sys.argv)

    # craete and show form
    form = Launcher()
    form.show()

    Launcher().show_hide_progress(False)

    # run the qt loop
    sys.exit(app.exec())