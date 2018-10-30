import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle('Lesson 1 ... build a window')
    w.show()
    sys.exit(app.exec_())

window()