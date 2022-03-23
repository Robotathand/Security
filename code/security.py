# not yet done
from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
from time import sleep
from gpiozero import Button

pir = MotionSensor(4)
camera = PiCamera()
button = Button(27)

while True:
# to be continued
