import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        status_bar = self.statusBar()
        status_bar.showMessage("Hello")

        self.setStyleSheet("QLabel {font: 10pt Arial}")



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

        # Textformating
        self.normal_font = QtGui.QFont("Helvetica", 10)

        #self.show()
        '''self.main_window = QtWidgets.QWidget(self)
        self.main_window.setLayout(QtWidgets.QVBoxLayout(self))
        self.setCentralWidget(self.main_window)
        self.main_window.addWidget(MainWidget(self))'''
        self.main_widget = MainWidget(self)
        #self.search_widget = SearchWidget(self)
        #self.setCentralWidget(self.search_widget)
        self.setCentralWidget(self.main_widget)
        #self.setCentralWidget(self.search_widget)



class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        # Top area for picture, effort, duration and rating
        top_area = TopWidget(self)
        self.layout.addWidget(top_area)

        # Bottom area for ingredients and instructions
        bot_area = BotWidget(self)
        self.layout.addWidget(bot_area)

class TopWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

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
        self.parent = parent

        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)
        picture = QtWidgets.QLabel("Placeholder", self)
        picture.setStyleSheet("background: darkblue")
        self.layout.addWidget(picture)

class TopMidWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(TopMidWidget, self).__init__(parent)
        self.parent = parent

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)


class TopRightWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(TopRightWidget, self).__init__(parent)
        self.parent = parent

        self.layout = QtWidgets.QGridLayout(self)
        self.setLayout(self.layout)


        self.tags_width = 55

        # Display tags
        tags = TagsWidget(self)
        self.layout.addWidget(tags, 0, 0, 1, 5)

        # Display duration
        duration = DurationWidget(self)
        self.layout.addWidget(duration, 1, 0)

        # Display portion size
        portion = PortionWidget(self)
        self.layout.addWidget(portion, 1, 1)

        # Display effort estimation
        effort = EffortWidget(self)
        self.layout.addWidget(effort, 2, 0)

        #Display rating
        rating = RatingWidget(self)
        self.layout.addWidget(rating, 2, 1)

class TagsWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(TagsWidget, self).__init__(parent)
        self.parent = parent

        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)

        # Label for Tags
        tags_label = QtWidgets.QLabel("Tags:",self)
        tags_label.setAlignment(QtCore.Qt.AlignRight)
        tags_label.setFixedWidth(parent.tags_width)
        self.layout.addWidget(tags_label)

        # Area to display tags
        self.tags_display = QtWidgets.QLabel("No tags available.", self)
        self.tags_display.setAlignment(QtCore.Qt.AlignLeft)
        self.layout.addWidget(self.tags_display)
        self.layout.addStretch(1)

class DurationWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(DurationWidget, self).__init__(parent)
        self.parent = parent

        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)

        # Label
        label = QtWidgets.QLabel("Duration:", self)
        label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        label.setFixedWidth(parent.tags_width)
        self.layout.addWidget(label)

        # Textbox with Value
        textbox = QtWidgets.QLineEdit("N/A", self)
        textbox.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        textbox.setFixedWidth(25)
        self.layout.addWidget(textbox)

        # Unit label for duration
        unit = QtWidgets.QLabel("min", self)
        unit.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.layout.addWidget(unit)

class PortionWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(PortionWidget, self).__init__(parent)
        self.parent = parent

        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)

        # Label for number of portions
        portions = QtWidgets.QLabel("Portions:", self)
        portions.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        portions.setFixedWidth(parent.tags_width)
        self.layout.addWidget(portions)

        # Choose number of portions
        portions_select = QtWidgets.QDoubleSpinBox(self)
        portions_select.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        portions_select.setDecimals(1)
        self.layout.addWidget(portions_select)
        self.layout.addStretch(1)
