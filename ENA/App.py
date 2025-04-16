
from PyQt5.QtWidgets import QApplication

from AppComponents.Window import Application
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())
