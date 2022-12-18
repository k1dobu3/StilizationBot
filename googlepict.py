import requests
from bs4 import BeautifulSoup
import random

def get_googlepicturl(item_name):
    s = requests.session()
    s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'})

    r = s.get(f'https://www.google.ru/search?q={item_name}&tbm=isch')

    soup = BeautifulSoup(r.text, "html.parser")

    images = soup.findAll(attrs={'class': 'rg_i Q4LuWd'})

    card = random.choice(images)
    #print(card)

    #print(card.get('data-src'))
    return card.get('data-src')