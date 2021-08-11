import cassiopeia as cass
import requests
import pandas
import numpy
import pymysql
version='11.16.1'
url='https://ddragon.leagueoflegends.com/cdn/'+version+'/data/ko_KR/runesReforged.json'
img_url='https://ddragon.leagueoflegends.com/cdn/img/'
rune_data=requests.get(url).json()

class RuneInfo():
    def __init__(self):
        self.runes=[]

    def insert_runes(self, _rune):
        self.runes.append(_rune)

    def get_runes(self):
        return self.runes

runeInfo=RuneInfo()

for i in rune_data:
    rune_category=i["name"]
    rune_slots=i["slots"]
    
    for m in rune_slots:
        rune=m["runes"]
        for n in rune:
            A_rune = {}
            A_rune["category"]=rune_category
            A_rune["eng_category"]=i["key"]
            A_rune["id"]=n["id"]
            A_rune["runeEngName"]=n["key"]
            A_rune["runeKorName"]=n["name"]
            A_rune["description"]=n["shortDesc"]
            A_rune["rune_url"]=img_url+n["icon"]
            runeInfo.insert_runes(A_rune)  
            print(A_rune)
    
#로컬 데이터베이스에 룬정보 삽입
if __name__=="__main__":
    myDB=pymysql.connect(
        user='root',
        password='rlathfals12#',
        host='127.0.0.1',
        db='project',
        charset='utf8'
    )
    cursor=myDB.cursor(pymysql.cursors.DictCursor)

    for i in runeInfo.get_runes(): 
        sql = "insert into rune_info values(%s,%s, %s, %s, %s, %s, %s);"
        data=(i["id"], i["category"],i["eng_category"], i["runeKorName"], i["runeEngName"],i["description"], i["rune_url"])
        cursor.execute(sql, data)
    myDB.commit()