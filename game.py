from gg import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.acceptBut.clicked.connect(self.start_game)
        self.ui.back2menu.clicked.connect(self.back_menu)
        self.ui.pushButton.clicked.connect(self.next_pic)
        self.diff_list = ['Легко', 'Обычно', 'Трудно']
        self.list = []
        self.ez_ans = [2, 8]
        self.norm_ans = []
        self.hard_ans = [32, 66]
        self.id_list = 0
        self.diff = 1
        self.i = 1
        self.step = 1
        self.end_score = 0
        self.cb = QtWidgets.QComboBox(self)
        self.cb.setFixedSize(150, 30)
        self.cb.move(360, 25)
        self.cb.setFont(QtGui.QFont("Times", 12))
        self.cb.addItems(self.diff_list)
        self.pixmap = None
        self.ui.LabelImage.setText('')
        self.resize(800, 90)


    def start_game(self):
        self.resize(800, 580)
        self.ui.acceptBut.setVisible(False)
        self.cb.setVisible(False)
        self.check_diff()

    def next_pic(self):
        self.check_ans()
        self.i += 1
        self.step += 1
        if self.i <= 2:
            if self.diff == 1:
                self.pixmap = QPixmap('ez{0}.jpg'.format(self.i))
                self.ui.LabelImage.setPixmap(self.pixmap)
            if self.diff == 2:
                self.pixmap = QPixmap('norm{0}.jpg'.format(self.i))
                self.ui.LabelImage.setPixmap(self.pixmap)
            if self.diff == 3:
                self.pixmap = QPixmap('hard{0}.jpg'.format(self.i))
                self.ui.LabelImage.setPixmap(self.pixmap)

        else:
            if self.end_score == 0:
                self.end0()
            if self.end_score == 1:
                self.end1()
            if self.end_score == 2:
                self.end2()

    def check_ans(self):
        ans = self.ui.ans.value()
        if self.diff == 1:
            if self.step == 1:
                if ans == 2:
                    self.end_score += 1
            if self.step == 2:
                if ans == 8:
                    self.end_score += 1

        if self.diff == 2:
            if self.step == 1:
                if ans == 13:
                    self.end_score += 1
            if self.step == 2:
                if ans == 18:
                    self.end_score += 1

        if self.diff == 3:
            if self.step == 1:
                if self.ui.ans.value == 32:
                    self.end_score += 1
            if self.step == 2:
                if self.ui.ans.value == 66:
                    self.end_score += 1

    def check_diff(self):
        self.id_list = self.cb.currentIndex()
        if self.id_list == 0:
            self.ui.label.setText('Сложность: легко')
            self.diff = 1
            self.pixmap = QPixmap('ez{0}.jpg'.format(self.i))
            self.ui.LabelImage.setPixmap(self.pixmap)

        if self.id_list == 1:
            self.ui.label.setText('Сложность: нормально')
            self.diff = 2
            self.pixmap = QPixmap('norm{0}.jpg'.format(self.i))
            self.ui.LabelImage.setPixmap(self.pixmap)

        if self.id_list == 2:
            self.ui.label.setText('Сложность: трудно')
            self.diff = 3
            self.pixmap = QPixmap('hard{0}.jpg'.format(self.i))
            self.ui.LabelImage.setPixmap(self.pixmap)

    def end0(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText("Игра закончена. Верно 0 из 2. Попробовать снова?")
        msgBox.setWindowTitle("Конец игры.")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Yes:
            self.reset()
        else:
            self.parent.show()
            self.close()

    def end1(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText("Игра закончена. Верно 1 из 2. Попробовать снова?")
        msgBox.setWindowTitle("Конец игры.")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Yes:
            self.reset()
        else:
            self.parent.show()
            self.close()

    def end2(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText("Игра закончена. Верно 2 из 2! Попробовать снова?")
        msgBox.setWindowTitle("Конец игры.")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Yes:
            self.reset()
        else:
            self.parent.show()
            self.close()

    def reset(self):
        self.resize(800, 90)
        self.ui.acceptBut.setVisible(True)
        self.cb.setVisible(True)
        self.end_score = 0
        self. i = 1
        self.step = 1
        self.ui.label.setText('Выберите уровень сложности:')


    def back_menu(self):
        self.parent.show()
        self.close()
