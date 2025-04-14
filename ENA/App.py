
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
import sys
import os

from AppComponents.NavBar import NavBar

class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)


        self.setWindowTitle("ENA Application")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(100, 100, 800, 600)
        

    def setup_style(self):
        self.styleSheet = """
        QMainWindow {
            background-color: transparent;
            border-radius: 10px;
        }
        """
        self.setStyleSheet(self.styleSheet)

    def setup_main_widget(self):
        self.layout = QVBoxLayout(self.main_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.navbar = NavBar(self.main_widget)
        self.layout.addWidget(self.navbar)

        self.content_area = QWidget(self.main_widget)
        self.content_area.setStyleSheet("background-color: #3B4252;")
        self.layout.addWidget(self.content_area)

        self.label = QLabel("Welcome to ENA", self.content_area)
        self.label.setFont(QFont("Arial", 24))
        self.label.setStyleSheet("color: #D8DEE9;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(0, 0, 800, 600)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())