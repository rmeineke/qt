# hello_world.py
from PySide2.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel()
label.setText("Hello Qt for Python!")
label.resize(800,600)
label.show()
app.exec_()