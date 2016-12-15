from PIL import Image
from PIL import ImageFilter
from PIL import ImageStat
from time import sleep
from PIL import ImageFont
from PIL import ImageDraw

comp = "mac"

if comp == "mac":
    font = "/Library/Fonts/Comic Sans MS.ttf"
    path = "/Users/maslo/Desktop/projects/light-pollution/"
    file = "img_0101.jpg"
else:
    font = "./DroidSansMono.ttf"
    path = "/home/pi/Desktop/"
    file = "img1.jpg"

im = Image.open(path+file)
im.show()
frames = []
fnt = ImageFont.truetype(font, 72)

gray = im.convert('L')
for i in range(30,240,50):
    bw = gray.point(lambda x: 0 if x<i else 255, '1')
    stat = ImageStat.Stat(bw)
    img = bw.convert("RGB")
    draw = ImageDraw.Draw(img)
    draw.text((50, 50), "Min/Max values: "+str(stat.extrema), (0, 255, 0), font=fnt)
    draw.text((50, 130), "Average color (pollution): "+str(stat.mean), (0, 255, 0), font=fnt)
    img.show()
    sleep(1)
    frames.append(img)


im.save(path+"test", "JPEG")
