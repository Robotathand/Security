from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
from time import sleep

pir = MotionSensor(4)
camera = PiCamera()

while True:
    pir.wait_for_motion()
#    print("Motion!")
    filename = "../footage/motion/securityFootageFrom{0:%c}.h264".format(datetime.now())
    camera.start_recording(filename)
    pir.wait_for_no_motion()
    sleep(5)
    camera.stop_recording()
#    print("Done!")
