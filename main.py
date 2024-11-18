import sys
import random

from PyQt6 import uic
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel


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

        self.existing_words = ['кот', 'лист', 'дом', 'снег', 'век', 'шар', 'долг', 'друг', 'ток']
        self.attempts = 1
        self.scores = 0
        self.correct_sequence = []
        self.user_sequence = []

        self.pushButton_2.clicked.connect(lambda: self.on_word_clicked(self.pushButton_2))
        self.pushButton_4.clicked.connect(lambda: self.on_word_clicked(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.on_word_clicked(self.pushButton_5))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.start_new_game()

    def set_button_words(self, words):
        self.pushButton_2.setText(words[0])
        self.pushButton_4.setText(words[1])
        self.pushButton_5.setText(words[2])

    def start_new_game(self):
        self.correct_sequence = self.generate_random_sequence()
        self.user_sequence = []
        self.current_index = 0
        self.show_sequence()

    def generate_random_sequence(self):
        sequence = random.sample(self.existing_words, 3)
        return sequence

    def show_sequence(self):
        self.current_index = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.display_next_word)
        self.timer.start(700)
        self.enable_buttons(False)

    def display_next_word(self):
        if self.current_index < len(self.correct_sequence):
            self.label_14.setText(self.correct_sequence[self.current_index])
            self.current_index += 1
        else:
            self.timer.stop()
            self.enable_buttons(True)
            shuffled_sequence = self.correct_sequence[:]
            random.shuffle(shuffled_sequence)
            self.set_button_words(shuffled_sequence)
            self.update_interface()

    def enable_buttons(self, enable):
        self.pushButton_2.setEnabled(enable)
        self.pushButton_4.setEnabled(enable)
        self.pushButton_5.setEnabled(enable)

    def on_word_clicked(self, button):
        word = button.text().lower()
        self.user_sequence.append(word)
        if len(self.user_sequence) == len(self.correct_sequence):
            if self.user_sequence == self.correct_sequence:
                self.scores += 1
                self.show_message("Правильно!", "Вы выбрали правильную последовательность слов.")
            else:
                self.show_message("Неправильно!", "Кажется, вы ошиблись.")
                self.add_to_attempts_table(self.attempts, self.scores)
                self.scores = 0
                self.attempts += 1
            self.start_new_game()
            self.user_sequence = []

        self.update_interface()

    def update_interface(self):
        self.score.setText(f"Счет: {self.scores}")
        self.attempt.setText(f"Попытка № {self.attempts}")

    def show_message(self, title, text):
        QMessageBox.information(self, title, text)

    def add_to_attempts_table(self, attempt_num, score_num):
        form_layout = self.formLayout
        if self.attempts > 13:
            form_layout.removeRow(0)
        attempt_label = QLabel(f"Попытка #{attempt_num}")
        score_label = QLabel(f"Счет: {score_num}")
        attempt_label.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        score_label.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        form_layout.addRow(attempt_label, score_label)

