import io
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit

class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pj_qt1.ui', self)
        self.startButton.clicked.connect(self.open_second_window)

    def open_second_window(self):
        self.second_window = SecondWindow()
        self.second_window.show()
        self.close()

class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pj_qt2.ui', self)
        self.coloursButton.clicked.connect(self.open_third_window)

    def open_third_window(self):  # Поменяйте название метода
        self.third_window = ThirdWindow()
        self.third_window.show()
        self.close()

class ThirdWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pj_qt3.ui', self)
        self.continueButton.clicked.connect(self.open_fourth_window)

    def open_fourth_window(self):
        self.fourth_window = FourthWindow()
        self.fourth_window.show()
        self.close()

class FourthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pj_qt4.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec())

