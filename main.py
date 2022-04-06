import requests
from bs4 import BeautifulSoup
import os
import cv2
import pytesseract
from textDet import detector
from cta import ctab
url1 = "https://www.geeksforgeeks.org"


def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        name = image['src']
        link = image['src']
        # if "ad" in name:
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing: ', name)


imagedown(url1, 'scrapes')
detector("scrapes")
ctab()

