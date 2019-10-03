from PyQt5 import QtCore, QtGui, QtWidgets
import Database_Files
import Functions


# check if there is already a recipe with the inputed recipe name in the database



class NewRecipe(QtWidgets.QWidget):
    # Set the width of the labels in the layout
    label_width = 90
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

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

        # Display recipe name
        self.recipe_name = RecipeNameWidget(self)
        self.recipe_name.recipe_name_input.editingFinished.connect(self.recipe_name_check)
        self.info_left_area_layout.addWidget(self.recipe_name)

        # Display duration
        self.duration = DurationWidget(self)
        self.info_left_area_layout.addWidget(self.duration)

        # Display the necessary effort to cook the recipe
        self.effort = EffortWidget(self)
        self.info_left_area_layout.addWidget(self.effort)

        self.info_area_layout.addWidget(self.info_left_area,0)


        # Right side of the info area
        self.info_right_area = QtWidgets.QWidget(self)
        self.info_right_area_layout = QtWidgets.QVBoxLayout(self)
        self.info_right_area.setLayout(self.info_right_area_layout)

        # Display tags
        self.tags = TagsWidget(self)
        self.info_right_area_layout.addWidget(self.tags)

        # Display portion size
        self.portion = PortionWidget(self)
        self.info_right_area_layout.addWidget(self.portion)

        # Display rating
        self.rating = RatingWidget(self)
        self.info_right_area_layout.addWidget(self.rating)

        self.info_area_layout.addWidget(self.info_right_area,1)

        # Bottom Area for ingredients and the recipe
        self.bot_area = QtWidgets.QWidget(self)
        self.bot_area_layout = QtWidgets.QHBoxLayout(self)
        self.bot_area_layout.setContentsMargins(0,0,0,0)
        self.bot_area.setLayout(self.bot_area_layout)

        # Display the ingredients
        self.ingredients = IngredientsWidget(self)
        self.bot_area_layout.addWidget(self.ingredients, 0)

        # Display the recipe
        self.instructions = InstructionsWidget(self)
        self.bot_area_layout.addWidget(self.instructions, 1)

        # Area for buttons
        self.button_area = QtWidgets.QWidget(self)
        self.button_area_layout = QtWidgets.QHBoxLayout(self)
        self.button_area.setLayout(self.button_area_layout)

        # Save button
        self.save_button = QtWidgets.QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_recipe)
        self.button_area_layout.addWidget(self.save_button)

        # Clear button
        self.clear_button = QtWidgets.QPushButton("Clear", self)
        self.button_area_layout.addWidget(self.clear_button)

        self.layout.addWidget(self.top_area)
        self.layout.addWidget(self.bot_area)
        self.layout.addWidget(self.button_area)

    def save_recipe(self):
        try:
            str(self.recipe_name.recipe_name_input.text())
        except:
            print("Recipe name cannot be converted to string")
            recipe_name = "N/A"
        else:
            recipe_name = str(self.recipe_name.recipe_name_input.text())

        try:
            str(self.tags.tags_input.text())
        except:
            print("Tags cannot be converted to string")
            tags = "N/A"
        else:
            tags = str(self.tags.tags_input.text())

        try:
            int(self.duration.duration_input.text())
        except:
            print("Duration is not an int")
            duration: int = 99
        else:
            duration = int(self.duration.duration_input.text())

        try:
            int(self.portion.portions_select.value())
        except:
            print("Portions not an int")
            portions: int = 99
        else:
            portions = int(self.portion.portions_select.value())

        if self.effort.low_effort.isChecked():
            effort: int = 0
        elif self.effort.mid_effort.isChecked():
            effort: int = 1
        elif self.effort.high_effort.isChecked():
            effort: int = 2
        else:
            print("no effort selected")
            effort: int = 99

        if self.rating.rating1.isChecked():
            rating: int = 1
        elif self.rating.rating2.isChecked():
            rating: int = 2
        elif self.rating.rating3.isChecked():
            rating: int = 3
        elif self.rating.rating4.isChecked():
            rating: int = 4
        elif self.rating.rating5.isChecked():
            rating: int = 5
        else:
            print("nof rating selected")
            rating: int = 99


        instructions = self.instructions.instructions_text.toPlainText()

        print(recipe_name)
        print(tags)
        print(duration)
        print(portions)
        print(effort)
        print(rating)
        print(instructions)

        ### Datenformat muss noch für die Datenbank aufbereitet werden!

        Database_Files.add_recipe(recipe_name, tags, duration, portions, effort, rating, instructions)

    def recipe_name_check(self):
        if Database_Files.recipe_already_exists(self.recipe_name.recipe_name_input.text()):
            self.recipe_name.recipe_name_input.setStyleSheet("color: red;")
        else:
            self.recipe_name.recipe_name_input.setStyleSheet("color: black;")





class TagsWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(TagsWidget, self).__init__(parent)
        self.parent = parent

        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)

        # Label for Tags
        tags_label = QtWidgets.QLabel("Tags:",self)
        tags_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        tags_label.setFixedWidth(parent.label_width)
        self.layout.addWidget(tags_label)

        # Area to display tags
        self.tags_input = QtWidgets.QLineEdit(self)
        self.tags_input.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.layout.addWidget(self.tags_input)

class RecipeNameWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)

        # Label for Tags
        recipe_name_label = QtWidgets.QLabel("Recipe Name:",self)
        recipe_name_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        recipe_name_label.setFixedWidth(parent.label_width)
        self.layout.addWidget(recipe_name_label)

        # Area to display tags
        self.recipe_name_input = QtWidgets.QLineEdit(self)
        self.recipe_name_input.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.layout.addWidget(self.recipe_name_input)

class DurationWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(DurationWidget, self).__init__(parent)
        self.parent = parent

        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)

        # Label
        duration_label = QtWidgets.QLabel("Duration:", self)
        duration_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        duration_label.setFixedWidth(parent.label_width)
        self.layout.addWidget(duration_label)

        # Textbox with Value
        self.duration_input = QtWidgets.QLineEdit(self)
        self.duration_input.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.duration_input.setFixedWidth(25)
        self.layout.addWidget(self.duration_input)

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
        self.mid_effort.setChecked(True)
        self.high_effort = QtWidgets.QRadioButton(self)
        self.effort_grid.addWidget(self.low_effort, 0, 0)
        self.effort_grid.addWidget(self.mid_effort, 0 ,1)
        self.effort_grid.addWidget(self.high_effort, 0 ,2)
        for i in range(3):
            self.effort_grid.setColumnMinimumWidth(i, 50)

        # Label radio buttons
        self.effort_grid.addWidget(QtWidgets.QLabel("Low"), 1, 0)
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
        portions_label = QtWidgets.QLabel("Portions:", self)
        portions_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        portions_label.setFixedWidth(parent.label_width)
        self.layout.addWidget(portions_label)

        # Choose number of portions
        self.portions_select = QtWidgets.QDoubleSpinBox(self)
        self.portions_select.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.portions_select.setDecimals(1)
        self.layout.addWidget(self.portions_select)
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
        self.rating3.setChecked(True)
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
        self.ingredients_table.setRowCount(50)
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

class InstructionsWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        # Label for instructions
        instructions_label = QtWidgets.QLabel("Instructions", self)
        self.layout.addWidget(instructions_label)

        # Area to display instructions
        self.instructions_text = QtWidgets.QTextEdit(self)
        self.instructions_text.setMinimumWidth(300)
        self.layout.addWidget(self.instructions_text)

if __name__ == "__main__":
    import Rezeptdatenbankk
