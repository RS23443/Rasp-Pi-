from picamera import PiCamera
from time import sleep
from libcamera import LibCamera

camera.start_preview()
sleep(5)
camera.stop_preview()

camera = PiCamera()
camera.resolution (1080,1080)
camera.start_preview()
#preview: open stream 
sleep (2)
camera.capture('jpeg.png')

