from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QGuiApplication
import sys

from AppComponents.Colors import *
from AppComponents.NavBar import create_navbar

class Application(QMainWindow):
    def __init__(self):
        super().__init__()

        self.background_widget = None
        self.main_widget = None

        self.window_width = 1400
        self.window_height = 800

        self.init_window()
        self.create_main_widget()
        self.create_background_widget()
        self.center_window()

    def init_window(self):
        self.setWindowTitle("ENA Application")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(100, 100, self.window_width, self.window_height)

    def create_main_widget(self):
        self.main_widget = QWidget(self)
        self.main_widget.setStyleSheet("background-color: transparent;")
        self.setCentralWidget(self.main_widget)
    
    def create_background_widget(self):
        self.background_widget = QWidget(self.main_widget)
        self.background_widget.setGeometry(0, 0, self.window_width, self.window_height)
        self.background_widget.setStyleSheet(f"""
            background-color: {CATPPUCCIN['base']};
            border-radius: 15px;
            border: 4px solid {CATPPUCCIN['mauve']}
        """)

    def center_window(self):
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        x = (screen_geometry.width() - self.window_width) // 2
        y = (screen_geometry.height() - self.window_height) // 2
        self.move(QPoint(x, y))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())
