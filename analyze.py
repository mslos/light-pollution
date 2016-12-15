from PIL import Image
from PIL import ImageFilter
from PIL import ImageStat
from time import sleep
from PIL import ImageFont
from PIL import ImageDraw
import sys
import os

## Configure for raspi or mac
comp = "raspi"
frames = [im]
fnt = ImageFont.truetype(font, 72)

if comp == "mac":
    font = "/Library/Fonts/Comic Sans MS.ttf"
    path = "/Users/***/Desktop/projects/light-pollution/"
    fl = "img_0101.jpg"
elif comp == 'raspi':
    font = "./DroidSansMono.ttf"
    path = "/home/pi/Desktop/"
    fl = "img1.jpg"
    from picamera import PiCamera, Color
    from time import sleep
    camera = PiCamera()


## Capture photo in the given path
def capture_photo_2(path):
    camera.resolution = (2592, 1944)
    # camera.resolution = (500,500)
    sleep(5)
    camera.capture(path)
    return path

## Sourcing image
capture_photo_2(path+fl)
im = Image.open(path+fl)

## Filter out light pollution for each image and calculate quotient
gray = im.convert('L')
for i in range(30,240,50):
    bw = gray.point(lambda x: 0 if x<i else 255, '1')
    stat = ImageStat.Stat(bw)
    img = bw.convert("RGB")
    draw = ImageDraw.Draw(img)
    draw.text((50, 50), "Min/Max values: "+str(stat.extrema), (0, 255, 0), font=fnt)
    draw.text((50, 130), "Average color (pollution): "+str(stat.mean), (0, 255, 0), font=fnt)
    # img.show()
    # sleep(1)
    frames.append(img)


## Prepare the image mixing
images = frames
widths, heights = zip(*(i.size for i in images))
total_width = sum(widths)/2
max_height = max(heights)*2

new_im = Image.new('RGB', (total_width, max_height))


## Place filtered images into a single image
x_offset = 0
for im in images[0:3]:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

x_offset = 0
for im in images[3:7]:
    new_im.paste(im,(x_offset,im.size[1]))
    x_offset += im.size[0]

## Saaaave!
new_im.save(path+'test2.jpg')
os.system("xdg-open "+path+'test2.jpg')
new_im.show()

# im.save(path+"test", "JPEG")
