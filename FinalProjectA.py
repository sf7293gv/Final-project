import requests # imported requests
import docx # imported python-docs
from PIL import Image, ImageDraw, ImageFont  # imported these libraries to be able wo work on the image
# installed and imported the pillow library

taco_recipe_urldata = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true')
     #  using the requests library to open the url link and get the dictionary that we are gonna use

