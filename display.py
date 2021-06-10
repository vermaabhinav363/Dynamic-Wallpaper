import ctypes
import time
from threading import Event
import cv2
SPI_SETDESKTOPWALLPAPER=20
frame_count = 0

def ExtractImages(path):
        # Path to video file --- capture_image is the object which calls read
        capture_image = cv2.VideoCapture(path)
        # keeping a count for each frame captured
        frame_count = 0

        while (True):

            # Reading each frame
            con, frames = capture_image.read()

            # con will test until last frame is extracted
            if con:
                # giving names to each frame and printing while extracting
                name = str(frame_count) + '.jpg'
                print('Capturing --- ' + name)

                # Extracting images and saving with name
                cv2.imwrite(name, frames)
                frame_count = frame_count + 1
            else:
                break

run_first_time=2
if run_first_time == 1:
    path = "C:\\Users\\verma\\OneDrive\\Desktop\\Codes\\Python\\VID2.mp4"

    ExtractImages(path)

run_first_time=0
i=1
while 1:
    i=1
    while i<974:

        ctypes.windll.user32.SystemParametersInfoW(20,0,"C:\\Users\\verma\\OneDrive\\Desktop\\Codes\\Python\\" +str(i)+".jpg" ,0)
        time.sleep(0.022)
        Event().wait(0.002)
        i=i+1
        
