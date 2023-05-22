import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtCore import QTimer, QEventLoop
from PyQt5.Qt import QTextCursor


def get_text_line():
    with open('data/test.txt') as file:
        data = file.read()
    return data


def qt_sleep(time):
    loop = QEventLoop()
    QTimer.singleShot(time, loop.quit)
    loop.exec_()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data/running_line_ui.ui', self)
        self.setWindowTitle('Running line')

        self.read_btn.clicked.connect(self.run_line)

        self.speed = 100

    def run_line(self):
        text = get_text_line()
        displayed = ''
        cursor = self.running_line.textCursor()

        for letter in text:
            displayed += letter
            self.running_line.setText(displayed)
            cursor.movePosition(QTextCursor.End)
            self.running_line.setTextCursor(cursor)
            qt_sleep(self.speed)


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
