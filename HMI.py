import sys
from PyQt5 import QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUi
import cv2

class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        loadUi('HMI.ui', self)

        self.btn_led.clicked.connect(self.setLed)
        self.btn_save.clicked.connect(self.savePicture)
        self.btn_configure.clicked.connect(self.configure)
        self.btn_start.clicked.connect(self.live)
        self.data = []
        self.img = None
        self.islive = True
        self.btn_start.toggle()
        self.displaytimer = QTimer(self)
        self.displaytimer.timeout.connect(self.display)
        self.displaytimer.start(100)

    def status_changed(self,info):
        pass

    def imagelist_changed(self,imagename):
        item = QtWidgets.QListWidgetItem()
        item.setText(imagename)
        self.list_imagename.addItem(item)

    def live(self):
        self.islive = self.btn_start.isChecked()
        if self.islive:
            self.btn_start.setText("Live")
        else:
            self.btn_start.setText("Image")

    def display(self):
        self.img = cv2.imread("shot.png")
        self.refresh(self.img)

    def refresh(self,img):
        qimage = QtGui.QImage(img, img.shape[1], img.shape[0],
                              QtGui.QImage.Format_RGB888)

        self.pixmap = QtGui.QPixmap(qimage)
        self.imageview.setPixmap( self.pixmap)

    #@abc.abstractmethod()
    def savePicture(self):
        work_order = self.line_workorder.text()
        part_number = self.line_partnumber.text()
        serial_number = self.line_serialnumber.text()
        operator_number = self.line_operatornumber.text()
        process = self.line_process.currentText()
        self.data = [work_order,part_number,serial_number,operator_number,process]

    #@abc.abstractmethod()
    def configure(self):
        pass

    #@abc.abstractmethod()
    def setLed(self):
        pass

    def getimagename(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
