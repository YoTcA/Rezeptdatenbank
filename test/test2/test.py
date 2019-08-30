import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class ButtonBlock(QtWidgets.QWidget):

    def __init__(self, *args):
        super(QtWidgets.QWidget, self).__init__()
        grid = QtWidgets.QGridLayout()
        names = ('One', 'Two', 'Three', 'Four', 'Five',
                 'Six', 'Seven', 'Eight', 'Nine', 'Ten')
        for i, name in enumerate(names):
            button = QtWidgets.QPushButton(name, self)
            button.clicked.connect(self.make_calluser(name))
            row, col = divmod(i, 5)
            grid.addWidget(button, row, col)
        self.setLayout(grid)

    def make_calluser(self, name):
        def calluser():
            print(name)
        return calluser

app = QtWidgets.QApplication(sys.argv)
tb = ButtonBlock()
tb.show()
app.exec_()