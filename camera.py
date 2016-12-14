from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

# Set up the camera
# camera.annotate_text = "Light Pollution Level"
# camera.brightness = 50 # default
# camera.annotate_text_size = 32 # default
# camera.awb_mode = "auto" # auto white balance
camera.exposure_mode = 'night'
# Exposure settings:
# Off, auto, night, nightpreview, backlight, spotlight, sports, snow, beach,
# verylong, fixedfps, antishake, and fireworks.
# The default is auto

def main(camera):
    preview_image(camera)
    capture_photo(1)
    return

def preview_image(camera):
# Code that shows camera preview for 10 sec
    camera.start_preview()
    sleep(10)
    camera.stop_preview()

# Take a photo
def capture_photo(i):
    camera.resolution = (2592, 1944)
    sleep(5)
    path = "/home/pi/Desktop/img%s.jpg" % i
    camera.capture(path)
    return path

main(camera)
