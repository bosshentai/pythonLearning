# convert JPG to PNG
import sys 
import os 
from PIL import Image

# grab first and second argument
imageFolder = sys.argv[1]
outputFolder = sys.argv[2]


# check is new/ exist, if not created 
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

#print(imagemFolder,outputFolder)



# loop through Pokedex 
for filename in os.listdir(imageFolder):
    img = Image.open(f'{imageFolder}{filename}')
    cleanName = os.path.splitext(filename)[0]
    #print(cleanName)
    img.save(f'{outputFolder}{cleanName}.png', 'png')
    # print('all done!')

# conert images to png 
# save to the new folder 