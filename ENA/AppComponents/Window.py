from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QGuiApplication
import sys

from AppComponents.Colors import *
from AppComponents.NavBar import create_navbar
from AppComponents.OptionBar import create_option_bar

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
        self.background_widget.setObjectName("background-widget")

        main_vertical_layout = QVBoxLayout()
        main_horizontal_layout = QHBoxLayout()

        self.background_widget.setGeometry(0, 0, self.window_width, self.window_height)
        self.background_widget.setStyleSheet(f"""
            #background-widget {{
                background-color: {CATPPUCCIN['base']};
                border-radius: 15px;
                border: 4px solid {CATPPUCCIN['mauve']}
            }}
        """)

        navbar = create_navbar(self)
        left_navbar = create_option_bar(self)

        main_vertical_layout.addWidget(navbar)

        main_horizontal_layout.addWidget(left_navbar)
        main_horizontal_layout.addStretch()
        main_vertical_layout.addLayout(main_horizontal_layout)
        self.background_widget.setLayout(main_vertical_layout)


    def center_window(self):
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        x = (screen_geometry.width() - self.window_width) // 2
        y = (screen_geometry.height() - self.window_height) // 2
        self.move(QPoint(x, y))


