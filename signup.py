import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5.QtGui import *
# Subclass QMainWindow to customize your application's main window

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        self.setGeometry(0,0,1000,1000)
        layout = QVBoxLayout()
        label=QLabel('Welcome to our app')
        layout.addWidget(label)
        font=label.font()
        font.setPointSize(30)
        label.setFont(font)
        name=QLineEdit()
        name.setMaxLength(10)
        name.setPlaceholderText('Enter Your Name ')
        layout.addWidget(name)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()