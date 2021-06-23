import requests
import pandas
import numpy
url='http://ddragon.leagueoflegends.com/cdn/11.13.1/data/ko_KR/item.json'
item_data=requests.get(url).json()

