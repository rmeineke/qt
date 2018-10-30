import sys
from PyQt5 import QtWidgets, QtGui


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton('Push Me')
    l = QtWidgets.QLabel('Labeled here')

    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(l)
    h_box.addStretch()

    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(b)

    v_box.addLayout(h_box)
    w.setLayout(v_box)
    w.setWindowTitle('Lesson 3.2 ... start adding a button')

    w.show()
    sys.exit(app.exec_())

window()