class MediumlevelWords(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/words_medium_win.ui', self)

        self.existing_words = ['город', 'песок', 'солнце', 'вода', 'книга', 'пламя', 'лампа', 'птица', 'туча']
        self.attempts = 1
        self.scores = 0
        self.correct_sequence = []
        self.user_sequence = []

        self.pushButton_2.clicked.connect(lambda: self.on_word_clicked(self.pushButton_2))
        self.pushButton.clicked.connect(lambda: self.on_word_clicked(self.pushButton))
        self.pushButton_4.clicked.connect(lambda: self.on_word_clicked(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.on_word_clicked(self.pushButton_5))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.start_new_game()

    def set_button_words(self, words):
        self.pushButton_2.setText(words[0])
        self.pushButton.setText(words[1])
        self.pushButton_4.setText(words[2])
        self.pushButton_5.setText(words[3])

    def start_new_game(self):
        self.correct_sequence = self.generate_random_sequence()
        self.user_sequence = []
        self.current_index = 0
        self.show_sequence()

    def generate_random_sequence(self):
        sequence = random.sample(self.existing_words, 4)
        return sequence

    def show_sequence(self):
        self.current_index = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.display_next_word)
        self.timer.start(700)
        self.enable_buttons(False)

    def display_next_word(self):
        if self.current_index < len(self.correct_sequence):
            self.label_14.setText(self.correct_sequence[self.current_index])
            self.current_index += 1
        else:
            self.timer.stop()
            self.enable_buttons(True)
            shuffled_sequence = self.correct_sequence[:]
            random.shuffle(shuffled_sequence)
            self.set_button_words(shuffled_sequence)
            self.update_interface()

    def enable_buttons(self, enable):
        self.pushButton_2.setEnabled(enable)
        self.pushButton.setEnabled(enable)
        self.pushButton_4.setEnabled(enable)
        self.pushButton_5.setEnabled(enable)

    def on_word_clicked(self, button):
        word = button.text().lower()
        self.user_sequence.append(word)
        if len(self.user_sequence) == len(self.correct_sequence):
            if self.user_sequence == self.correct_sequence:
                self.scores += 1
                self.show_message("Правильно!", "Вы выбрали правильную последовательность слов.")
            else:
                self.show_message("Неправильно!", "Кажется, вы ошиблись.")
                self.add_to_attempts_table(self.attempts, self.scores)
                self.scores = 0
                self.attempts += 1
            self.start_new_game()
            self.user_sequence = []

        self.update_interface()

    def update_interface(self):
        self.score.setText(f"Счет: {self.scores}")
        self.attempt.setText(f"Попытка № {self.attempts}")

    def show_message(self, title, text):
        QMessageBox.information(self, title, text)

    def add_to_attempts_table(self, attempt_num, score_num):
        form_layout = self.formLayout
        if self.attempts > 13:
            form_layout.removeRow(0)
        attempt_label = QLabel(f"Попытка #{attempt_num}")
        score_label = QLabel(f"Счет: {score_num}")
        attempt_label.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        score_label.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        form_layout.addRow(attempt_label, score_label)

class DifficultlevelWords(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/words_difficult_win.ui', self)

        self.existing_words = ['коробка', 'известие', 'платформа', 'компьютер', 'картинка', 'площадка',
                               'партизан', 'господин', 'календарь']
        self.attempts = 1
        self.scores = 0
        self.correct_sequence = []
        self.user_sequence = []

        self.pushButton_2.clicked.connect(lambda: self.on_word_clicked(self.pushButton_2))
        self.pushButton.clicked.connect(lambda: self.on_word_clicked(self.pushButton))
        self.pushButton_4.clicked.connect(lambda: self.on_word_clicked(self.pushButton_4))
        self.pushButton_6.clicked.connect(lambda: self.on_word_clicked(self.pushButton_6))
        self.pushButton_5.clicked.connect(lambda: self.on_word_clicked(self.pushButton_5))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.start_new_game()

    def set_button_words(self, words):
        self.pushButton_2.setText(words[0])
        self.pushButton.setText(words[1])
        self.pushButton_6.setText(words[2])
        self.pushButton_4.setText(words[3])
        self.pushButton_5.setText(words[4])

    def start_new_game(self):
        self.correct_sequence = self.generate_random_sequence()
        self.user_sequence = []
        self.current_index = 0
        self.show_sequence()

    def generate_random_sequence(self):
        sequence = random.sample(self.existing_words, 5)
        return sequence

    def show_sequence(self):
        self.current_index = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.display_next_word)
        self.timer.start(700)
        self.enable_buttons(False)

    def display_next_word(self):
        if self.current_index < len(self.correct_sequence):
            self.label_14.setText(self.correct_sequence[self.current_index])
            self.current_index += 1
        else:
            self.timer.stop()
            self.enable_buttons(True)
            shuffled_sequence = self.correct_sequence[:]
            random.shuffle(shuffled_sequence)
            self.set_button_words(shuffled_sequence)
            self.update_interface()

    def enable_buttons(self, enable):
        self.pushButton_2.setEnabled(enable)
        self.pushButton.setEnabled(enable)
        self.pushButton_6.setEnabled(enable)
        self.pushButton_4.setEnabled(enable)
        self.pushButton_5.setEnabled(enable)

    def on_word_clicked(self, button):
        word = button.text().lower()
        self.user_sequence.append(word)
        if len(self.user_sequence) == len(self.correct_sequence):
            if self.user_sequence == self.correct_sequence:
                self.scores += 1
                self.show_message("Правильно!", "Вы выбрали правильную последовательность слов.")
            else:
                self.show_message("Неправильно!", "Кажется, вы ошиблись.")
                self.add_to_attempts_table(self.attempts, self.scores)
                self.scores = 0
                self.attempts += 1
            self.start_new_game()
            self.user_sequence = []

        self.update_interface()

    def update_interface(self):
        self.score.setText(f"Счет: {self.scores}")
        self.attempt.setText(f"Попытка № {self.attempts}")

    def show_message(self, title, text):
        QMessageBox.information(self, title, text)

    def add_to_attempts_table(self, attempt_num, score_num):
        form_layout = self.formLayout
        if self.attempts > 13:
            form_layout.removeRow(0)
        attempt_label = QLabel(f"Попытка #{attempt_num}")
        score_label = QLabel(f"Счет: {score_num}")
        attempt_label.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        score_label.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        form_layout.addRow(attempt_label, score_label)

class EasylevelColours(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/colours_easy_win.ui', self)

        self.existing_colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'cyan', 'white', 'black']
        self.attempts = 1
        self.scores = 0
        self.correct_sequence = []
        self.user_sequence = []

        self.pushButton_2.clicked.connect(lambda: self.on_color_clicked(self.pushButton_2))
        self.pushButton_5.clicked.connect(lambda: self.on_color_clicked(self.pushButton_5))
        self.pushButton.clicked.connect(lambda: self.on_color_clicked(self.pushButton))

        self.start_new_game()

    def set_button_colors(self, colors):
        self.pushButton_2.setStyleSheet(f"background-color: {colors[0]};")
        self.pushButton_5.setStyleSheet(f"background-color: {colors[1]};")
        self.pushButton.setStyleSheet(f"background-color: {colors[2]};")

    def start_new_game(self):
        self.correct_sequence = self.generate_random_sequence()
        self.user_sequence = []
        self.current_index = 0
        self.show_sequence()

    def generate_random_sequence(self):
        sequence = random.sample(self.existing_colors, 3)
        return sequence

    def show_sequence(self):
        self.current_index = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.display_next_color)
        self.timer.start(700)
        self.enable_buttons(False)

    def display_next_color(self):
        if self.current_index < len(self.correct_sequence):
            self.frame.setStyleSheet(f"background-color: {self.correct_sequence[self.current_index]};")
            self.current_index += 1
        else:
            self.timer.stop()
            self.enable_buttons(True)
            shuffled_sequence = self.correct_sequence[:]
            random.shuffle(shuffled_sequence)
            self.set_button_colors(shuffled_sequence)
            self.update_interface()

    def enable_buttons(self, enable):
        self.pushButton_2.setEnabled(enable)
        self.pushButton_5.setEnabled(enable)
        self.pushButton.setEnabled(enable)

    def on_color_clicked(self, button):
        color = button.styleSheet().split(': ')[1].split(';')[0]
        self.user_sequence.append(color)
        if len(self.user_sequence) == len(self.correct_sequence):
            if self.user_sequence == self.correct_sequence:
                self.scores += 1
                self.show_message("Правильно!", "Вы выбрали правильную последовательность цветов.")
            else:
                self.show_message("Неправильно!", "Кажется, вы ошиблись.")
                self.add_to_attempts_table(self.attempts, self.scores)
                self.scores = 0
                self.attempts += 1
            self.start_new_game()
            self.user_sequence = []

        self.update_interface()

    def update_interface(self):
        self.score.setText(f"Счет: {self.scores}")
        self.attempt.setText(f"Попытка № {self.attempts}")

    def show_message(self, title, text):
        QMessageBox.information(self, title, text)

    def add_to_attempts_table(self, attempt_num, score_num):
        form_layout = self.formLayout
        if self.attempts > 13:
            form_layout.removeRow(0)
        attempt_label = QLabel(f"Попытка #{attempt_num}")
        score_label = QLabel(f"Счет: {score_num}")
        attempt_label.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        score_label.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        form_layout.addRow(attempt_label, score_label)

