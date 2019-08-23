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
        grid = QGridLayout()
        namen = ["1","2","3","4","5","6","7","8","9"]
        posis = [(i,j) for i in range(3) for j in range(3)]
        for pos, name in zip(posis, namen):
            button = QPushButton(name)
            grid.addWidget(button, *pos)


        self.setLayout(grid)
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("Hello World")
        self.show()


app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec_())