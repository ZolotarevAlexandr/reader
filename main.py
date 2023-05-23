import sys
import os

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QTimer, QEventLoop
from PyQt5.Qt import QTextCursor

from data.ui_file import Ui_MainWindow

import cgitb
cgitb.enable(format='text')


def qt_sleep(time):
    loop = QEventLoop()
    QTimer.singleShot(time, loop.quit)
    loop.exec_()


def create_progress_file(forced=False):
    if not os.path.exists('progress.txt') or forced:
        with open('progress.txt', 'w'):
            pass


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Running line')

        if os.path.exists('progress.txt') and os.path.exists('last_book.txt'):
            with open('progress.txt') as file:
                content = file.read()
                self.running_line.setText(content)

            with open('last_book.txt') as file:
                path = file.read()
            with open(path) as book_file:
                self.book_text = book_file.read()
        else:
            self.change_book()

        self.start_btn.clicked.connect(self.run_line)
        self.plus_btn.clicked.connect(self.change_speed)
        self.minus_btn.clicked.connect(self.change_speed)
        self.pause_btn.clicked.connect(self.change_pause_state)
        self.cont_btn.clicked.connect(self.change_pause_state)
        self.change_btn.clicked.connect(self.change_book)

        self.speed = 100
        self.paused = False

    def change_speed(self):
        sender = self.sender()
        if sender == self.plus_btn and not self.paused:
            self.speed += 10
        elif sender == self.minus_btn and self.speed != 10 and not self.paused:
            self.speed -= 10
        if not self.paused:
            self.current_speed.setText(str(self.speed))

    def change_pause_state(self):
        sender = self.sender()
        if self.paused is False and sender == self.pause_btn:
            self.paused = True
            self.current_speed.setText('Paused')
        elif self.paused is True and sender == self.cont_btn:
            self.paused = False
            self.current_speed.setText(str(self.speed))

    def run_line(self):
        displayed = ''
        cursor = self.running_line.textCursor()

        for letter in self.book_text:
            displayed += letter
            if displayed in self.running_line.toPlainText():
                continue

            self.running_line.setText(displayed)
            cursor.movePosition(QTextCursor.End)
            self.running_line.setTextCursor(cursor)
            qt_sleep(self.speed)

            while self.paused:
                qt_sleep(10)

    def change_book(self):
        filepath, ok = QFileDialog.getOpenFileName(self, 'Выберите книгу', '',
                                                   'Текстовый файл (*.txt)')
        if ok:
            with open(filepath) as file:
                self.book_text = file.read()

            with open('last_book.txt', 'w') as file:
                file.write(filepath)

            create_progress_file(forced=True)
            self.running_line.clear()

    def closeEvent(self, event):
        with open('progress.txt', 'w') as file:
            file.write(self.running_line.toPlainText())
        event.accept()
        exit(0)


def main():
    create_progress_file()
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