class MediumlevelColours(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/colours_medium_win.ui', self)

        self.existing_colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'cyan', 'white', 'black']
        self.attempts = 1
        self.scores = 0
        self.correct_sequence = []
        self.user_sequence = []

        self.pushButton_2.clicked.connect(lambda: self.on_color_clicked(self.pushButton_2))
        self.pushButton_5.clicked.connect(lambda: self.on_color_clicked(self.pushButton_5))
        self.pushButton_3.clicked.connect(lambda: self.on_color_clicked(self.pushButton_3))
        self.pushButton.clicked.connect(lambda: self.on_color_clicked(self.pushButton))

        self.start_new_game()

    def set_button_colors(self, colors):
        self.pushButton_2.setStyleSheet(f"background-color: {colors[0]};")
        self.pushButton_5.setStyleSheet(f"background-color: {colors[1]};")
        self.pushButton_3.setStyleSheet(f"background-color: {colors[2]};")
        self.pushButton.setStyleSheet(f"background-color: {colors[3]};")

    def start_new_game(self):
        self.correct_sequence = self.generate_random_sequence()
        self.user_sequence = []
        self.current_index = 0
        self.show_sequence()

    def generate_random_sequence(self):
        sequence = random.sample(self.existing_colors, 4)
        return sequence

    def show_sequence(self):
        self.current_index = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.display_next_color)
        self.timer.start(700)
        self.enable_buttons(False)

    def display_next_color(self):
        if self.current_index < len(self.correct_sequence):
            self.frame.setStyleSheet(f"background-color: {self.correct_sequence[self.current_index]};")
            self.current_index += 1
        else:
            self.timer.stop()
            self.enable_buttons(True)
            shuffled_sequence = self.correct_sequence[:]
            random.shuffle(shuffled_sequence)
            self.set_button_colors(shuffled_sequence)
            self.update_interface()

    def enable_buttons(self, enable):
        self.pushButton_2.setEnabled(enable)
        self.pushButton_5.setEnabled(enable)
        self.pushButton_3.setEnabled(enable)
        self.pushButton.setEnabled(enable)

    def on_color_clicked(self, button):
        color = button.styleSheet().split(': ')[1].split(';')[0]
        self.user_sequence.append(color)
        if len(self.user_sequence) == len(self.correct_sequence):
            if self.user_sequence == self.correct_sequence:
                self.scores += 1
                self.show_message("Правильно!", "Вы выбрали правильную последовательность цветов.")
            else:
                self.show_message("Неправильно!", "Кажется, вы ошиблись.")
                self.add_to_attempts_table(self.attempts, self.scores)
                self.scores = 0
                self.attempts += 1
            self.start_new_game()
            self.user_sequence = []

        self.update_interface()

    def update_interface(self):
        self.score.setText(f"Счет: {self.scores}")
        self.attempt.setText(f"Попытка № {self.attempts}")

    def show_message(self, title, text):
        QMessageBox.information(self, title, text)

    def add_to_attempts_table(self, attempt_num, score_num):
        form_layout = self.formLayout
        if self.attempts > 13:
            form_layout.removeRow(0)
        attempt_label = QLabel(f"Попытка #{attempt_num}")
        score_label = QLabel(f"Счет: {score_num}")
        attempt_label.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        score_label.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        form_layout.addRow(attempt_label, score_label)

