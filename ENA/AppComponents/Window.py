from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QGuiApplication
import sys

from AppComponents.Colors import *
from AppComponents.NavBar import *
from AppComponents.OptionBar import *

class Application(QMainWindow):
    def __init__(self):
        super().__init__()

        self.background_widget = None
        self.main_widget = None
        self.option_bar = None
        self.central_widget = None
        self.navbar = None
        
        self.option_I = None
        self.option_II = None
        self.option_III = None

        self.window_width = 1400
        self.window_height = 800

        self.init_window()

        self.create_navbar()
        self.create_option_bar()
        self.create_central_widget()

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

        main_vertical_layout.addWidget(self.navbar)
        main_horizontal_layout.addWidget(self.option_bar)
        main_horizontal_layout.addWidget(self.central_widget)
        main_horizontal_layout.addStretch()
        main_vertical_layout.addLayout(main_horizontal_layout)
        main_vertical_layout.addStretch()
        self.background_widget.setLayout(main_vertical_layout)

    def create_navbar(self):
        self.navbar = QWidget()
        self.navbar.setObjectName("navbar-widget")
        self.navbar.setGeometry(0, 0, self.window_width, 75)
        navbar_layout = QHBoxLayout(self.navbar)
        
        title_label = create_title_label()
        close_button = create_close_button(self)
        minimize_button = create_minimize_button(self)
        icon = create_app_icon()

        navbar_layout.addWidget(icon, alignment=Qt.AlignLeft)
        navbar_layout.addWidget(title_label)
        navbar_layout.addStretch()
        navbar_layout.addWidget(minimize_button)
        navbar_layout.addWidget(close_button)
        
        navbar_layout.setContentsMargins(20, 10, 10, 10) 
        navbar_layout.setSpacing(20)


    def create_option_bar(self):
        self.option_bar = QWidget()
        self.option_bar.setFixedWidth(150)
        self.option_bar.setFixedHeight(self.window_height- 180)

        option_bar_layout = QVBoxLayout(self.option_bar)
        option_bar_layout.setContentsMargins(20, 10, 10, 10)
        option_bar_layout.setSpacing(20)

        self.option_I = create_option_button_I()
        self.option_II = create_option_button_II()
        self.option_III = creater_option_button_III()

        option_bar_layout.addStretch()
        option_bar_layout.addWidget(self.option_I)
        option_bar_layout.addWidget(self.option_II)
        option_bar_layout.addWidget(self.option_III)
        option_bar_layout.addStretch()

    
    def create_central_widget(self):
        width = self.window_width - self.option_bar.width() - 100
        height = self.window_height - self.navbar.height() - 100

        print(width, height)
        self.central_widget = QWidget()
        self.central_widget.setFixedWidth(width)
        self.central_widget.setFixedHeight(height)
        self.central_widget.setStyleSheet("""
            background-color: white;
        """)


    


    def center_window(self):
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        x = (screen_geometry.width() - self.window_width) // 2
        y = (screen_geometry.height() - self.window_height) // 2
        self.move(QPoint(x, y))


