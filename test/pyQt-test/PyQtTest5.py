import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

##
class Fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        w = QLabel(self)
        w.setText("<a href='https://www.google.com'>Zu Google</a>")
        w.setOpenExternalLinks(False)
        w.linkActivated.connect(self.clicked)

        w2 = QCheckBox("Check Me", self)
        w2.move(50,50)
        w2.stateChanged.connect(self.clicked)

        w3 = QPushButton("toggleme", self)
        w3.setCheckable(True)
        w3.move(50,100)
        w3.clicked[bool].connect(self.clicked2)

        w4 = QRadioButton("Ckeck me", self)
        w4.setCheckable(True)
        w4.move(50,150)
        w4.toggled.connect(self.clicked2)




        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("Hello World")
        self.show()

    def clicked(self):
        print("clicked")

    def clicked2(self, down):
        if down:
            print("Down")
        else:
            print("Up")


app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec_())