class DifficultlevelColours(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/colours_difficult_win.ui', self)

        self.existing_colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'cyan', 'white', 'black']
        self.attempts = 1
        self.scores = 0
        self.correct_sequence = []
        self.user_sequence = []

        self.pushButton_2.clicked.connect(lambda: self.on_color_clicked(self.pushButton_2))
        self.pushButton_5.clicked.connect(lambda: self.on_color_clicked(self.pushButton_5))
        self.pushButton_3.clicked.connect(lambda: self.on_color_clicked(self.pushButton_3))
        self.pushButton_6.clicked.connect(lambda: self.on_color_clicked(self.pushButton_6))
        self.pushButton.clicked.connect(lambda: self.on_color_clicked(self.pushButton))

        self.start_new_game()

    def set_button_colors(self, colors):
        self.pushButton_2.setStyleSheet(f"background-color: {colors[0]};")
        self.pushButton_5.setStyleSheet(f"background-color: {colors[1]};")
        self.pushButton_3.setStyleSheet(f"background-color: {colors[2]};")
        self.pushButton_6.setStyleSheet(f"background-color: {colors[3]};")
        self.pushButton.setStyleSheet(f"background-color: {colors[4]};")

    def start_new_game(self):
        self.correct_sequence = self.generate_random_sequence()
        self.user_sequence = []
        self.current_index = 0
        self.show_sequence()

    def generate_random_sequence(self):
        sequence = random.sample(self.existing_colors, 5)
        return sequence

    def show_sequence(self):
        self.current_index = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.display_next_color)
        self.timer.start(700)
        self.enable_buttons(False)

    def display_next_color(self):
        if self.current_index < len(self.correct_sequence):
            self.frame.setStyleSheet(f"background-color: {self.correct_sequence[self.current_index]};")
            self.current_index += 1
        else:
            self.timer.stop()
            self.enable_buttons(True)
            shuffled_sequence = self.correct_sequence[:]
            random.shuffle(shuffled_sequence)
            self.set_button_colors(shuffled_sequence)
            self.update_interface()

    def enable_buttons(self, enable):
        self.pushButton_2.setEnabled(enable)
        self.pushButton_5.setEnabled(enable)
        self.pushButton_3.setEnabled(enable)
        self.pushButton_6.setEnabled(enable)
        self.pushButton.setEnabled(enable)

    def on_color_clicked(self, button):
        color = button.styleSheet().split(': ')[1].split(';')[0]
        self.user_sequence.append(color)
        if len(self.user_sequence) == len(self.correct_sequence):
            if self.user_sequence == self.correct_sequence:
                self.scores += 1
                self.show_message("Правильно!", "Вы выбрали правильную последовательность цветов.")
            else:
                self.show_message("Неправильно!", "Кажется, вы ошиблись.")
                self.add_to_attempts_table(self.attempts, self.scores)
                self.scores = 0
                self.attempts += 1
            self.start_new_game()
            self.user_sequence = []

        self.update_interface()

    def update_interface(self):
        self.score.setText(f"Счет: {self.scores}")
        self.attempt.setText(f"Попытка № {self.attempts}")

    def show_message(self, title, text):
        QMessageBox.information(self, title, text)

    def add_to_attempts_table(self, attempt_num, score_num):
        form_layout = self.formLayout
        if self.attempts > 13:
            form_layout.removeRow(0)
        attempt_label = QLabel(f"Попытка #{attempt_num}")
        score_label = QLabel(f"Счет: {score_num}")
        attempt_label.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        score_label.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        form_layout.addRow(attempt_label, score_label)

