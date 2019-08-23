import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

##
class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.statusBar().showMessage("Immer noch Hello world")
        exitMe = QAction("&Exit", self)
        exitMe.setShortcut("Ctrl+Q")
        exitMe.setStatusTip("Exit")
        exitMe.triggered.connect(self.close)

        menubar = self.menuBar()
        file = menubar.addMenu("&File")
        file.addAction(exitMe)

        toolBar = self.addToolBar("Exit")
        toolBar.addAction(exitMe)

        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("Hello World")
        self.show()


app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec_())