import pypylon.pylon as py
import matplotlib.pyplot as plt
import cv2

icam = py.InstantCamera(py.TlFactory.GetInstance().CreateFirstDevice())
icam.Open()
icam.MaxNumBuffer = 5
icam.ExposureTime = 500000
#icam.UserSetSelector = "UserSet1"
#icam.UserSetLoad.Execute()
icam.PixelFormat = "RGB8"
while True:
    img = icam.GrabOne(600)
    img = img.Array
    cv2.waitKey(10)
    cv2.imshow("result",img)
    cv2.imwrite("shot.png",img)
    # plt.imshow(cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    # plt.show()

from datetime import datetime

str_time = datetime.now().strftime("%y%m%d_%H%M%S")
print(str_time)