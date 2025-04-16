import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont

from AppComponents.Colors import *

BUTTON_WIDTH = 80
BUTTON_HEIGHT = 80


def create_option_bar(parent):
  option_bar = QWidget()
  option_bar.setFixedWidth(200)
  option_bar.setFixedHeight(parent.window_height- 180)


  option_bar_layout = QVBoxLayout(option_bar)
  option_bar_layout.setContentsMargins(10, 10, 10, 10)
  option_bar_layout.setSpacing(20)


  option_bar_layout.addStretch()
  option_bar_layout.addWidget(create_option_button_I())
  option_bar_layout.addWidget(create_option_button_II())
  option_bar_layout.addWidget(creater_option_button_III())
  option_bar_layout.addStretch()


  option_bar.setObjectName("option-bar")

  
  return option_bar



def create_option_button_I():
  button = QPushButton()
  button.setObjectName("option-button-I")
  button.setFixedWidth(BUTTON_WIDTH)
  button.setFixedHeight(BUTTON_HEIGHT)
  button.setStyleSheet(f"""
      #option-button-I{{
          background-color: {CATPPUCCIN["base"]};
          border-radius: 6px;
          border: 2px solid {CATPPUCCIN["red"]};
          font-weight: bold;
          font-size: 16px;
      }}
      #option-button-I:hover {{
          background-color: {CATPPUCCIN["maroon"]};
      }}
  """)

  return button


def create_option_button_II():
  button = QPushButton()
  button.setObjectName("option-button-II")
  button.setFixedWidth(BUTTON_WIDTH)
  button.setFixedHeight(BUTTON_HEIGHT)
  button.setStyleSheet(f"""
      #option-button-II{{
          background-color: {CATPPUCCIN["base"]};
          border-radius: 6px;
          border: 2px solid {CATPPUCCIN["red"]};
          font-weight: bold;
          font-size: 16px;
      }}
      #option-button-II:hover {{
          background-color: {CATPPUCCIN["maroon"]};
      }}
  """)

  return button


def creater_option_button_III():
  button = QPushButton()
  button.setObjectName("option-button-III")
  button.setFixedWidth(BUTTON_WIDTH)
  button.setFixedHeight(BUTTON_HEIGHT)
  button.setStyleSheet(f"""
      #option-button-III{{
          background-color: {CATPPUCCIN["base"]};
          border-radius: 6px;
          border: 2px solid {CATPPUCCIN["red"]};
          font-weight: bold;
          font-size: 16px;
      }}
      #option-button-III:hover {{
          background-color: {CATPPUCCIN["maroon"]};
      }}
  """)

  return button



