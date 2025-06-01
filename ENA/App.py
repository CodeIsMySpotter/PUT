
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from AppComponents.Window import Application
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./AppComponents/icons/logo.png"))
    window = Application()
    window.show()
    sys.exit(app.exec_())

# D:/IT/SCOOP/apps/python310/3.10.11/python.exe d:/IT/UNIVERSITY/GITHUB/PUT/ENA/App.py