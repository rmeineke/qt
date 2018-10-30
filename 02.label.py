import sys
from PyQt5 import QtWidgets, QtGui


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)
    l2 = QtWidgets.QLabel(w)
    l1.setText('Lesson 2 ... set a label')
    l2.setPixmap(QtGui.QPixmap('t.png'))
    w.setWindowTitle('Lesson 2 ... set a label')
    w.setGeometry(100, 100, 1000, 400)
    l1.move(130, 20)
    l2.move(120,90)
    w.show()
    sys.exit(app.exec_())

window()