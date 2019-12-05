import requests # imported requests
import docx # imported python-docs
from PIL import Image, ImageDraw, ImageFont  # imported these libraries to be able wo work on the image
# installed and imported the pillow library


# Working on the image down here
image = Image.open('tacorecipe.jpg') # the pic that I am gonna use (Taco image)
image.thumbnail((800, 800)) # Because the image is big, I resized it to 800/800
iimage = ImageDraw.Draw(image) # I've used the Imagedraw library to be able to put text on the image
font = ImageFont.truetype('DejaVuSans.ttf', 25) # using a database for the fonts
iimage.text([10, 475], 'Random Taco Cookbook', fill='black', font=font) # drawing text on the image
image.show() # shows the new edited version of the image

taco3 = [] # a list to stole the dictionaries in

for i in range(3): # I've used a for loop here so I can get the result from url 3 times (the dictionaries)
    taco_recipe_urldata = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()  # using the requests library to open the url link and get the dictionary that we are gonna use
    taco3.append(taco_recipe_urldata) # adds the results to the list created earlier
print(taco3)
