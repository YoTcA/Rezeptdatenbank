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
        self.setGeometry(50, 50, 1024, 768)
        self.setWindowTitle("Rezeptdatenbank V" + version)

        # Status bar
        status_bar = self.statusBar()
        status_bar.showMessage("RecipeDB V" + version)

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

        self.tabs = QtWidgets.QTabWidget(self)
        self.setCentralWidget(self.tabs)

        self.tabs.addTab(SearchRecipe(self), "Search Recipe")
        self.tabs.addTab(NewRecipe(self), "New Recipe")
        self.tabs.addTab(QtWidgets.QLabel("Hello"), "Display Recipe")

class SearchRecipe(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # Define main vertical layout
        layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(layout)

        # Search area
        self.search_area = QtWidgets.QWidget(self)
        search_area_layout = QtWidgets.QHBoxLayout(self)
        self.search_area.setLayout(search_area_layout)
        search_label = QtWidgets.QLabel("Search:", self)
        search_area_layout.addWidget(search_label)
        self.search_input = QtWidgets.QLineEdit(self)
        search_area_layout.addWidget(self.search_input)
        self.search_button = QtWidgets.QPushButton("Search", self)
        search_area_layout.addWidget(self.search_button)
        layout.addWidget(self.search_area)

        # Effort and rating area
        self.effort_rating_area = QtWidgets.QWidget(self)
        self.effort_rating_area_layout = QtWidgets.QHBoxLayout(self)
        self.effort_rating_area.setLayout(self.effort_rating_area_layout)
        layout.addWidget(self.effort_rating_area)
        self.checkbox_spacing = 30

        # Effort area
        self.effort_area = QtWidgets.QWidget(self)
        effort_area_layout = QtWidgets.QHBoxLayout(self)
        self.effort_area.setLayout(effort_area_layout)
        # Effort label
        effort_label = QtWidgets.QLabel("Effort:", self)
        effort_label.setAlignment(QtCore.Qt.AlignTop)
        effort_area_layout.addWidget(effort_label)
        # Effort select
        self.effort_grid = QtWidgets.QGridLayout(self)
        self.effort1 = QtWidgets.QCheckBox(self)
        self.effort1.setChecked(1)
        self.effort2 = QtWidgets.QCheckBox(self)
        self.effort2.setChecked(1)
        self.effort3 = QtWidgets.QCheckBox(self)
        self.effort3.setChecked(1)
        self.effort_grid.addWidget(self.effort1, 0, 0)
        self.effort_grid.addWidget(self.effort2, 0, 1)
        self.effort_grid.addWidget(self.effort3, 0, 2)
        for i in range(3):
            self.effort_grid.setColumnMinimumWidth(i, self.checkbox_spacing)
        self.effort_grid.addWidget(QtWidgets.QLabel("Low"), 1, 0)
        self.effort_grid.addWidget(QtWidgets.QLabel("High"), 1, 2)
        effort_area_layout.addLayout(self.effort_grid)
        self.effort_rating_area_layout.addWidget(self.effort_area)


        # Rating area
        self.rating_area = QtWidgets.QWidget(self)
        rating_area_layout = QtWidgets.QHBoxLayout(self)
        self.rating_area.setLayout(rating_area_layout)
        # Rating label
        rating_label = QtWidgets.QLabel("Rating:", self)
        rating_label.setAlignment(QtCore.Qt.AlignTop)
        rating_area_layout.addWidget(rating_label)
        # Rating select
        self.rating_grid = QtWidgets.QGridLayout(self)
        self.rating1 = QtWidgets.QCheckBox(self)
        self.rating1.setChecked(1)
        self.rating2 = QtWidgets.QCheckBox(self)
        self.rating2.setChecked(1)
        self.rating3 = QtWidgets.QCheckBox(self)
        self.rating3.setChecked(1)
        self.rating4 = QtWidgets.QCheckBox(self)
        self.rating4.setChecked(1)
        self.rating5 = QtWidgets.QCheckBox(self)
        self.rating5.setChecked(1)
        self.rating_grid.addWidget(self.rating1, 0, 0)
        self.rating_grid.addWidget(self.rating2, 0, 1)
        self.rating_grid.addWidget(self.rating3, 0, 2)
        self.rating_grid.addWidget(self.rating4, 0, 3)
        self.rating_grid.addWidget(self.rating5, 0, 4)
        for i in range(5):
            self.rating_grid.setColumnMinimumWidth(i, self.checkbox_spacing)
        self.rating_grid.addWidget(QtWidgets.QLabel("1"), 1, 0)
        self.rating_grid.addWidget(QtWidgets.QLabel("5"), 1, 4)
        rating_area_layout.addLayout(self.rating_grid)
        self.effort_rating_area_layout.addWidget(self.rating_area)
        self.effort_rating_area_layout.addStretch(1)

        self.recipes = QtWidgets.QTableWidget(self)
        layout.addWidget(self.recipes)


class NewRecipe(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)
        # Set the width of the labels in the layout
        self.label_width = 55

        # Top area for picture, effort, duration and rating
        self.top_area = QtWidgets.QWidget(self)
        self.top_area_layout = QtWidgets.QHBoxLayout(self)
        self.top_area.setLayout(self.top_area_layout)

        # Add picture
        self.picture = QtWidgets.QLabel("Placeholder", self)
        self.picture.setFixedSize(150,150)
        self.picture.setStyleSheet("background: darkblue")
        self.top_area_layout.addWidget(self.picture)

        # Top right area for additional information
        self.info_area = QtWidgets.QWidget(self)
        self.info_area_layout = QtWidgets.QHBoxLayout(self)
        self.info_area.setLayout(self.info_area_layout)
        self.top_area_layout.addWidget(self.info_area)


        # Left side of the info area
        self.info_left_area = QtWidgets.QWidget(self)
        self.info_left_area_layout = QtWidgets.QVBoxLayout(self)
        self.info_left_area.setLayout(self.info_left_area_layout)

        # Display Duration
        duration = DurationWidget(self)
        self.info_left_area_layout.addWidget(duration)

        # Display the necessary effort to cook the recipe
        effort = EffortWidget(self)
        self.info_left_area_layout.addWidget(effort)

        self.info_area_layout.addWidget(self.info_left_area,0)


        # Right side of the info area
        self.info_right_area = QtWidgets.QWidget(self)
        self.info_right_area_layout = QtWidgets.QVBoxLayout(self)
        self.info_right_area.setLayout(self.info_right_area_layout)

        # Display portion size
        portion = PortionWidget(self)
        self.info_right_area_layout.addWidget(portion)

        # Display rating
        rating = RatingWidget(self)
        self.info_right_area_layout.addWidget(rating)

        self.info_area_layout.addWidget(self.info_right_area,1)

        # Bottom Area for ingredients and the recipe
        self.bot_area = QtWidgets.QWidget(self)
        self.bot_area_layout = QtWidgets.QHBoxLayout(self)
        self.bot_area_layout.setContentsMargins(0,0,0,0)
        self.bot_area.setLayout(self.bot_area_layout)

        # Display the ingredients
        ingredients = IngredientsWidget(self)
        self.bot_area_layout.addWidget(ingredients, 0)

        # Display the recipe
        recipe = RecipeWidget(self)
        self.bot_area_layout.addWidget(recipe, 1)

        self.layout.addWidget(self.top_area)
        self.layout.addWidget(self.bot_area)


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
        label.setFixedWidth(parent.label_width)
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

class EffortWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(EffortWidget, self).__init__(parent)
        self.parent = parent

        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)

        # Add effort label
        effort_label = QtWidgets.QLabel("Effort:")
        effort_label.setAlignment(QtCore.Qt.AlignRight)
        effort_label.setFixedWidth(parent.label_width)
        self.layout.addWidget(effort_label)

        # Add effort rating radio buttons
        self.effort_grid = QtWidgets.QGridLayout()
        self.effort_grid.setAlignment(QtCore.Qt.AlignLeft)
        self.effort_grid.setColumnStretch(1, 1)
        self.effort_grid.setContentsMargins(0, 0, 0, 0)
        self.low_effort = QtWidgets.QRadioButton(self)
        self.mid_effort = QtWidgets.QRadioButton(self)
        self.high_effort = QtWidgets.QRadioButton(self)
        self.effort_grid.addWidget(self.low_effort, 0, 0)
        self.effort_grid.addWidget(self.mid_effort, 0 ,1)
        self.effort_grid.addWidget(self.high_effort, 0 ,2)
        for i in range(3):
            self.effort_grid.setColumnMinimumWidth(i, 50)

        # Label radio buttons
        effort_label_low = QtWidgets.QLabel("Low")
        self.effort_grid.addWidget(effort_label_low, 1, 0)
        self.effort_grid.addWidget(QtWidgets.QLabel("High"), 1, 2)
        self.layout.addLayout(self.effort_grid)
        self.layout.addStretch(1)

class PortionWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(PortionWidget, self).__init__(parent)
        self.parent = parent

        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)

        # Label for number of portions
        portions = QtWidgets.QLabel("Portions:", self)
        portions.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        portions.setFixedWidth(parent.label_width)
        self.layout.addWidget(portions)

        # Choose number of portions
        portions_select = QtWidgets.QDoubleSpinBox(self)
        portions_select.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        portions_select.setDecimals(1)
        self.layout.addWidget(portions_select)
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
        self.rating_label.setFixedWidth(parent.label_width)
        self.layout.addWidget(self.rating_label)

        # Add effort rating radio buttons
        self.rating_grid = QtWidgets.QGridLayout()
        self.rating_grid.setAlignment(QtCore.Qt.AlignLeft| QtCore.Qt.AlignVCenter)
        self.rating_grid.setColumnStretch(1, 1)
        #self.rating_grid.addWidget(self.rating_label,1,0)

        self.rating1 = QtWidgets.QRadioButton()
        self.rating2 = QtWidgets.QRadioButton()
        self.rating3 = QtWidgets.QRadioButton()
        self.rating4 = QtWidgets.QRadioButton()
        self.rating5 = QtWidgets.QRadioButton()
        self.rating_grid.addWidget(self.rating1, 0, 0)
        self.rating_grid.addWidget(self.rating2, 0, 1)
        self.rating_grid.addWidget(self.rating3, 0, 2)
        self.rating_grid.addWidget(self.rating4, 0, 3)
        self.rating_grid.addWidget(self.rating5, 0, 4)
        for i in range(5):
            self.rating_grid.setColumnMinimumWidth(i, 30)

        # Label radio buttons
        self.rating_grid.addWidget(QtWidgets.QLabel(" 1"), 1, 0)
        self.rating_grid.addWidget(QtWidgets.QLabel(" 5"), 1, 4)
        self.layout.addLayout(self.rating_grid)
        self.layout.addStretch(1)

class IngredientsWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
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

class RecipeWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
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

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = RecipeDB()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()







