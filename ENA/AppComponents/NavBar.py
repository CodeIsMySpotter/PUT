import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont

from AppComponents.Colors import *


def create_title_label():
    label = QLabel("Lagrange interpolation")
    label.setObjectName("title-label")
    label.setStyleSheet(f"""
        #title-label{{
            font-size: 28px;
            font-weight: bold;
            color: {CATPPUCCIN['text']};
            background-color: {CATPPUCCIN['base']};
            padding: 10px;
        }}
    """)
    
    return label

def create_navbar(parent):
    navbar_widget = QWidget()
    navbar_widget.setGeometry(0, 0, parent.window_width, 75)
    navbar_layout = QHBoxLayout(navbar_widget)
    navbar_widget.setObjectName("navbar-widget")
    
    title_label = create_title_label()
    close_button = create_close_button(parent)
    minimize_button = create_minimize_button(parent)
    icon = create_app_icon()

    navbar_layout.addWidget(icon, alignment=Qt.AlignLeft)
    navbar_layout.addWidget(title_label)
    navbar_layout.addStretch()
    navbar_layout.addWidget(minimize_button)
    navbar_layout.addWidget(close_button)
    
    navbar_layout.setContentsMargins(10, 10, 10, 10) 
    navbar_layout.setSpacing(20)
    return navbar_widget



def create_close_button(window):
    button = QPushButton()
    button.setObjectName("close-button")

    button.setFixedWidth(50)
    button.setFixedHeight(50)

    button.setStyleSheet(f"""
        #close-button{{
            border: 2px solid {CATPPUCCIN["red"]};
            border-radius: 6px;
            font-weight: bold;
            font-size: 16px;
        }}
        #close-button:hover {{
            background-color: {CATPPUCCIN["maroon"]};
        }}
       
    """)

    button.clicked.connect(lambda: QApplication.quit())

    return button

def create_minimize_button(window):
    button = QPushButton()
    button.setObjectName("minimize-button")
    
    button.setFixedWidth(50)
    button.setFixedHeight(50)

    button.setStyleSheet(f"""
        #minimize-button{{
            border: 2px solid {CATPPUCCIN["red"]};
            border-radius: 6px;
            font-weight: bold;
            font-size: 16px;
        }}
        #minimize-button:hover {{
            background-color: {CATPPUCCIN["maroon"]};
        }}
        
    """)

    button.clicked.connect(window.showMinimized)

    return button

def create_title_label():
    label = QLabel("Lagrange interpolation and Neville's algorithm")
    label.setObjectName("title-label")
    label.setStyleSheet(f"""
        #title-label{{
            font-size: 28px;
            font-weight: bold;
            color: {CATPPUCCIN['text']};
            background-color: {CATPPUCCIN['base']};
            padding: 10px;
        }}
    """)
    
    return label

def create_app_icon():
  icon = QLabel()

  icon.setObjectName("app-icon")
  icon.setPixmap(QIcon("./AppComponents/icons/logo.png").pixmap(80, 80))
  icon.setStyleSheet(f"""
      #app-icon{{
          background-color: {CATPPUCCIN['base']};
          border-radius: 6px;
          padding: 10px;
      }}
  """)

  return icon
