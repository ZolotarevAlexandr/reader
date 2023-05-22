import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtCore import QTimer, QEventLoop
from PyQt5.Qt import QTextCursor

import cgitb
cgitb.enable(format='text')


def get_text_line():
    with open('data/test.txt') as file:
        data = file.read()
    return data


def qt_sleep(time):
    loop = QEventLoop()
    QTimer.singleShot(time, loop.quit)
    loop.exec_()


def create_progress_file():
    if not os.path.exists('progress.txt'):
        with open('progress.txt', 'w'):
            pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data/running_line_ui.ui', self)
        self.setWindowTitle('Running line')

        with open('progress.txt') as file:
            self.running_line.setText(file.read())

        self.start_btn.clicked.connect(self.run_line)
        self.plus_btn.clicked.connect(self.change_speed)
        self.minus_btn.clicked.connect(self.change_speed)
        self.pause_btn.clicked.connect(self.change_pause_state)
        self.cont_btn.clicked.connect(self.change_pause_state)

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
        text = get_text_line()
        displayed = ''
        cursor = self.running_line.textCursor()

        for letter in text:
            displayed += letter

            if displayed in self.running_line.toPlainText():
                continue

            self.running_line.setText(displayed)
            cursor.movePosition(QTextCursor.End)
            self.running_line.setTextCursor(cursor)
            qt_sleep(self.speed)

            while self.paused:
                qt_sleep(10)

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
