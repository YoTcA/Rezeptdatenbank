import sys
import Database_Files
from PyQt5 import QtCore, QtGui, QtWidgets
import SearchRecipe
import NewRecipe


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

        self.tabs.addTab(SearchRecipe.SearchRecipe(self), "Search Recipe")
        self.tabs.addTab(NewRecipe.NewRecipe(self), "New Recipe")
        self.tabs.addTab(QtWidgets.QLabel("Hello"), "Display Recipe")






def main():
    app = QtWidgets.QApplication(sys.argv)
    w = RecipeDB()
    w.show()
    Database_Files.create_table()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()







