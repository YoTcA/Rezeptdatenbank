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

        # Menu File
        menu_new = QAction("&New Recipe", self)
        menu_new.setShortcut("Ctrl+N")
        menu_new.setStatusTip("Create New Recipe")
        # Funktion einfügen!

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

        # Top area for picture, effort, duration and rating
        top_area = TopWidget(self)
        self.layout.addWidget(top_area)

        # Middle area for portion size and tags
        mid_area = MidWidget(self)
        self.layout.addWidget(mid_area)

        # Bottom area for ingredients and instructions
        bot_area = BotWidget(self)
        self.layout.addWidget(bot_area)

class TopWidget(QWidget):
    def __init__(self, parent):
        super(TopWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        top_left = TopLeftWidget(self)
        top_left.setFixedSize(150, 150)
        self.layout.addWidget(top_left)

        top_middle = TopMidWidget(self)
        top_middle.setFixedWidth(100)
        self.layout.addWidget(top_middle)


        top_right = TopRightWidget(self)
        self.layout.addWidget(top_right)


class TopLeftWidget(QWidget):
    def __init__(self, parent):
        super(TopLeftWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        picture = QLabel("Placeholder", self)

        self.layout.addWidget(picture)

class TopMidWidget(QWidget):
    def __init__(self, parent):
        super(TopMidWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        #self.layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.layout)
        label_height = 25
        label_font = QFont("Arial",10)

        # Label to display the duration label
        duration = QLabel("Duration:", self)
        duration.setAlignment(Qt.AlignRight)
        duration.setFixedHeight(label_height)
        duration.setFont(label_font)
        self.layout.addWidget(duration)

        # Label to display the effort label
        effort = QLabel("Effort:", self)
        effort.setFixedHeight(label_height)
        effort.setAlignment(Qt.AlignRight)
        effort.setFont(label_font)
        self.layout.addWidget(effort)

        # Label to display the rating label
        rating = QLabel("Rating:", self)
        rating.setFixedHeight(label_height)
        rating.setAlignment(Qt.AlignRight)
        rating.setFont(label_font)
        self.layout.addWidget(rating)

class TopRightWidget(QWidget):
    def __init__(self, parent):
        super(TopRightWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        #self.layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.layout)
        textbox_height = 25

        # Area to display the duration of the recipe
        duration = QLineEdit("No duration avaliable.", self)
        duration.setReadOnly(True)
        duration.setFixedHeight(textbox_height)
        self.layout.addWidget(duration)

        # Area to display the effort of the recipe
        effort = QLineEdit("No effort rating avaliable.", self)
        effort.setReadOnly(True)
        effort.setFixedHeight(textbox_height)
        self.layout.addWidget(effort)

        # Area to display the rating of the recipe
        rating = QLineEdit("No rating avaliable.", self)
        rating.setReadOnly(True)
        rating.setFixedHeight(textbox_height)
        self.layout.addWidget(rating)

class MidWidget(QWidget):
    def __init__(self, parent):
        super(MidWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)
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

class MidLeftWidget(QWidget):
    def __init__(self, parent):
        super(MidLeftWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        # Label for number of portions
        portions = QLabel("Portions:", self)
        self.layout.addWidget(portions)

        # Choose number of portions
        portions_select = QDoubleSpinBox(self)
        self.layout.addWidget(portions_select)

class MidMidWidget(QWidget):
    def __init__(self, parent):
        super(MidMidWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        # Label for tags
        tags = QLabel("Tags:", self)
        tags.setAlignment(Qt.AlignRight)
        self.layout.addWidget(tags)

class MidRightWidget(QWidget):
    def __init__(self, parent):
        super(MidRightWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)


        # Area to display tags
        tags_display = QLineEdit("Placeholder", self)
        tags_display.setReadOnly(True)
        self.layout.addWidget(tags_display)



class BotWidget(QWidget):
    def __init__(self, parent):
        super(BotWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # Area for ingredients
        bot_left = BotLeftWidget(self)
        self.layout.addWidget(bot_left,0)

        # Area for instructions
        bot_right = BotRightWidget(self)
        self.layout.addWidget(bot_right,1)

class BotLeftWidget(QWidget):
    def __init__(self, parent):
        super(BotLeftWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        # Label for ingredients
        ingredients_label = QLabel("Ingredients", self)
        self.layout.addWidget(ingredients_label)

        # Area to display ingredients
        ingredients_table = QTableView(self)
        ingredients_table.setFixedWidth(250)
        self.layout.addWidget(ingredients_table)

class BotRightWidget(QWidget):
    def __init__(self, parent):
        super(BotRightWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        # Label for instructions
        instructions_label = QLabel("Instructions", self)
        self.layout.addWidget(instructions_label)

        # Area to display instructions
        instructions_text = QTextEdit(self)
        instructions_text.setMinimumWidth(300)
        self.layout.addWidget(instructions_text)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())