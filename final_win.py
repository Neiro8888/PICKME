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

text = QLabel("Индекс Руфье:")
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