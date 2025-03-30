from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel, QHBoxLayout, QVBoxLayout
import sys
import os
import random
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('132')
main_win.resize(600,300)
cmd = 'python second_win.py'
def start2():
    main_win.hide()
    os.system(cmd)
    
    
linev =  QVBoxLayout()
line1 =  QHBoxLayout()
line2 =  QHBoxLayout()
line3 =  QHBoxLayout()
line4 =  QHBoxLayout()

text = QLabel("Добро пожаловать в программу по определению состояния здоровья")



text2 = QLabel("Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.")



text4 = QLabel("Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособости средца при физический нагрузке. \nУ испытуемого, находящегося в положениилежа на спине в течении 5 мин, определяют частоту пульса за 15 секунд; \nзатем в течении 45 секунд испытуемый выполняет 30 приседаний.\nПосле окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсация за первые 15 секунд, \n а потом - за последние 15 секунд первой минуты периода восстановления. \nВажно! Если в процессе проведения испытания вы почувствуете себя плохо ( появится головокружение, шум в\nушах, сильная отдышка и др.) то тест необходимо прервать и обратиться к врачу.")


line1.addWidget(text, alignment=Qt.AlignCenter)

line2.addWidget(text2, alignment=Qt.AlignCenter)

line3.addWidget(text4, alignment=Qt.AlignCenter)
button = QPushButton("Начать")
button.clicked.connect(start2)
button.text()
line4.addWidget(button, alignment=Qt.AlignCenter)

linev.addLayout(line1)
linev.addLayout(line2)
linev.addLayout(line3)
linev.addLayout(line4)

main_win.setLayout(linev)
main_win.show()
app.exec_()