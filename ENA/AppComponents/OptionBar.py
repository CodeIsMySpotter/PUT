import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont

from AppComponents.Colors import *



def create_option_bar(parent):
  option_bar = QWidget()
  option_bar.setFixedWidth(200)
  option_bar.setFixedHeight(parent.window_height - 120)


  option_bar_layout = QVBoxLayout(option_bar)
  option_bar_layout.setContentsMargins(10, 10, 10, 10)
  option_bar_layout.setSpacing(20)


  option_bar.setObjectName("option-bar")
  
  return option_bar



def create_option_button_I():
  pass


def create_option_button_II():
  pass


def creater_option_button_III():
  pass

