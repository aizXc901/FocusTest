import io
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QMessageBox


class StartGame(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/start_win.ui', self)
        self.startButton.clicked.connect(self.open_choose_game)

    def open_choose_game(self):
        self.choose_game = ChooseGame()
        self.choose_game.show()
        self.close()

class ChooseGame(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/choose_win.ui', self)
        self.coloursButton.clicked.connect(self.open_colours_instructuion)
        self.wordsButton.clicked.connect(self.open_words_instructuion)
        self.colours_wordsButton.clicked.connect(self.open_colours_words_instructuion)

    def open_colours_instructuion(self):
        self.colours_instructuion = coloursInstruction()
        self.colours_instructuion.show()
        self.close()

    def open_words_instructuion(self):
        self.words_instructuion = wordsInstruction()
        self.words_instructuion.show()
        self.close()

    def open_colours_words_instructuion(self):
        self.colours_words_instructuion = colours_wordsInstruction()
        self.colours_words_instructuion.show()
        self.close()

class coloursInstruction(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/colours_instruct_win.ui', self)
        self.continue_coloursButton.clicked.connect(self.open_difficulty_level_colours)

    def open_difficulty_level_colours(self):
        self.difficulty_level_colours = DifficultylevelColours()
        self.difficulty_level_colours.show()
        self.close()

class wordsInstruction(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/words_instruct_win.ui', self)
        self.continue_wordsButton.clicked.connect(self.open_difficulty_level_words)

    def open_difficulty_level_words(self):
        self.difficulty_level_words = DifficultylevelWords()
        self.difficulty_level_words.show()
        self.close()


class colours_wordsInstruction(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/colours&words_instruct_win.ui', self)
        self.continue_colours_wordsButton.clicked.connect(self.open_difficulty_level_colours_words)

    def open_difficulty_level_colours_words(self):
        self.difficulty_level_colours_words = DifficultylevelColoursWords()
        self.difficulty_level_colours_words.show()
        self.close()

class DifficultylevelColours(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/dif_level_colours_win.ui', self)
        self.startColoursButton.clicked.connect(self.check_selection)

    def check_selection(self):
        if self.easyColoursButton.isChecked():
            self.easy_level_colours = EasylevelColours()
            self.easy_level_colours.show()
            self.close()
        elif self.mediumColoursButton.isChecked():
            self.medium_level_colours = MediumlevelColours()
            self.medium_level_colours.show()
            self.close()
        elif self.difficultColoursButton.isChecked():
            self.difficult_level_colours = DifficultlevelColours()
            self.difficult_level_colours.show()
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите уровень сложности.")

class DifficultylevelWords(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/dif_level_words_win.ui', self)
        self.startWordsButton.clicked.connect(self.check_selection)

    def check_selection(self):
        if self.easyWordsButton.isChecked():
            self.easy_level_words = EasylevelWords()
            self.easy_level_words.show()
            self.close()
        elif self.mediumWordsButton.isChecked():
            self.medium_level_words = MediumlevelWords()
            self.medium_level_words.show()
            self.close()
        elif self.difficultWordsButton.isChecked():
            self.difficult_level_words = DifficultlevelWords()
            self.difficult_level_words.show()
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите уровень сложности.")

class DifficultylevelColoursWords(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/dif_level_colours&words_win.ui', self)
        self.startColoursWordsButton.clicked.connect(self.check_selection)

    def check_selection(self):
        if self.easyColoursWordsButton.isChecked():
            self.easy_level_colours_words = EasylevelColoursWords()
            self.easy_level_colours_words.show()
            self.close()
        elif self.mediumColoursWordsButton.isChecked():
            self.medium_level_colours_words = MediumlevelColoursWords()
            self.medium_level_colours_words.show()
            self.close()
        elif self.difficultColoursWordsButton.isChecked():
            self.difficult_level_colours_words = DifficultlevelColoursWords()
            self.difficult_level_colours_words.show()
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите уровень сложности.")

class EasylevelWords(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/words_easy_win.ui', self)

class MediumlevelWords(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/words_medium_win.ui', self)

class DifficultlevelWords(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/words_difficult_win.ui', self)

class EasylevelColours(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/colours_easy_win.ui', self)

class MediumlevelColours(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/colours_medium_win.ui', self)

class DifficultlevelColours(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/colours_difficult_win.ui', self)

class EasylevelColoursWords(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/colours&words_easy_win.ui', self)

class MediumlevelColoursWords(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/colours&words_medium_win.ui', self)

class DifficultlevelColoursWords(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/colours&words_difficult_win.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartGame()
    ex.show()
    sys.exit(app.exec())
