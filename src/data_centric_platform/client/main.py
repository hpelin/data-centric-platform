import sys
from PyQt5.QtWidgets import QApplication
from welcome_window import WelcomeWindow

import warnings
warnings.simplefilter('ignore')

import settings
settings.init()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WelcomeWindow()
    sys.exit(app.exec())