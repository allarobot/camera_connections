<<<<<<< HEAD
from basler_camera import Basler
from HMI import MainWindow
from PyQt5.QtWidgets import QApplication
import sys
import threading,time
from datetime import datetime
from log import Log
import  os,cv2


class Win(MainWindow):
    def __init__(self,parent=None):
        self.cam = Basler()
        self.log = Log()
        self.selected_image = None
        super(Win,self).__init__(parent)

    def savePicture(self):
        super(Win,self).savePicture()
        str_time = datetime.now().strftime("%y%m%d_%H%M%S")
        image_name = os.path.join("data",str_time+".png")
        self.data.append(image_name)
        self.log.save(self.data)
        cv2.imwrite(image_name,self.img)
        self.imagelist_changed(image_name)

    def display(self):
        if self.selected_image and not self.live:
            self.img = cv2.imread(self.image_name)
        else:
            self.img = self.cam.get_image()
            self._img = cv2.cvtColor(self.img,cv2.COLOR_BGR2RGB)

        self.refresh(self._img)

=======
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
>>>>>>> master

    def configure(self):
        pass

<<<<<<< HEAD

    def setLed(self):
        pass
    # import odroid_wiringpi as wpi
    # import time
    # wpi.wiringPiSetup()
    # wpi.pinMode(0, 1)
    # wpi.digitalWrite(0, 1)
    # time.sleep(1)
    # wpi.digitalWrite(0, 0)
    # time.sleep(1)
=======
    def setLed(self):
        pass
>>>>>>> master


if __name__ == "__main__":
    app = QApplication(sys.argv)
<<<<<<< HEAD
    w = Win()
=======
    w = MainWindow()
>>>>>>> master
    w.show()
    sys.exit(app.exec())