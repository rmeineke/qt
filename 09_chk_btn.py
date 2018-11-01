import sys
from PyQt5.QtWidgets import (QCheckBox, QPushButton, QLabel, QVBoxLayout, QApplication, QWidget)
from PyQt5.QtCore import Qt


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel()
        self.cbx = QCheckBox('Do you like dogs?')
        self.btn = QPushButton('Push Me')

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.cbx)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.setWindowTitle('lesson 8 slider')
        self.btn.clicked.connect(lambda: self.btn_clicked(self.cbx.isChecked(), self.lbl))
        self.show()

    def btn_clicked(self, chk, lbl):
        if chk:
            lbl.setText('you like dogs')
        else:
            lbl.setText('dog hater')

app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec())
