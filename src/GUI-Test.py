import sys
#from PyQt5.QtWidgets import *
#from PyQt5.QtGui import *
#from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        status_bar = self.statusBar()
        status_bar.showMessage("Hello")

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

        # Additional start up information
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("Rezeptdatenbank V0.1")
        #self.show()
        self.MainWidget = MainWidget(self)
        self.setCentralWidget(self.MainWidget)


class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(MainWidget, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        # Top area for picture, effort, duration and rating
        top_area = TopWidget(self)
        self.layout.addWidget(top_area)

        # Middle area for portion size and tags
        mid_area = MidWidget(self)
        self.layout.addWidget(mid_area)

        # Bottom area for ingredients and instructions
        bot_area = BotWidget(self)
        self.layout.addWidget(bot_area)

class TopWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(TopWidget, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # Add picture area
        top_left = TopLeftPicture(self)
        top_left.setFixedSize(150, 150)
        self.layout.addWidget(top_left)

        # Add additional information area
        top_right = TopRightWidget(self)
        self.layout.addWidget(top_right)


class TopLeftPicture(QtWidgets.QWidget):
    def __init__(self, parent):
        super(TopLeftPicture, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)
        picture = QtWidgets.QLabel("Placeholder", self)
        picture.setStyleSheet("background: darkblue")
        self.layout.addWidget(picture)

class TopRightWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(TopRightWidget, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        # Display duration of the recipe
        duration = DurationWidget(self, "Duration:", "No duration available.")
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(duration)

        # Display effort of the recipe
        effort = EffortAndRatingWidget(self)
        self.layout.addWidget(effort)


class DurationWidget(QtWidgets.QWidget):
    def __init__(self, parent, labeltext, lineeditetext):
        super(DurationWidget, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)

        # Label
        label = QtWidgets.QLabel(labeltext, self)
        label.setAlignment(QtCore.Qt.AlignRight)
        label.setFixedWidth(55)
        self.layout.addWidget(label)

        # Textbox with Value
        textbox = QtWidgets.QLineEdit(lineeditetext, self)
        textbox.setAlignment(QtCore.Qt.AlignLeft)
        self.layout.addWidget(textbox)
        self.layout.addStretch(1)

class EffortAndRatingWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(EffortAndRatingWidget, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)

        # Add effort label
        self.effort_label = QtWidgets.QLabel("Effort:")
        self.effort_label.setAlignment(QtCore.Qt.AlignRight)
        self.effort_label.setFixedWidth(55)
        self.layout.addWidget(self.effort_label)

        # Add effort rating radio buttons
        self.effort_grid = QtWidgets.QGridLayout()
        self.effort_grid.setAlignment(QtCore.Qt.AlignLeft)
        self.effort_grid.setColumnStretch(1, 1)
        self.rating1 = self.effort_grid.addWidget(QtWidgets.QRadioButton(), 1, 2)
        self.rating2 = self.effort_grid.addWidget(QtWidgets.QRadioButton(), 1, 3)
        self.rating3 = self.effort_grid.addWidget(QtWidgets.QRadioButton(), 1, 4)
        self.rating4 = self.effort_grid.addWidget(QtWidgets.QRadioButton(), 1, 5)
        self.rating5 = self.effort_grid.addWidget(QtWidgets.QRadioButton(), 1, 6)

        # Label radio buttons
        effort_label_low = QtWidgets.QLabel(" 1")
        self.effort_grid.addWidget(effort_label_low, 2, 2)
        self.effort_grid.addWidget(QtWidgets.QLabel(" 5"), 2, 6)
        self.layout.addLayout(self.effort_grid)

        # Add rating label
        self.rating_label = QtWidgets.QLabel("Rating:")
        self.rating_label.setAlignment(QtCore.Qt.AlignRight)
        self.rating_label.setFixedWidth(55)
        self.layout.addWidget(self.rating_label)

        # Add effort rating radio buttons
        self.rating_grid = QtWidgets.QGridLayout()
        self.rating_grid.setAlignment(QtCore.Qt.AlignLeft)
        self.rating_grid.setColumnStretch(1, 1)
        self.rating1 = self.rating_grid.addWidget(QtWidgets.QRadioButton(), 1, 2)
        self.rating2 = self.rating_grid.addWidget(QtWidgets.QRadioButton(), 1, 3)
        self.rating3 = self.rating_grid.addWidget(QtWidgets.QRadioButton(), 1, 4)
        self.rating4 = self.rating_grid.addWidget(QtWidgets.QRadioButton(), 1, 5)
        self.rating5 = self.rating_grid.addWidget(QtWidgets.QRadioButton(), 1, 6)

        # Label radio buttons
        self.rating_grid.addWidget(QtWidgets.QLabel(" 1"), 2, 2)
        self.rating_grid.addWidget(QtWidgets.QLabel(" 5"), 2, 6)
        self.layout.addLayout(self.rating_grid)
        self.layout.addStretch(1)





class MidWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(MidWidget, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # Label for number of portions
        portions = MidLeftWidget(self)
        self.layout.addWidget(portions)

        # Label for tags
        tags_label = MidMidWidget(self)
        self.layout.addWidget(tags_label)

        # Displayarea for tags
        tags = MidRightWidget(self)
        self.layout.addWidget(tags)
        self.layout.addStretch(1)

class MidLeftWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(MidLeftWidget, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)
        # Label for number of portions
        portions = QtWidgets.QLabel("Portions:", self)
        self.layout.addWidget(portions)

        # Choose number of portions
        portions_select = QtWidgets.QDoubleSpinBox(self)
        self.layout.addWidget(portions_select)

class MidMidWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(MidMidWidget, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)
        # Label for tags
        tags = QtWidgets.QLabel("Tags:", self)
        self.layout.addWidget(tags)

class MidRightWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(MidRightWidget, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)

        # Area to display tags
        tags_display = QtWidgets.QLabel("No tags available.", self)
        self.layout.addWidget(tags_display)



class BotWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(BotWidget, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # Area for ingredients
        bot_left = BotLeftWidget(self)
        self.layout.addWidget(bot_left,0)

        # Area for instructions
        bot_right = BotRightWidget(self)
        self.layout.addWidget(bot_right,1)

class BotLeftWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(BotLeftWidget, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        # Label for ingredients
        ingredients_label = QtWidgets.QLabel("Ingredients", self)
        self.layout.addWidget(ingredients_label)

        # Area to display ingredients
        self.ingredients_table = QtWidgets.QTableWidget(self)
        self.ingredients_table.setRowCount(1)
        self.ingredients_table.setColumnCount(3)
        self.ingredients_table.verticalHeader().hide()
        self.ingredients_table.horizontalHeader().hide()
        #self.ingredients_table.setHorizontalHeaderLabels(["Qty.","Unit","Ingredient"])
        #self.ingredients_table.setShowGrid(False)
        self.ingredients_table.setFixedWidth(300)
        self.layout.addWidget(self.ingredients_table)
        self.ingredients_table.horizontalHeader().setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeToContents)
        self.ingredients_table.horizontalHeader().setSectionResizeMode(1,QtWidgets.QHeaderView.ResizeToContents)
        self.ingredients_table.horizontalHeader().setSectionResizeMode(2,QtWidgets.QHeaderView.Stretch)

class BotRightWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(BotRightWidget, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        # Label for instructions
        instructions_label = QtWidgets.QLabel("Instructions", self)
        self.layout.addWidget(instructions_label)

        # Area to display instructions
        instructions_text = QtWidgets.QTextEdit(self)
        instructions_text.setMinimumWidth(300)
        self.layout.addWidget(instructions_text)


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())