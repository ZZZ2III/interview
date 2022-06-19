import requests
from PIL import Image,ImageDraw
import sys
from PIL.Image import Resampling


def download_im(urls:list):
        counter = 0
        for i in urls:
            counter += 1
            req = requests.get(i)
            with open(f"{counter}.jpg",'wb') as f:
                f.write(req.content)
def making_overlay(base_im:str,overlay_im:str):
    im1 = Image.open(base_im)
    im2 = Image.open(overlay_im)
    im1.paste(im2, (-70,170))
    im1.save('result_im.png')
    im1.close()
    im2.close()

urls_list = ['http://alitair.1gb.ru/test_prog_plashki/106044_benefit.jpg','http://alitair.1gb.ru/test_prog_plashki/benefit.png']
download_im(urls_list)
image = Image.open('1.jpg')
width, height = image.size
new_height = 580
new_width = int(new_height * width / height)

tatras = image.resize((new_width, new_height), Resampling.LANCZOS)
tatras.save('new_pic.jpg', quality=95)
making_overlay('2.jpg', 'new_pic.jpg')