from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit
from PyQt5.QtCore import Qt, QPoint, QProcess
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
        self.optype_label = None
        self.x_input = None
        self.y_input = None
        self.point_input = None
        self.output_field = None

        self.process = None


        self.optype_I = "Floating point arithmetics (float128)"
        self.optype_II = "Floating point to interval"
        self.optype_III = "Interval arithmetics"

        self.input_I = "3.14; 1.61 ..."
        self.input_II = "3.14; 1.61 ..."
        self.input_III = "[3.13, 3.15]; ..."

        self.point_input_I = "3.14"
        self.point_input_II = "3.14"
        self.point_input_III = "[3.13, 3.15]"

        self.output_text = ""
        
        self.option_I = None
        self.option_II = None
        self.option_III = None

        self.window_width = 1400
        self.window_height = 800
        self.op_signal = 1

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
        self.option_I.clicked.connect(self.callback_option_I)
        self.option_II = create_option_button_II()
        self.option_II.clicked.connect(self.callback_option_II)
        self.option_III = creater_option_button_III()
        self.option_III.clicked.connect(self.callback_option_III)

        option_bar_layout.addStretch()
        option_bar_layout.addWidget(self.option_I)
        option_bar_layout.addWidget(self.option_II)
        option_bar_layout.addWidget(self.option_III)
        option_bar_layout.addStretch()

    
    def create_central_widget(self):
        width = self.window_width - self.option_bar.width() - 100
        height = self.window_height - self.navbar.height() - 100

        
        self.central_widget = QWidget()
        self.central_widget.setFixedWidth(width)
        self.central_widget.setFixedHeight(height)
        
        self.optype_label = QLabel()
        self.optype_label.setText(self.optype_I)
        self.optype_label.setObjectName("optype-label")
        self.optype_label.setStyleSheet(f"""
            #optype-label{{
                font-size: 28px;
                font-weight: bold;
                color: {CATPPUCCIN['red']};
                background-color: {CATPPUCCIN['base']};
                padding: 10px;
            }}
        """)

        central_widget_layout = QVBoxLayout()
        central_widget_horizontal_layout = QHBoxLayout()
        input_fields_vertical_layout = QVBoxLayout()


        X_label = QLabel("Enter X values")
        Y_label = QLabel("Enter Y values")
        point_label = QLabel("Enter point")
        self.output_field = QTextEdit()


        X_label.setObjectName("type-label")
        Y_label.setObjectName("type-label")
        point_label.setObjectName("type-label")
        self.output_field.setObjectName("output-field")

        X_label.setStyleSheet(f"""
            #type-label{{
                font-size: 24px;
                font-weight: lighter;
                color: {CATPPUCCIN['text']};
                background-color: {CATPPUCCIN['base']};
                padding: 10px;
            }}
        """)

        Y_label.setStyleSheet(f"""
            #type-label{{
                font-size: 24px;
                font-weight: lighter;
                color: {CATPPUCCIN['text']};
                background-color: {CATPPUCCIN['base']};
                padding: 10px;
            }}
        """)

        point_label.setStyleSheet(f"""
            #type-label{{
                font-size: 24px;
                font-weight: lighter;
                color: {CATPPUCCIN['text']};
                background-color: {CATPPUCCIN['base']};
                padding: 10px;
            }}
        """)

        self.x_input = QLineEdit()
        self.y_input = QLineEdit()
        self.point_input = QLineEdit()
        calc_button = QPushButton("Calculate")


        self.x_input.setFixedSize(300, 65)
        self.y_input.setFixedSize(300, 65)
        self.point_input.setFixedSize(300, 65)
        calc_button.setFixedSize(300, 65)
        self.output_field.setFixedSize(self.central_widget.width() - 350, 475)

        self.x_input.setObjectName("input")
        self.y_input.setObjectName("input")
        self.point_input.setObjectName("input")
        calc_button.setObjectName("calc-button")

        self.x_input.setStyleSheet(f"""
            #input {{
                color: {CATPPUCCIN['text']};
                border: 4px solid {CATPPUCCIN['text']};
                border-radius: 15px;
                padding: 6px;
                font-size: 14px;
            }}
            #input:focus {{
                border: 4px solid {CATPPUCCIN['red']};
            }}
        """)

        self.y_input.setStyleSheet(f"""
            #input {{
                color: {CATPPUCCIN['text']};
                border: 4px solid {CATPPUCCIN['text']};
                border-radius: 15px;
                padding: 6px;
                font-size: 14px;
            }}
            #input:focus {{
                border: 4px solid {CATPPUCCIN['red']};
            }}
        """)

        self.point_input.setStyleSheet(f"""
            #input {{
                color: {CATPPUCCIN['text']};
                border: 4px solid {CATPPUCCIN['text']};
                border-radius: 15px;
                padding: 6px;
                font-size: 14px;
            }}
            #input:focus {{
                border: 4px solid {CATPPUCCIN['red']};
            }}
        """)

        calc_button.setStyleSheet(f"""
            #calc-button{{
                color: {CATPPUCCIN['red']};
                font-size: 14px;
                padding: 6px;
                background-color: {CATPPUCCIN["base"]};
                border-radius: 15px;
                border: 4px solid {CATPPUCCIN["red"]};
                font-weight: bold;
                font-size: 16px;
            }}
            #calc-button:hover {{
                border: 8px solid {CATPPUCCIN["red"]};
            }}
        """)

        self.output_field.setStyleSheet(f"""
            #output-field{{
                border-radius: 15px;
                border: 4px solid {CATPPUCCIN['text']}
            }}
        """)

        self.x_input.setPlaceholderText(self.input_I)
        self.y_input.setPlaceholderText(self.input_I)
        self.point_input.setPlaceholderText(self.point_input_I)
        self.output_field.setReadOnly(True)

        input_fields_vertical_layout.addWidget(X_label, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        input_fields_vertical_layout.addWidget(self.x_input, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        input_fields_vertical_layout.addWidget(Y_label, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        input_fields_vertical_layout.addWidget(self.y_input, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        input_fields_vertical_layout.addWidget(point_label, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        input_fields_vertical_layout.addWidget(self.point_input, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        input_fields_vertical_layout.addWidget(calc_button, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        input_fields_vertical_layout.addStretch()

        central_widget_horizontal_layout.addLayout(input_fields_vertical_layout)
        central_widget_horizontal_layout.addStretch()
        central_widget_horizontal_layout.addWidget(self.output_field, alignment=Qt.AlignmentFlag.AlignTop)
    
        central_widget_layout.addWidget(self.optype_label, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        central_widget_layout.addLayout(central_widget_horizontal_layout)

        self.central_widget.setLayout(central_widget_layout)

    def callback_option_I(self):
        self.optype_label.setText(self.optype_I)
        self.op_signal = 1

        self.x_input.setPlaceholderText(self.input_I)
        self.y_input.setPlaceholderText(self.input_I)
        self.point_input.setPlaceholderText(self.point_input_I)

    def callback_option_II(self):
        self.optype_label.setText(self.optype_II)
        self.op_signal = 2

        self.x_input.setPlaceholderText(self.input_II)
        self.y_input.setPlaceholderText(self.input_II)
        self.point_input.setPlaceholderText(self.point_input_II)

    def callback_option_III(self):
        self.optype_label.setText(self.optype_III)
        self.op_signal = 3

        self.x_input.setPlaceholderText(self.input_III)
        self.y_input.setPlaceholderText(self.input_III)
        self.point_input.setPlaceholderText(self.point_input_III)

    def callback_cal(self):
        self.output_field.clear()
        self.process = QProcess()
        self.process.start("./Arithmetics/calc.exe")

    def process_arguments(self):
        x_args = self.x_input.text()
        y_args = self.y_input.text()
        point = self.point_input.text()

        

    def handle_stdout(self):
        data = self.process.readAllStandardOutput()
        text = bytes(data).decode('utf8')
        self.output_field.append(text)

    def handle_stderr(self):
        data = self.process.readAllStandardError()
        text = bytes(data).decode('utf8')
        self.output_field.append(f"<span style='color:red;'>{text}</span>")

    def handle_finish(self):
        self.output_field.append("Program finished succesfully")
    


    def center_window(self):
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        x = (screen_geometry.width() - self.window_width) // 2
        y = (screen_geometry.height() - self.window_height) // 2
        self.move(QPoint(x, y))


