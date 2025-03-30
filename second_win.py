from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel, QHBoxLayout, QVBoxLayout, QLineEdit
import sys
import os
import random
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Здоровье')
main_win.resize(600,300)    
linev =  QVBoxLayout()
line1 =  QVBoxLayout()
line2 =  QVBoxLayout()
line3 =  QVBoxLayout()
line4 =  QVBoxLayout()

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
t = QLabel('00:00:15')
line1.addWidget(text, alignment=Qt.AlignLeft)
line1.addWidget(pole1, alignment=Qt.AlignLeft)
line1.addWidget(text1, alignment=Qt.AlignLeft)
line1.addWidget(pole2, alignment=Qt.AlignLeft)
line1.addWidget(text2, alignment=Qt.AlignLeft)
line1.addWidget(button, alignment=Qt.AlignLeft)
line2.addWidget(t,alignment=Qt.AlignCenter)
line1.addWidget(pole3, alignment=Qt.AlignLeft)
line1.addWidget(text3, alignment=Qt.AlignLeft)
line1.addWidget(button2, alignment=Qt.AlignLeft)
line1.addWidget(text4, alignment=Qt.AlignLeft)
line1.addWidget(button3, alignment=Qt.AlignLeft)
line1.addWidget(pole4, alignment=Qt.AlignLeft)
line1.addWidget(pole5, alignment=Qt.AlignLeft)

button = QPushButton("Отправить результаты")

button.text()
line4.addWidget(button, alignment=Qt.AlignCenter)

linev.addLayout(line1)
linev.addLayout(line2)
linev.addLayout(line3)
linev.addLayout(line4)

main_win.setLayout(linev)
main_win.show()
app.exec_()