import requests
import pandas as pd
import pymysql
import os
from sqlalchemy import create_engine

pymysql.install_as_MySQLdb()
root=os.path.dirname(os.path.realpath(__file__))
version='11.16.1'
url='http://ddragon.leagueoflegends.com/cdn/'+version+'/data/ko_KR/item.json'
img_url='https://ddragon.leagueoflegends.com/cdn/'+version+'/img/item/'
item_data=requests.get(url).json()["data"]

class ItemInfo():
    def __init__(self):
        self.items=[]

    def insert_items(self, _item):
        self.items.append(_item)

    def get_items(self):
        return self.items

itemInfo=ItemInfo()

for i in item_data:
    A_item={}
    A_item["id"]=i #id
    A_item["kor_name"]=item_data[i]["name"]#kor
    A_item["item_url"]=img_url+A_item["id"]+'.png'
    A_name=A_item["kor_name"]
    
    value=item_data[i].get("depth")
    #다음 경우는 예외로 최종 아이템 카테고리로 적용
    if A_name in ('메자이의 영혼약탈자', '대천사의 지팡이','마나무네','무라마나','대천사의 포옹','무한의 대검', '라바돈의 죽음모자'):
        A_item["category"]='최종 아이템'
    #최종 아이템
    elif value== 3: 
        A_item["category"]='최종 아이템'
    #신발
    elif 'Boots' in item_data[i]["tags"]:
        A_item["category"]='신발'
    #소비 아이템
    elif 'Consumable' in item_data[i]["tags"]:
        A_item["category"]='소비 아이템'
    elif A_name in ('굳건한 의지의 완전한 비스킷','미니언 해체분석기'):
        A_item["category"]='소비 아이템'
    #장신구
    elif 'Trinket' in item_data[i]["tags"]:
        A_item["category"]='장신구'
    else:
        A_item["category"]=''

    A_item["description"]=item_data[i]["description"]
    itemInfo.insert_items(A_item)

if __name__=="__main__":    
    id_pw=pd.read_csv(root+'/resource/password.csv')
    mysql_id=id_pw["id"][0]
    mysql_pw=id_pw["pw"][0]
    myDB=pymysql.connect(
        user=mysql_id,
        password=mysql_pw,
        host='54.180.119.182',
        db='test',
        charset='utf8',
        port=50912
    )
    cursor=myDB.cursor(pymysql.cursors.DictCursor)
    for i in itemInfo.get_items(): 
        sql = "insert into item_info values(%s, %s, %s, %s,%s);"
        data=(i["id"], i["kor_name"], i["category"],i["description"],i["item_url"])
        cursor.execute(sql, data)
    myDB.commit()