import sys
from PyQt5 import QtCore, QtGui, QtWidgets

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

    '''def load_all_recepies(self):
        result = Database_Files.readall_recipes("Rezeptdatenbank.db")
        print(result)

    load_all_recepies'''

if __name__ == "__main__":
    import Rezeptdatenbank
