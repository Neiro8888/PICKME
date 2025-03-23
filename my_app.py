from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel, QHBoxLayout, QVBoxLayout
import random
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Бабка овера')
main_win.resize(400,200)

linev =  QVBoxLayout()
line1 =  QHBoxLayout()
line2 =  QHBoxLayout()
line3 =  QHBoxLayout()

text = QLabel("Добро пожаловать в программу по определению состояния здоровья")



text2 = QLabel("Данное приложение позвалит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.")



text4 = QLabel("Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособости средца при физический нагрузке. \n У испытуе")

text5 = QLabel("C++")
line1.addWidget(text, alignment=Qt.AlignCenter)

line2.addWidget(text2, alignment=Qt.AlignCenter)

line3.addWidget(text4, alignment=Qt.AlignCenter)
line3.addWidget(text5, alignment=Qt.AlignCenter)
linev.addLayout(line1)
linev.addLayout(line2)
linev.addLayout(line3)

main_win.setLayout(linev)
main_win.show()
app.exec_()