from BaslerCamera import Basler
from HMI import MainWindow
from PyQt5.QtWidgets import QApplication

class APP(MainWindow):
    def __init__(self,parent=None):
        super(APP,self).__init__(parent)
        self.cam = Basler()

    def savePicture(self):
        super(APP,self).savePicture()
        self.img = self.cam.get_image()

    def configure(self):
        pass

    def setLed(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())