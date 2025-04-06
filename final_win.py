from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel, QHBoxLayout, QVBoxLayout, QLineEdit
import sys
import os
import random
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Результат')
main_win.resize(600,300)    
linev =  QVBoxLayout()
line1 =  QVBoxLayout()
line2 =  QVBoxLayout()
line3 =  QVBoxLayout()
line4 =  QVBoxLayout()
with open('file.txt', 'r') as r:
    a = r.read()
    r.close()
with open('age.txt', 'r') as r:
    age = r.read()
    r.close()
def workers(age):
    low = 21
    nice = 17
    nice1 = 20.9
    middle = 12
    middle1 = 16.9
    hight_middle = 6.5
    hight_middle1 = 11.9
    hight = 6.4

    if age == 7 or age == 8:
        if a >= low:
            b = ' Низкая '
        elif a >= nice and a <= nice1:
            b = 'Удовлетворительная'
        elif a >= middle and a <= middle1:
            b = 'Средняя'
        elif a >= hight_middle and a <= hight_middle1:
            b = 'Выше среднего'
        elif a <= hight :
            b = 'Выше среднего'




    return b        

text = QLabel('Индекс Руфье:' + a)
t = QLabel('Работоспособность сердца:')
line1.addWidget(text, alignment=Qt.AlignCenter)
line1.addWidget(t, alignment=Qt.AlignCenter)




linev.addLayout(line1)
linev.addLayout(line2)
linev.addLayout(line3)
linev.addLayout(line4)

main_win.setLayout(linev)
main_win.show()
app.exec_()