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
b = ''
with open('file.txt', 'r') as r:
    a = int(r.read())
    r.close()
with open('age.txt', 'r') as r:
    age = int(r.read())
    r.close()
b = ''
def workers(age,a):
    
    low = 21
    nice = 17
    nice1 = 20.9
    middle = 12
    middle1 = 16.9
    hight_middle = 6.5
    hight_middle1 = 11.9
    hight = 6.4
    
    if int(age) == 7 or int(age) == 8:
        
        if a >= low:
            b = ' Низкая '
        elif a >= nice and a <= nice1:
            b = ' Удовлетворительная'
        elif a >= middle and a <= middle1:
            b = ' Средняя'
        elif a >= hight_middle and a <= hight_middle1:
            b = ' Выше среднего'
        elif a <= hight :
            b = ' Высокая'
    if int(age) == 9 or int(age) == 10:
        
        low = 19.5
        nice = 15.5
        nice1 = 19.4
        middle = 10.5
        middle1 = 15.4
        hight_middle = 5
        hight_middle1 = 10.4
        hight = 4.9
        if a >= low:
            b = ' Низкая '
        elif a >= nice and a <= nice1:
            b = ' Удовлетворительная'
        elif a >= middle and a <= middle1:
            b = ' Средняя'
        elif a >= hight_middle and a <= hight_middle1:
            b = ' Выше среднего'
        elif a <= hight :
            b = ' Высокая'
    if int(age) == 11 or int(age) == 12:
        
        low = 19.5 - 1.5
        nice = 15.5 - 1.5
        nice1 = 19.4 - 1.5
        middle = 10.5 - 1.5
        middle1 = 15.4 - 1.5
        hight_middle = 5 - 1.5
        hight_middle1 = 10.4 - 1.5
        hight = 4.9 - 1.5
        if a >= low:
            b = ' Низкая '
        elif a >= nice and a <= nice1:
            b = ' Удовлетворительная'
        elif a >= middle and a <= middle1:
            b = ' Средняя'
        elif a >= hight_middle and a <= hight_middle1:
            b = ' Выше среднего'
        elif a <= hight :
            b = ' Высокая'
    if int(age) == 13 or int(age) == 14:
        
        low = 19.5 - 1.5 - 1.5
        nice = 15.5 - 1.5 - 1.5
        nice1 = 19.4 - 1.5 - 1.5 
        middle = 10.5 - 1.5- 1.5
        middle1 = 15.4 - 1.5- 1.5
        hight_middle = 5 - 1.5- 1.5
        hight_middle1 = 10.4 - 1.5- 1.5
        hight = 4.9 - 1.5- 1.5
        if a >= low:
            b = ' Низкая '
        elif a >= nice and a <= nice1:
            b = ' Удовлетворительная'
        elif a >= middle and a <= middle1:
            b = ' Средняя'
        elif a >= hight_middle and a <= hight_middle1:
            b = ' Выше среднего'
        elif a <= hight :
            b = ' Высокая'
    if int(age) >= 15:
        
        low = 19.5 - 1.5 - 1.5- 1.5
        nice = 15.5 - 1.5 - 1.5- 1.5
        nice1 = 19.4 - 1.5 - 1.5 - 1.5
        middle = 10.5 - 1.5- 1.5- 1.5
        middle1 = 15.4 - 1.5- 1.5- 1.5
        hight_middle = 5 - 1.5- 1.5- 1.5
        hight_middle1 = 10.4 - 1.5- 1.5- 1.5
        hight = 4.9 - 1.5- 1.5- 1.5
        if a >= low:
            b = ' Низкая '
        elif a >= nice and a <= nice1:
            b = ' Удовлетворительная'
        elif a >= middle and a <= middle1:
            b = ' Средняя'
        elif a >= hight_middle and a <= hight_middle1:
            b = ' Выше среднего'
        elif a <= hight :
            b = ' Высокая'
    
    
    t = QLabel('Работоспособность сердца:' + str(b))
    line1.addWidget(t, alignment=Qt.AlignCenter)


text = QLabel('Индекс Руфье: '+ str(a))

line1.addWidget(text, alignment=Qt.AlignCenter)
          
age1 = workers(age,a)






linev.addLayout(line1)
linev.addLayout(line2)
linev.addLayout(line3)
linev.addLayout(line4)

main_win.setLayout(linev)
main_win.show()
app.exec_()