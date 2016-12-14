from PIL import Image
from PIL import ImageFilter
from PIL import ImageStat
from time import sleep
from PIL import ImageFont
from PIL import ImageDraw


im = Image.open("/Users/maslo/Desktop/img_0101.jpg")
im.show()

fnt = ImageFont.truetype("/Library/Fonts/Comic Sans MS.ttf", 72)
frames = []
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

 # write GIF animatio
# fp = open("~/Desktop/out.gif", "wb")
# gifmaker.makedelta(fp, frames)
# fp.close()

# bw = im.convert('RGB')
# im1 = bw.filter(ImageFilter.FIND_EDGES)
# im1.show
#
# draw = ImageDraw.Draw(img)
#
# img.show()
