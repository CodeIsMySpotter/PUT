import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont

class NavBar(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #2E3440; color: #D8DEE9;")
        self.setWindowIcon(QIcon("icon.png"))

        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.label = QLabel("ENA Navigation Bar", self)
        self.label.setFont(QFont("Arial", 16))
        self.layout.addWidget(self.label)

        self.button1 = QPushButton("Home", self)
        self.button1.clicked.connect(self.on_home_click)
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton("Settings", self)
        self.button2.clicked.connect(self.on_settings_click)
        self.layout.addWidget(self.button2)

        self.button3 = QPushButton("About", self)
        self.button3.clicked.connect(self.on_about_click)
        self.layout.addWidget(self.button3)

    def on_home_click(self):
        print("Home button clicked")
        # Add functionality for home button click

    def on_settings_click(self):
        print("Settings button clicked")
        # Add functionality for settings button click

    def on_about_click(self):
        print("About button clicked")
        # Add functionality for about button click

