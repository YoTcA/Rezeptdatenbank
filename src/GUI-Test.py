import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        status_bar = self.statusBar()
        status_bar.showMessage("Hello")

        #Menu File
        menu_new = QAction("&New Recipe", self)
        menu_new.setShortcut("Ctrl+N")
        menu_new.setStatusTip("Create New Recipe")
        #Funktion einfügen!

        menu_exit = QAction("&Exit", self)
        menu_exit.setShortcut("Ctrl+Q")
        menu_exit.setStatusTip("Exit Program")
        menu_exit.triggered.connect(self.close)

        menu_bar = self.menuBar()
        menu_file = menu_bar.addMenu("&File")
        menu_file.addAction(menu_new)
        menu_file.addAction(menu_exit)

        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("Rezeptdatenbank V0.1")
        #self.show()
        self.MainWidget = MainWidget(self)
        self.setCentralWidget(self.MainWidget)

class MainWidget(QWidget):
    def __init__(self, parent):
        super(MainWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        top_area = TopWidget(self)
        self.layout.addWidget(top_area)
        mid_area = MidWidget(self)
        self.layout.addWidget(mid_area)

class TopWidget(QWidget):
    def __init__(self, parent):
        super(TopWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        picture = QLabel("Placeholder", self)
        top_middle = TopMidWidget(self)
        top_right = TopRightWidget(self)
        self.layout.addWidget(picture)
        self.layout.addWidget(top_middle)
        self.layout.addWidget(top_right)
        self.layout.addStretch(1)

class TopMidWidget(QWidget):
    def __init__(self, parent):
        super(TopMidWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        # Label to display the duration label
        duration = QLabel("Duration:", self)
        self.layout.addWidget(duration)

        # Label to display the effort label
        effort = QLabel("Effort:", self)
        self.layout.addWidget(effort)

        # Label to display the rating label
        rating = QLabel("Rating:", self)
        self.layout.addWidget(rating)

class TopRightWidget(QWidget):
    def __init__(self, parent):
        super(TopRightWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        # Area to display the duration of the recipe
        duration = QLineEdit("Duration:", self)
        duration.setReadOnly(True)
        self.layout.addWidget(duration)

        # Area to display the effort of the recipe
        effort = QLineEdit("Effort:", self)
        effort.setReadOnly(True)
        self.layout.addWidget(effort)

        # Area to display the rating of the recipe
        rating = QLineEdit("Rating:", self)
        rating.setReadOnly(True)
        self.layout.addWidget(rating)

class MidWidget(QWidget):
    def __init__(self, parent):
        super(MidWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)

        #Label for number of portions
        portions = QLabel("Portions:", self)
        self.layout.addWidget(portions)

        #Choose number of portions
        portions_select = QDoubleSpinBox(self)
        self.layout.addWidget(portions_select)

        #Label for tags
        tags = QLabel("Tags:", self)
        self.layout.addWidget(tags)

        #Area to display tags
        tags_display = QLineEdit("Placeholder", self)
        tags_display.setReadOnly(True)
        self.layout.addWidget(tags_display)





app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())