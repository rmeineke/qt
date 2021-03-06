import sys
from PyQt5 import QtWidgets, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.b = QtWidgets.QPushButton('Push Me')
        self.l = QtWidgets.QLabel('Not Clicked Yet')

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.b)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('lesson 5 .. button')

        self.b.clicked.connect(self.btn_click)
        self.show()

    def btn_click(self):
        self.l.setText('CLICKED!')


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec())