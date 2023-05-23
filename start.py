import os
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

import main
from data.start_ui import Ui_MainWindow


def create_files():
    if not os.path.exists('progress.txt'):
        with open('progress.txt', 'w'):
            pass

    if not os.path.exists('last_book.txt'):
        with open('last_book.txt', 'w'):
            pass


class StartWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Choose a book')

        self.conf_btn.clicked.connect(self.choose)
        self.browse_btn.clicked.connect(self.browse)

        with open('last_book.txt') as file:
            self.last_book_path = file.read()

        self.path_inp.setText(self.last_book_path)

    def browse(self):
        filepath, ok = QFileDialog.getOpenFileName(self, 'Выберите книгу', '',
                                                   'Текстовый файл (*.txt)')
        if ok:
            self.path_inp.setText(filepath)

    def choose(self):
        new_path = self.path_inp.text()

        if not new_path:
            self.error_label.setText('Error: empty path')
            return

        if not new_path == self.last_book_path:
            with open('last_book.txt', 'w') as book_file:
                book_file.write(new_path)
            with open('progress.txt', 'w') as progress_file:
                progress_file.write('')

        self.close()
        self.main_window = main.MainWindow()
        self.main_window.show()


def run():
    create_files()

    app = QApplication(sys.argv)
    ex = StartWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
