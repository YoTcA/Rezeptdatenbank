import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        StatusBar = self.statusBar()
        StatusBar.showMessage("Hello")

        #Menu File
        MenuNew = QAction("&New Recipe", self)
        MenuNew.setShortcut("Ctrl+N")
        MenuNew.setStatusTip("Create New Recipe")
        #Funktion einfügen!

        MenuExit = QAction("&Exit", self)
        MenuExit.setShortcut("Ctrl+Q")
        MenuExit.setStatusTip("Exit Program")
        MenuExit.triggered.connect(self.close)

        MenuBar = self.menuBar()
        MenuFile = MenuBar.addMenu("&File")
        MenuFile.addAction(MenuNew)
        MenuFile.addAction(MenuExit)

        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("Rezeptdatenbank V0.1")
        #self.show()
        self.MainWidget = MainWidget(self)
        self.setCentralWidget(self.MainWidget)

class MainWidget(QWidget):
    def __init__(self, parent):
        super(MainWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.button1 = QPushButton("Button 1")
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton("Button 2")
        self.layout.addWidget(self.button2)

        self.setLayout(self.layout)






app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())