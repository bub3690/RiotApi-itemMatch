import cassiopeia as cass
import requests
import numpy
import pymysql
import pandas as pd
import numpy
import pymysql
import os,sys
from sqlalchemy import create_engine

pymysql.install_as_MySQLdb()

root=os.path.dirname(os.path.realpath(__file__))

version='11.16.1'
url='https://ddragon.leagueoflegends.com/cdn/'+version+'/data/ko_KR/summoner.json'
img_url='https://ddragon.leagueoflegends.com/cdn/'+version+'/img/spell/'
spell_data=requests.get(url).json()

class SpellInfo():
    def __init__(self):
        self.spells=[]

    def insert_spells(self, _spell):
        self.spells.append(_spell)

    def get_spells(self):
        return self.spells

spellInfo=SpellInfo()

for i in spell_data["data"]:
    iterable=spell_data["data"]
    A_spell={}
    A_spell["id"]=iterable[i]["key"]
    A_spell["kor_name"]=iterable[i]["name"]
    A_spell["eng_name"]=iterable[i]["id"]
    A_spell["description"]=iterable[i]["description"]
    A_spell["spell_url"]=img_url+iterable[i]["image"]["full"]
    spellInfo.insert_spells(A_spell)

    
#로컬 데이터베이스에 스펠정보 삽입
if __name__=="__main__":
    myDB=pymysql.connect(
        user='root',
        password='1q2w3e4r',
        host='54.180.119.182',
        db='test',
        charset='utf8',
        port=50912
    )
    cursor=myDB.cursor(pymysql.cursors.DictCursor)

    for i in spellInfo.get_spells(): 
        sql = "insert into spell_info values(%s, %s, %s, %s,%s);"
        data=(i["id"], i["kor_name"], i["eng_name"], i["description"],i["spell_url"])
        cursor.execute(sql, data)
    myDB.commit()