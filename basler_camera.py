from pypylon import pylon
import cv2
from pypylon_opencv_viewer import BaslerOpenCVViewer
class Basler:
    VIEWER_CONFIG_RGB_MATRIX = {
        "features": [
            {
                "name": "Gain",
                "type": "int",
                "step": 1,
            },
            {
                "name": "Height",
                "type": "int",
                "value": 1080,
                "unit": "px",
                "step": 2,
            },
            {
                "name": "Width",
                "type": "int",
                "value": 1920,
                "unit": "px",
                "step": 2,
            },
            {
                "name": "CenterX",
                "type": "bool",
            },
            {
                "name": "CenterY",
                "type": "bool",

            },
            {
                "name": "OffsetX",
                "type": "int",
                "dependency": {"CenterX": False},
                "unit": "px",
                "step": 2,
            },
            {
                "name": "OffsetY",
                "type": "int",
                "dependency": {"CenterY": False},
                "unit": "px",
                "step": 2,
            },
            {
                "name": "ExposureTime",
                "type": "int",
                "value": 500000,
                "unit": "us",
                "step": 1,
            },
            {
                "name": "ExposureAuto",
                "type": "choice_text",
                "options": ["Off", "Once", "Continuous"],
                "style": {"button_width": "90px"}
            },

            {
                "name": "BalanceWhiteAuto",
                "type": "choice_text",
                "options": ["Off", "Once", "Continuous"],
                "style": {"button_width": "90px"}
            },
        ],

        "default_user_set": "UserSet1",
    }

    def __init__(self):
        # Pypylon get camera by serial number
        self.serial_number = '22925543'
        self.info = None
        self.camera = None
        self.config = self.VIEWER_CONFIG_RGB_MATRIX

        for i in pylon.TlFactory.GetInstance().EnumerateDevices():
            if i.GetSerialNumber() == self.serial_number:
                self.info = i
                print("{} found!".format(self.serial_number))
                break
        else:
            print('Camera with {} serial number not found'.format(self.serial_number))

        # VERY IMPORTANT STEP! To use Basler PyPylon OpenCV viewer you have to call .Open() method on you camera
        if self.info is not None:
            self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateDevice(self.info))
            self.camera.Open()
        self.viewer = BaslerOpenCVViewer(self.camera)


    def load_configure(self,path):
        self.config = self.VIEWER_CONFIG_RGB_MATRIX

    def set_configure(self):
        self.load_configure("cam.xml")
        self.viewer.set_configuration(self.config)

    def save_image(self,path="img.png"):
        self.viewer.save_image(path)

    def get_image(self):
        return self.viewer.get_image()


if __name__ == "__main__":
    cam = Basler()

    while False:
        img = cam.get_image()
        cv2.waitKey(10)
        cv2.imshow("result",img)
    from datetime import  datetime
    str_time = datetime.now().strftime("%y%m%d_%H%M%S")
    import os
    image_name = str_time+ ".png"
    print(image_name)
    cam.save_image(image_name)
