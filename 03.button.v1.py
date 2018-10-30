import sys
from PyQt5 import QtWidgets, QtGui


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton(w)
    l = QtWidgets.QLabel(w)
    b.setText('Push Me')
    l.setText('I am a label')

    w.setWindowTitle('Lesson 3.1 ... start adding a button')
    b.move(100, 50)
    l.move(110,100)
    w.setGeometry(100, 100, 1000, 400)

    w.show()
    sys.exit(app.exec_())

window()