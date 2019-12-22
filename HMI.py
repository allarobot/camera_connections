import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        loadUi('HMI.ui', self)
        self.setFixedSize(self.sizeHint())

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