class EasylevelColoursWords(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/colours&words_easy_win.ui', self)

        self.existing_words = ['кот', 'лист', 'дом', 'снег', 'век', 'шар', 'долг', 'друг', 'ток']
        self.colors = [QColor("red"), QColor("blue"), QColor("green"), QColor("yellow"), QColor("purple"),
                       QColor("orange"), QColor("cyan"), QColor("pink"), QColor("brown")]
        self.attempts = 1
        self.scores = 0
        self.correct_sequence = []
        self.user_sequence = []

        self.pushButton_4.clicked.connect(lambda: self.on_word_clicked(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.on_word_clicked(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.on_word_clicked(self.pushButton_6))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14.setStyleSheet('font: 12pt "MS Shell Dlg 2";')

        self.start_new_game()

    def set_button_words(self, words_and_colors):
        self.pushButton_4.setText(words_and_colors[0][0])
        self.pushButton_5.setText(words_and_colors[1][0])
        self.pushButton_6.setText(words_and_colors[2][0])
        self.pushButton_4.setStyleSheet(
            f"background-color: {words_and_colors[0][1].name()}; font: 12pt 'MS Shell Dlg 2';")
        self.pushButton_5.setStyleSheet(
            f"background-color: {words_and_colors[1][1].name()}; font: 12pt 'MS Shell Dlg 2';")
        self.pushButton_6.setStyleSheet(
            f"background-color: {words_and_colors[2][1].name()}; font: 12pt 'MS Shell Dlg 2';")

    def start_new_game(self):
        self.correct_sequence = self.generate_random_sequence()
        self.user_sequence = []
        self.current_index = 0
        self.show_sequence()

    def generate_random_sequence(self):
        sequence = []
        selected_words = random.choices(self.existing_words, k=3)
        for word in selected_words:
            background_color = random.choice(self.colors)
            sequence.append((word, background_color))
        return sequence

    def show_sequence(self):
        self.current_index = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.display_next_word)
        self.timer.start(700)
        self.enable_buttons(False)

    def display_next_word(self):
        if self.current_index < len(self.correct_sequence):
            word, background_color = self.correct_sequence[self.current_index]
            self.label_14.setStyleSheet(f"background-color: {background_color.name()}; font: 12pt 'MS Shell Dlg 2';")
            self.label_14.setText(word)
            self.current_index += 1
        else:
            self.timer.stop()
            self.enable_buttons(True)
            shuffled_sequence = self.correct_sequence[:]
            random.shuffle(shuffled_sequence)
            self.set_button_words(shuffled_sequence)
            self.update_interface()

    def enable_buttons(self, enable):
        self.pushButton_4.setEnabled(enable)
        self.pushButton_5.setEnabled(enable)
        self.pushButton_6.setEnabled(enable)

    def on_word_clicked(self, button):
        word = button.text().lower()
        self.user_sequence.append(word)
        if len(self.user_sequence) == len(self.correct_sequence):
            if self.user_sequence == [x[0] for x in self.correct_sequence]:
                self.scores += 1
                self.show_message("Правильно!", "Вы выбрали правильную последовательность слов.")
            else:
                self.show_message("Неправильно!", "Кажется, вы ошиблись.")
                self.add_to_attempts_table(self.attempts, self.scores)
                self.scores = 0
                self.attempts += 1
            self.start_new_game()
            self.user_sequence = []

        self.update_interface()

    def update_interface(self):
        self.score.setText(f"Счет: {self.scores}")
        self.attempt.setText(f"Попытка № {self.attempts}")

    def show_message(self, title, text):
        QMessageBox.information(self, title, text)

    def add_to_attempts_table(self, attempt_num, score_num):
        form_layout = self.formLayout
        if self.attempts > 13:
            form_layout.removeRow(0)
        attempt_label = QLabel(f"Попытка #{attempt_num}")
        score_label = QLabel(f"Счет: {score_num}")
        attempt_label.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        score_label.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        form_layout.addRow(attempt_label, score_label)

class MediumlevelColoursWords(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/colours&words_medium_win.ui', self)

        self.existing_words = ['город', 'песок', 'солнце', 'вода', 'книга', 'пламя', 'лампа', 'птица', 'туча']
        self.colors = [QColor("red"), QColor("blue"), QColor("green"), QColor("yellow"), QColor("purple"),
                       QColor("orange"), QColor("cyan"), QColor("pink"), QColor("brown")]
        self.attempts = 1
        self.scores = 0
        self.correct_sequence = []
        self.user_sequence = []

        self.pushButton_4.clicked.connect(lambda: self.on_word_clicked(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.on_word_clicked(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.on_word_clicked(self.pushButton_6))
        self.pushButton_2.clicked.connect(lambda: self.on_word_clicked(self.pushButton_2))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14.setStyleSheet('font: 12pt "MS Shell Dlg 2";')

        self.start_new_game()

    def set_button_words(self, words_and_colors):
        self.pushButton_4.setText(words_and_colors[0][0])
        self.pushButton_5.setText(words_and_colors[1][0])
        self.pushButton_6.setText(words_and_colors[2][0])
        self.pushButton_2.setText(words_and_colors[3][0])
        self.pushButton_4.setStyleSheet(
            f"background-color: {words_and_colors[0][1].name()}; font: 12pt 'MS Shell Dlg 2';")
        self.pushButton_5.setStyleSheet(
            f"background-color: {words_and_colors[1][1].name()}; font: 12pt 'MS Shell Dlg 2';")
        self.pushButton_6.setStyleSheet(
            f"background-color: {words_and_colors[2][1].name()}; font: 12pt 'MS Shell Dlg 2';")
        self.pushButton_2.setStyleSheet(
            f"background-color: {words_and_colors[3][1].name()}; font: 12pt 'MS Shell Dlg 2';")

    def start_new_game(self):
        self.correct_sequence = self.generate_random_sequence()
        self.user_sequence = []
        self.current_index = 0
        self.show_sequence()

    def generate_random_sequence(self):
        sequence = []
        selected_words = random.choices(self.existing_words, k=4)
        for word in selected_words:
            background_color = random.choice(self.colors)
            sequence.append((word, background_color))
        return sequence

    def show_sequence(self):
        self.current_index = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.display_next_word)
        self.timer.start(700)
        self.enable_buttons(False)

    def display_next_word(self):
        if self.current_index < len(self.correct_sequence):
            word, background_color = self.correct_sequence[self.current_index]
            self.label_14.setStyleSheet(f"background-color: {background_color.name()}; font: 12pt 'MS Shell Dlg 2';")
            self.label_14.setText(word)
            self.current_index += 1
        else:
            self.timer.stop()
            self.enable_buttons(True)
            shuffled_sequence = self.correct_sequence[:]
            random.shuffle(shuffled_sequence)
            self.set_button_words(shuffled_sequence)
            self.update_interface()

    def enable_buttons(self, enable):
        self.pushButton_4.setEnabled(enable)
        self.pushButton_5.setEnabled(enable)
        self.pushButton_6.setEnabled(enable)
        self.pushButton_2.setEnabled(enable)

    def on_word_clicked(self, button):
        word = button.text().lower()
        self.user_sequence.append(word)
        if len(self.user_sequence) == len(self.correct_sequence):
            if self.user_sequence == [x[0] for x in self.correct_sequence]:
                self.scores += 1
                self.show_message("Правильно!", "Вы выбрали правильную последовательность слов.")
            else:
                self.show_message("Неправильно!", "Кажется, вы ошиблись.")
                self.add_to_attempts_table(self.attempts, self.scores)
                self.scores = 0
                self.attempts += 1
            self.start_new_game()
            self.user_sequence = []

        self.update_interface()

    def update_interface(self):
        self.score.setText(f"Счет: {self.scores}")
        self.attempt.setText(f"Попытка № {self.attempts}")

    def show_message(self, title, text):
        QMessageBox.information(self, title, text)

    def add_to_attempts_table(self, attempt_num, score_num):
        form_layout = self.formLayout
        if self.attempts > 13:
            form_layout.removeRow(0)
        attempt_label = QLabel(f"Попытка #{attempt_num}")
        score_label = QLabel(f"Счет: {score_num}")
        attempt_label.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        score_label.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        form_layout.addRow(attempt_label, score_label)

class DifficultlevelColoursWords(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/colours&words_difficult_win.ui', self)

        self.existing_words = ['коробка', 'известие', 'платформа', 'компьютер', 'картинка', 'площадка',
                               'партизан', 'господин', 'календарь']
        self.colors = [QColor("red"), QColor("blue"), QColor("green"), QColor("yellow"), QColor("purple"),
                       QColor("orange"), QColor("cyan"), QColor("pink"), QColor("brown")]
        self.attempts = 1
        self.scores = 0
        self.correct_sequence = []
        self.user_sequence = []

        self.pushButton_8.clicked.connect(lambda: self.on_word_clicked(self.pushButton_8))
        self.pushButton_4.clicked.connect(lambda: self.on_word_clicked(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.on_word_clicked(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.on_word_clicked(self.pushButton_6))
        self.pushButton_2.clicked.connect(lambda: self.on_word_clicked(self.pushButton_2))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14.setStyleSheet('font: 12pt "MS Shell Dlg 2";')

        self.start_new_game()

    def set_button_words(self, words_and_colors):
        self.pushButton_8.setText(words_and_colors[0][0])
        self.pushButton_4.setText(words_and_colors[1][0])
        self.pushButton_5.setText(words_and_colors[2][0])
        self.pushButton_6.setText(words_and_colors[3][0])
        self.pushButton_2.setText(words_and_colors[4][0])
        self.pushButton_8.setStyleSheet(
            f"background-color: {words_and_colors[0][1].name()}; font: 12pt 'MS Shell Dlg 2';")
        self.pushButton_4.setStyleSheet(
            f"background-color: {words_and_colors[1][1].name()}; font: 12pt 'MS Shell Dlg 2';")
        self.pushButton_5.setStyleSheet(
            f"background-color: {words_and_colors[2][1].name()}; font: 12pt 'MS Shell Dlg 2';")
        self.pushButton_6.setStyleSheet(
            f"background-color: {words_and_colors[3][1].name()}; font: 12pt 'MS Shell Dlg 2';")
        self.pushButton_2.setStyleSheet(
            f"background-color: {words_and_colors[4][1].name()}; font: 12pt 'MS Shell Dlg 2';")

    def start_new_game(self):
        self.correct_sequence = self.generate_random_sequence()
        self.user_sequence = []
        self.current_index = 0
        self.show_sequence()

    def generate_random_sequence(self):
        sequence = []
        selected_words = random.choices(self.existing_words, k = 5)
        for word in selected_words:
            background_color = random.choice(self.colors)
            sequence.append((word, background_color))
        return sequence

    def show_sequence(self):
        self.current_index = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.display_next_word)
        self.timer.start(700)
        self.enable_buttons(False)

    def display_next_word(self):
        if self.current_index < len(self.correct_sequence):
            word, background_color = self.correct_sequence[self.current_index]
            self.label_14.setStyleSheet(f"background-color: {background_color.name()}; font: 12pt 'MS Shell Dlg 2';")
            self.label_14.setText(word)
            self.current_index += 1
        else:
            self.timer.stop()
            self.enable_buttons(True)
            shuffled_sequence = self.correct_sequence[:]
            random.shuffle(shuffled_sequence)
            self.set_button_words(shuffled_sequence)
            self.update_interface()

    def enable_buttons(self, enable):
        self.pushButton_8.setEnabled(enable)
        self.pushButton_4.setEnabled(enable)
        self.pushButton_5.setEnabled(enable)
        self.pushButton_6.setEnabled(enable)
        self.pushButton_2.setEnabled(enable)

    def on_word_clicked(self, button):
        word = button.text().lower()
        self.user_sequence.append(word)
        if len(self.user_sequence) == len(self.correct_sequence):
            if self.user_sequence == [x[0] for x in self.correct_sequence]:
                self.scores += 1
                self.show_message("Правильно!", "Вы выбрали правильную последовательность слов.")
            else:
                self.show_message("Неправильно!", "Кажется, вы ошиблись.")
                self.add_to_attempts_table(self.attempts, self.scores)
                self.scores = 0
                self.attempts += 1
            self.start_new_game()
            self.user_sequence = []

        self.update_interface()

    def update_interface(self):
        self.score.setText(f"Счет: {self.scores}")
        self.attempt.setText(f"Попытка № {self.attempts}")

    def show_message(self, title, text):
        QMessageBox.information(self, title, text)

    def add_to_attempts_table(self, attempt_num, score_num):
        form_layout = self.formLayout
        if self.attempts > 13:
            form_layout.removeRow(0)
        attempt_label = QLabel(f"Попытка #{attempt_num}")
        score_label = QLabel(f"Счет: {score_num}")
        attempt_label.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        score_label.setStyleSheet("font: 10pt 'MS Shell Dlg 2';")
        form_layout.addRow(attempt_label, score_label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartGame()
    ex.show()
    sys.exit(app.exec())
