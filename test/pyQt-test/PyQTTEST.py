import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

### Lässt den Knopf verschwinden (also sich selbst)
class MyButton(QPushButton):
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.close()

class EigenerEvent(QObject):
    schliessmichEvent = pyqtSignal()


class Fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.sig = EigenerEvent()
        self.sig.schliessmichEvent.connect(self.close)
        QToolTip.setFont(QFont("Arial", 14))
        button = QPushButton('Drück mich', self)
        button.move(50,50)
        button.setToolTip("Bitte <b>drücken</b>")
        button.clicked.connect(self.gedrueckt)
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("Hello World")
        self.show()

    def gedrueckt(self):
        sender = self.sender()
        sender.move(100,100)

### hier kann man hotkeys definieren!
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_W:
            self.sig.schliessmichEvent.emit()


app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec_())