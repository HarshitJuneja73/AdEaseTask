import requests
from bs4 import BeautifulSoup
import os

url1 = 'https://www.airbnb.co.uk/s/Ljubljana--Slovenia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&query=Ljubljana%2C%20Slovenia&place_id=ChIJ0YaYlvUxZUcRIOw_ghz4AAQ&checkin=2020-11-01&checkout=2020-11-08&source=structured_search_input_header&search_type=autocomplete_click'
url2 = 'https://parade.com'
url3 = "https://www.geeksforgeeks.org/how-to-download-all-images-from-a-web-page-in-python/"


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


imagedown(url3, 'scrapes')
print('Hey')
