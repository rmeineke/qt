import sys
from PyQt5.QtWidgets import (QRadioButton, QCheckBox, QPushButton, QLabel, QVBoxLayout, QApplication, QWidget)
from PyQt5.QtCore import Qt


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel('Which do you like best?')
        self.dog = QRadioButton('Dogs')
        self.dog.setChecked(True)
        self.cat = QRadioButton('Cats')
        self.btn = QPushButton('Select')


        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.dog)
        layout.addWidget(self.cat)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.setWindowTitle('lesson 10 radio button')
        self.btn.clicked.connect(lambda: self.btn_clicked(self.dog.isChecked(), self.lbl))
        self.show()

    def btn_clicked(self, chk, lbl):
        if chk:
            lbl.setText('you like dogs')
        else:
            lbl.setText('dog hater')

app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec())
