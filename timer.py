from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
    def setupui(self):
        self.resize(500,500)
        self.label=QLabel(self)
        
        self.label.setGeometry(QRect(170,300,250,150))
        self.button=QPushButton(self)
        self.button.setText('Start Timer')
        self.button.setGeometry(200,200,100,50)
        self.button.clicked.connect(self.startTimer)
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.showTime)
    def showTime(self):
        time=QDateTime.currentDateTime()
        showdate=time.toString('yyyy-mm-dd hh:mm:ss dddd')
        self.label.setText(showdate)
    
    def startTimer(self):
        self.timer.start(1000)
        self.button.setEnabled(False)
if __name__=='__main__':
    app=QApplication(sys.argv)
    mainWidow=Window()
    mainWidow.setupui()
    mainWidow.show()
    sys.exit(app.exec_())