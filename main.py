import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from game import MainWindow


class Window(QMainWindow):
    def __init__(self):
        self.x_main = 640
        self.y_main = 360

        super(Window, self).__init__()
        self.setWindowTitle("Подсчёт числа треугольников")
        self.setFixedSize(self.x_main, self.y_main)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Подсчёт числа треугольников")
        self.main_text.setFont(QtGui.QFont("Times", 24, QtGui.QFont.Bold))
        self.main_text.move(self.x_main // 10, self.y_main // 10)
        self.main_text.adjustSize()

        self.btn_startplay = QtWidgets.QPushButton(self)
        self.btn_startplay.move(self.x_main // 2 - 100, self.y_main // 10 + 100)
        self.btn_startplay.setText("Играть")
        self.btn_startplay.setFixedWidth(200)
        self.btn_startplay.setFixedHeight(50)
        self.btn_startplay.clicked.connect(self.play_main)

        self.btn_exit = QtWidgets.QPushButton(self)
        self.btn_exit.move(self.x_main // 2 - 100, self.y_main // 2 + 75)
        self.btn_exit.setText("Выход")
        self.btn_exit.clicked.connect(self.exit_main)
        self.btn_exit.setFixedWidth(200)

    def play_main(self):
        self.setVisible(False)
        self.mainWindow = MainWindow(self)
        self.mainWindow.show()

    def back_menu(self):
        self.setVisible(True)

    def exit_main(self):
        sys.exit()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()

