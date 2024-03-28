import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image) #存储着打开的图片
    
images[0].save(
    "costumes.gif",save_all=True, append_image=[images[1]], duration=200, loop=0
)