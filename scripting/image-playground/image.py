from PIL import Image, ImageFilter

# Pillow library 


img = Image.open('./Pokedex/pikachu.jpg')

#filteredImg = img.filter(ImageFilter.SMOOTH)
filteredImg = img.convert('L')
crooked = filteredImg.rotate(180)

crooked.save('./changed/grey1.png','png')
filteredImg.save('./changed/grey.png', 'png')

resize = filteredImg.resize((300,300))
resize.save('./changed/resize.png', 'png')


box = (100,100,400,400)
region = filteredImg.crop(box)
region.save('./changed/region.png','png')

#filteredImg.show()
#print(img.format)
#print(img.size)
#print(img.mode)