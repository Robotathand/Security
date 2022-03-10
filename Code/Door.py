from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from time import sleep

camera = PiCamera()
button = Button(27)

while True:
    button.wait_for_release()
#    print("Door!")
    filename = "../Footage/Door/SecurityFootageFrom{0:%c}.h264".format(datetime.now())
    camera.start_recording(filename)
    sleep(300)
    camera.stop_recording()
#    print("Done!")
