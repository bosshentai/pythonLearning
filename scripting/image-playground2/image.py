from PIL import Image


img = Image.open('./image/astro.jpg')

#newImg = img.resize((400,400))
img.thumbnail((400,400))
img.save('imgchanged/thumbnail.jpg')

print(img.size)
