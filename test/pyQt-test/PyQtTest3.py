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
        upvote = QPushButton("Upvote Me")
        abo = QPushButton("Abo me")
        h = QHBoxLayout()
        h.addStretch(1)
        h.addWidget(upvote)
        h.addWidget(abo)
        h.addStretch(1)
        v = QVBoxLayout()
        v.addStretch(1)
        v.addLayout(h)
        self.setLayout(v)
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("Hello World")
        self.show()


app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec_())