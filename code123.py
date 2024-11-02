import io
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit

class StartGame(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('start_win.ui', self)
        self.startButton.clicked.connect(self.open_choose_game)

    def open_choose_game(self):
        self.choose_game = ChooseGame()
        self.choose_game.show()
        self.close()

class ChooseGame(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('choose_win.ui', self)
        self.coloursButton.clicked.connect(self.open_colours_instructuion)

    def open_colours_instructuion(self):
        self.colours_instructuion = coloursInstruction()
        self.colours_instructuion.show()
        self.close()

class coloursInstruction(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('colours_instruct_win.ui', self)
        self.continueButton.clicked.connect(self.open_difficulty_level_colours)

    def open_difficulty_level_colours(self):
        self.difficulty_level_colours = DifficultylevelColours()
        self.difficulty_level_colours.show()
        self.close()

class DifficultylevelColours(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('dif_level_colours_win.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartGame()
    ex.show()
    sys.exit(app.exec())

