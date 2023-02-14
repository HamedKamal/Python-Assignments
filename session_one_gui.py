# from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class window(QMainWindow):
    def __init__(self):
        super().__init__()
    def setupui(self):
        self.resize(500,500)
        self.label=QLabel(self)
        self.label.setGeometry(QRect(300,200,140,100))
        self.btn=QPushButton(self)
        self.btn.setGeometry(QRect(100,200,140,100))
        self.btn.setText('push me')
        self.label.setText('hello world')
        self.radio=QRadioButton('one',self)
        self.radio2=QRadioButton('two',self)
        self.radio.setGeometry(QRect(100,400,100,30))
        self.radio2.setGeometry(QRect(250,400,100,30))
        self.combobox=QComboBox(self)
        self.combobox.addItems(['1','2','3'])
        self.combobox.setGeometry(QRect(50,30,70,30))
        self.check1=QCheckBox('s',self)
        self.check2=QCheckBox('k',self)
        self.check1.setGeometry(QRect(200,20,100,50))
        self.check2.setGeometry(QRect(350,20,100,50))
if __name__=='__main__':
    app=QApplication(sys.argv)
    mainWidow=window()
    mainWidow.setupui()
    mainWidow.show()
    sys.exit(app.exec_())