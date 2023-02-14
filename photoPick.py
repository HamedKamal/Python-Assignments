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
        
        self.label.setGeometry(100,300,200,200)
        
        self.button=QPushButton(self)
        self.button.setText('load file ')
        self.button.setGeometry(100,200,140,100)
        self.button.clicked.connect(self.readphoto)
    def readphoto(self):
        self.dialog=QFileDialog()
        path,cheak=self.dialog.getOpenFileName(self,'open file ')
        self.label.setPixmap(QPixmap(path))
        self.label.setScaledContents(True)
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    mainWidow=Window()
    mainWidow.setupui()
    mainWidow.show()
    sys.exit(app.exec_())