import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont

from AppComponents.Colors import *

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100
ICON_SIZE = 100



def create_option_button_I():
  button = QPushButton()
  button.setObjectName("option-button-I")
  button.setFixedWidth(BUTTON_WIDTH)
  button.setFixedHeight(BUTTON_HEIGHT)

  button.setIcon(QIcon("./AppComponents/icons/real_logo.png"))
  button.setIconSize(PyQt5.QtCore.QSize(ICON_SIZE, ICON_SIZE))

  button.setStyleSheet(f"""
      #option-button-I{{
          background-color: {CATPPUCCIN["base"]};
          border-radius: 15px;
          border: 4px solid {CATPPUCCIN["red"]};
          font-weight: bold;
          font-size: 16px;
      }}
      #option-button-I:hover {{
          border: 8px solid {CATPPUCCIN["red"]};
      }}
  """)

  return button



  


def create_option_button_II():
  button = QPushButton()
  button.setObjectName("option-button-II")
  button.setFixedWidth(BUTTON_WIDTH)
  button.setFixedHeight(BUTTON_HEIGHT)

  button.setIcon(QIcon("./AppComponents/icons/real_inter.png"))
  button.setIconSize(PyQt5.QtCore.QSize(ICON_SIZE, ICON_SIZE))    

  button.setStyleSheet(f"""
      #option-button-II{{
          background-color: {CATPPUCCIN["base"]};
          border-radius: 15px;
          border: 4px solid {CATPPUCCIN["red"]};
          font-weight: bold;
          font-size: 16px;
      }}
      #option-button-II:hover {{
          border: 8px solid {CATPPUCCIN["red"]};
      }}
  """)


  return button


def creater_option_button_III():
  button = QPushButton()
  button.setObjectName("option-button-III")
  button.setFixedWidth(BUTTON_WIDTH)
  button.setFixedHeight(BUTTON_HEIGHT)

  button.setIcon(QIcon("./AppComponents/icons/inter.png"))
  button.setIconSize(PyQt5.QtCore.QSize(ICON_SIZE, ICON_SIZE))  

  button.setStyleSheet(f"""
      #option-button-III{{
          background-color: {CATPPUCCIN["base"]};
          border-radius: 15px;
          border: 4px solid {CATPPUCCIN["red"]};
          font-weight: bold;
          font-size: 16px;
      }}
      #option-button-III:hover {{
          border: 8px solid {CATPPUCCIN["red"]};
      }}
  """)

  return button



