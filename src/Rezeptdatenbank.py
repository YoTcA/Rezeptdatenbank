import sys
from PyQt5 import QtCore, QtGui, QtWidgets



class RecipeDB(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)



        # Version
        version = "0.1"

        # Style sheets
        self.setStyleSheet("QLabel {font: 10pt Arial}")

        # Additional start up information
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("Rezeptdatenbank V" + version)

        # Status bar
        status_bar = self.statusBar()
        status_bar.showMessage("RecepeDB V" + version)

        # Menu File
        # New Recipe
        menu_new = QtWidgets.QAction("&New Recipe", self)
        menu_new.setShortcut("Ctrl+N")
        menu_new.setStatusTip("Create New Recipe")
        ### Funktion einfügen!

        # Open Recipe
        menu_open = QtWidgets.QAction("&Open Recipe", self)
        menu_open.setShortcut("Ctrl+O")
        menu_open.setStatusTip("Open Recipe")
        ### Funktion einfügen!

        # Save Recipe
        menu_save = QtWidgets.QAction("&Save", self)
        menu_save.setShortcut("Ctrl+S")
        menu_save.setStatusTip("Save Recipe")

        # Save As Recipe
        menu_save_as = QtWidgets.QAction("Save &As..", self)
        menu_save_as.setShortcut("Ctrl+Shift+S")
        menu_save_as.setStatusTip("Save Recipe As..")

        # Exit Programm
        menu_exit = QtWidgets.QAction("&Exit", self)
        menu_exit.setShortcut("Ctrl+Q")
        menu_exit.setStatusTip("Exit Program")
        menu_exit.triggered.connect(self.close)

        # Build menu bar
        menu_bar = self.menuBar()
        menu_file = menu_bar.addMenu("&File")
        menu_file.addAction(menu_new)
        menu_file.addAction(menu_open)
        menu_file.addAction(menu_save)
        menu_file.addAction(menu_save_as)
        menu_file.addAction(menu_exit)

        # Load Homescreen
        self.recipedisplay()

    def recipedisplay(self):
        self.window1 = Page1(self)
        self.setCentralWidget(self.window1)
        self.show()

    def startsecond(self):
        self.window2 = Page2(self)
        self.setCentralWidget(self.window2)
        self.show()

class Page1(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.agree = QtWidgets.QPushButton("to Page2", self)
        self.agree.move(180,400)
        self.agree.clicked.connect(parent.startsecond)
        self.tabs = QtWidgets.QTabWidget(self)
        self.tabs.addTab(QtWidgets.QLabel("Hello"), "Tag1")
        self.tabs.addTab(QtWidgets.QLabel("Hello"), "Tag2")

class Page2(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.agree2 = QtWidgets.QPushButton("to Page1", self)
        self.agree2.move(200, 400)
        self.agree2.clicked.connect(parent.recipedisplay)




def main():
    app = QtWidgets.QApplication(sys.argv)
    w = RecipeDB()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

'''
        '''





