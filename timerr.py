# هو مش قد كدا و اخر حته واخدها زي ما هي بس اضغط فى الوقت الاسبوع ده بدايه دراسه وكدا بس ناوى اشوف حجات اكتر فى الموضوع ده عموما
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

    def setupui(self):
        self.stateStart = True
        self.stateStop = True

        self.resize(500, 500)
        self.labell = QLabel(self)
        self.labell = QLabel(self)
        self.labell.setGeometry(QRect(300, 300, 250, 150))


        self.startTime = QPushButton(self)
        self.startTime.setText('Start Timer')
        self.startTime.setGeometry(300, 200, 100, 50)
        self.startTime.clicked.connect(self.starttime)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showtime)
        self.StopClock = QPushButton(self)
        self.StopClock.setText(' Stop Clock')
        self.StopClock.setGeometry(400, 200, 100, 50)
        self.StopClock.clicked.connect(self.stoptimer)

        # self.switchh.clicked.connect(self.switchhhstop

        self.count = 0

        # creating flag
        self.flag = False

        # creating a label to show the time
        self.label = QLabel(self)

        # setting geometry of label
        self.label.setGeometry(75, 100, 250, 70)

        # adding border to the label
        self.label.setStyleSheet("border : 4px solid black;")

        # setting text to the label
        self.label.setText(str(self.count))

        # setting font to the label
        self.label.setFont(QFont('Arial', 25))

        # setting alignment to the text of label
        self.label.setAlignment(Qt.AlignCenter)

        # creating start button
        start = QPushButton("Start", self)

        # setting geometry to the button
        start.setGeometry(125, 250, 150, 40)

        # add action to the method
        start.pressed.connect(self.Start)

        # creating pause button
        pause = QPushButton("Pause", self)

        # setting geometry to the button
        pause.setGeometry(125, 300, 150, 40)

        # add action to the method
        pause.pressed.connect(self.Pause)

        # creating reset button
        re_set = QPushButton("Re-set", self)

        # setting geometry to the button
        re_set.setGeometry(125, 350, 150, 40)

        # add action to the method
        re_set.pressed.connect(self.Re_set)

        # creating a timer object
        timer = QTimer(self)

        # adding action to timer
        timer.timeout.connect(self.showTime)

        # update the timer every tenth second
        timer.start(100)

    # method called by timer
    def showTime(self):

        # checking if flag is true
        if self.flag:

            # incrementing the counter
            self.count += 1

        # getting text from count
        text = str(self.count / 10)

        # showing text
        self.label.setText(text)

    def Start(self):

        # making flag to true
        self.flag = True

    def Pause(self):

        # making flag to False
        self.flag = False

    def Re_set(self):

        # making flag to false
        self.flag = False

        # resetting the count
        self.count = 0

        # setting text to label
        self.label.setText(str(self.count))

    def showtime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.labell.setText(timeDisplay)

    def starttime(self):

        self.timer.start(1000)
        self.stateStart = False
        self.stateStop = True
        self.startTime.setEnabled(self.stateStart)
        self.StopClock.setEnabled(self.stateStop)

    def stoptimer(self):
        self.stateStart = True
        self.stateStop = False
        self.timer.disconnect()
        self.startTime.setEnabled(self.stateStart)
        self.StopClock.setEnabled(self.stateStop)

        # self.startTime.setEnabled(self.stateStart)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWidow = Window()
    mainWidow.setupui()
    mainWidow.show()
    sys.exit(app.exec_())
