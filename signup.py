# from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class window(QMainWindow):
    def __init__(self):
        super().__init__()
    def setupui(self):
        # self.resize(150,150)

        # self.label.move(100,50)
        
        self.mywindowLayout=QVBoxLayout(self)
        

        self.signUpLayout=QHBoxLayout()
        self.yournameLabel=QLabel(self)
        self.yournameLabel.setText('Name')
        self.yournameEnter=QLineEdit(self)
        self.yournameEnter.setPlaceholderText('Enter your name ')
        self.yournameEnter.textEdited.connect(self.myQline)

        self.signUpLayout.addWidget(self.yournameLabel)
        self.signUpLayout.addWidget(self.yournameEnter)
        self.mywindowLayout.addLayout(self.signUpLayout)

        
        self.ageLayout=QHBoxLayout(self)
        self.yourageLabel=QLabel(self)
        self.yourageLabel.setText('Age')
        self.combo=QComboBox(self)
        self.combo.addItems(['10','11','12','13','14','15','16','17','18','19','20'])
        self.ageLayout.addWidget(self.yourageLabel)
        self.ageLayout.addWidget(self.combo)
        self.mywindowLayout.addLayout(self.ageLayout)
        
        self.genderLayout=QHBoxLayout(self)
        self.gender=QLabel(self)
        self.gender.setText('Gender')
        self.male=QRadioButton()
        self.male.setText('male')
        
        self.female=QRadioButton()
        self.female.setText('female')
        self.genderLayout.addWidget(self.gender)
        self.genderLayout.addWidget(self.male)
        self.genderLayout.addWidget(self.female)
        self.mywindowLayout.addLayout(self.genderLayout)
        
        self.hobbiesLayout=QHBoxLayout(self)
        self.hobbies=QLabel(self)
        self.hobbies.setText('hobbies')
        self.programming=QCheckBox()
        self.programming.setText('programming')
        
        self.painting=QCheckBox()
        self.painting.setText('painting')
        
        self.hobbiesLayout.addWidget(self.hobbies)
        self.hobbiesLayout.addWidget(self.programming)
        self.hobbiesLayout.addWidget(self.painting)
        self.mywindowLayout.addLayout(self.hobbiesLayout)
        
        # self.mywindowLayout.setGeometry(QRect(0,0,100,100))
        widget = QWidget()
        widget.setLayout(self.mywindowLayout)
        self.setCentralWidget(widget)
    def myQline(self,s):
        # print('qline')
        print(s)
if __name__=='__main__':
    app=QApplication(sys.argv)
    mainWidow=window()
    mainWidow.setupui()
    mainWidow.show()
    sys.exit(app.exec_())