import cv2
import numpy
import pyautogui
import datetime
import time

four = cv2.VideoWriter_fourcc(*'XVID')
screen_size = (2048,1152)
string = str(datetime.date.today())+'  '+time.strftime("%I-%M-%S %p")
out = cv2.VideoWriter(f"E:\\screenshots\\{string}.avi",four,20.0,(screen_size))

while True:
    img = pyautogui.screenshot()
    frame = numpy.array(img)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)
    if cv2.waitKey(1) and 0xFF=='q':
        break



