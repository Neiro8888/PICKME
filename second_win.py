from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel, QHBoxLayout, QVBoxLayout, QLineEdit
import sys
import os
import random

from datetime import datetime, timedelta
import threading
import time



app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Здоровье')
main_win.resize(700,300)    
linev =  QVBoxLayout()
line1 =  QVBoxLayout()
line2 =  QHBoxLayout()
line3 =  QVBoxLayout()
line4 =  QVBoxLayout()
cmd = 'python final_win.py'
def start2():
    p1 = int(pole3.text())
    p2 = int(pole4.text())
    p3 = int(pole5.text())
    rr = str((4*(p1+p2+p3)-200)/10)
    p4 = pole2.text()
    file4321 = open('file.txt','w')
    file4321.write(rr)
    file4321.close()
    file432 = open('age.txt','w')
    file432.write(p4)
    file432.close()
    main_win.hide()
    os.system(cmd)
def my_timer(print_interval):
    data = threading.local()
    data.counter = 14
    while data.counter >= 0:
        time.sleep(print_interval)
        if data.counter >= 10:
            tex.setText('00:00:'+str(data.counter))
        if data.counter < 10:
            tex.setText('00:00:0'+str(data.counter))
        data.counter -= 1
    tex.setText('00:00:00')
def you():
    t = threading.Thread(target=my_timer, name="My time thread", args=(1, ), daemon=True)
    t.start()
text = QLabel("Введите Ф.И.О")
pole1 = QLineEdit()
text1 = QLabel('Кол-во полных лет')
pole2 = QLineEdit()
text2 = QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\nРезультат запишите в соответствующее поле.')
button = QPushButton('Начать первый тест')

pole3 = QLineEdit()
text3 = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\nчтобы запустить счетчик приседаний.')
button2 = QPushButton('Начать делать приседания')
text4 = QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗелёным обозначены секунды, в течение которых необходимо \nпроводить измерения, черным - секунды без замера пульсаций. Результаты запишите в соответствующие поля.'
)
button3 = QPushButton('Начать финальный тест')
pole4 = QLineEdit()
pole5 = QLineEdit()
tex = QLabel('00:00:15')
button.clicked.connect(you)
line1.addWidget(text, alignment=Qt.AlignLeft)
line2.addWidget(tex,alignment=Qt.AlignRight)
line1.addWidget(pole1, alignment=Qt.AlignLeft)
line1.addWidget(text1, alignment=Qt.AlignLeft)
line1.addWidget(pole2, alignment=Qt.AlignLeft)
line1.addWidget(text2, alignment=Qt.AlignLeft)
line1.addWidget(button, alignment=Qt.AlignLeft)

line1.addWidget(pole3, alignment=Qt.AlignLeft)
line1.addWidget(text3, alignment=Qt.AlignLeft)
line1.addWidget(button2, alignment=Qt.AlignLeft)
line1.addWidget(text4, alignment=Qt.AlignLeft)
line1.addWidget(button3, alignment=Qt.AlignLeft)
line1.addWidget(pole4, alignment=Qt.AlignLeft)
line1.addWidget(pole5, alignment=Qt.AlignLeft)

button = QPushButton("Отправить результаты")
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