'''
class DurationAndPortionWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(DurationAndPortionWidget, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)

        # Label
        label = QtWidgets.QLabel("Duration:", self)
        label.setAlignment(QtCore.Qt.AlignRight)
        label.setFixedWidth(parent.tags_width)
        self.layout.addWidget(label)

        # Textbox with Value
        textbox = QtWidgets.QLineEdit("N/A", self)
        textbox.setAlignment(QtCore.Qt.AlignLeft)
        textbox.setFixedWidth(25)
        self.layout.addWidget(textbox)

        # Unit label for duration
        unit = QtWidgets.QLabel("min",self)
        unit.setAlignment(QtCore.Qt.AlignLeft)
        self.layout.addWidget(unit)

        self.layout.addSpacing(50)

        # Label for number of portions
        portions = QtWidgets.QLabel("Portions:", self)
        portions.setAlignment(QtCore.Qt.AlignRight)
        self.layout.addWidget(portions)

        # Choose number of portions
        portions_select = QtWidgets.QDoubleSpinBox(self)
        portions_select.setAlignment(QtCore.Qt.AlignLeft)
        self.layout.addWidget(portions_select)
        self.layout.addStretch(1)
'''
class EffortWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(EffortWidget, self).__init__(parent)
        self.parent = parent

        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)

        # Add effort label
        effort_label = QtWidgets.QLabel("Effort:")
        effort_label.setAlignment(QtCore.Qt.AlignRight)
        effort_label.setFixedWidth(parent.tags_width)
        self.layout.addWidget(effort_label)

        # Add effort rating radio buttons
        self.effort_grid = QtWidgets.QGridLayout()
        self.effort_grid.setAlignment(QtCore.Qt.AlignLeft)
        self.effort_grid.setColumnStretch(1, 1)
        self.effort_grid.setContentsMargins(0, 0, 0, 0)
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
        self.layout.addStretch(1)

class RatingWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(RatingWidget, self).__init__(parent)
        self.parent = parent

        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)

        # Add rating label
        self.rating_label = QtWidgets.QLabel("Rating:")
        self.rating_label.setAlignment(QtCore.Qt.AlignRight)#| QtCore.Qt.AlignVCenter)
        self.rating_label.setFixedWidth(parent.tags_width)
        self.layout.addWidget(self.rating_label)

        # Add effort rating radio buttons
        self.rating_grid = QtWidgets.QGridLayout()
        self.rating_grid.setAlignment(QtCore.Qt.AlignLeft| QtCore.Qt.AlignVCenter)
        self.rating_grid.setColumnStretch(1, 1)
        #self.rating_grid.addWidget(self.rating_label,1,0)
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
'''
class EffortAndRatingWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(EffortAndRatingWidget, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)

        # Add effort label
        self.effort_label = QtWidgets.QLabel("Effort:")
        self.effort_label.setAlignment(QtCore.Qt.AlignRight)
        self.effort_label.setFixedWidth(parent.tags_width)
        self.layout.addWidget(self.effort_label)

        # Add effort rating radio buttons
        self.effort_grid = QtWidgets.QGridLayout()
        self.effort_grid.setAlignment(QtCore.Qt.AlignLeft)
        self.effort_grid.setColumnStretch(1, 1)
        self.effort_grid.setContentsMargins(0,0,0,0)
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
        self.rating_label.setFixedWidth(parent.tags_width)
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
'''
class BotWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(BotWidget, self).__init__(parent)
        self.parent = parent

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
        self.parent = parent

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
        self.parent = parent

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        # Label for instructions
        instructions_label = QtWidgets.QLabel("Instructions", self)
        self.layout.addWidget(instructions_label)

        # Area to display instructions
        instructions_text = QtWidgets.QTextEdit(self)
        instructions_text.setMinimumWidth(300)
        self.layout.addWidget(instructions_text)

class SearchWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(SearchWidget, self).__init__(parent)
        self.parent = parent

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)
        self.layout.addWidget(QtWidgets.QLabel("Test"))



app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())