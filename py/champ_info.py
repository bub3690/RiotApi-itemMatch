import cassiopeia as cass
import requests
import pandas
import numpy
import pymysql
url='https://ddragon.leagueoflegends.com/cdn/11.15.1/data/ko_KR/championFull.json'
champions_data=requests.get(url).json()

class Champion():
    """
        THIS CLASS is for storing each champion information
    """
    def __init__(self,_champNameEng,_champNameKor, _id, _skill_info):
        self.champNameEng=_champNameEng
        self.champNameKor=_champNameKor
        self.id=_id
        self.skill_info=_skill_info

class ChampionInfo():

    def __init__(self):
        self.champion=[]
    
    def insert_champion(self, _champion):
        self.champion.append(_champion)

    def print_info(self):
        for i in self.champion:
            print(i.champNameEng)
            print(i.champNameKor)
            print(i.id)
            print(i.skill_info)
    
    def get_info(self):
        return self.champion


    def print_champinfo(self, chname):
        for i in self.champion:
            if i.champNameKor==chname:
                print(i.champNameEng)
                print(i.champNameKor)
                print(i.id)
                print(i.skill_info)

championInfo = ChampionInfo()

for i in champions_data["data"]:
    iterable=champions_data["data"][i]
    # print(iterable["id"],iterable["key"],end=" ")
    skills=[]
    #passive_skill={}
    #passive_skill["id"]=iterable["id"]+'_'+'passive'
    #passive_skill["name"]=iterable["passive"]["name"]
    #passive_skill["description"]=iterable["passive"]["description"]
    #https://developer.riotgames.com/docs/lol#data-dragon_other 태그내용 추출 가능
    #skills.append(passive_skill)
    for iterable2 in iterable["spells"]:
        # print(iterable2["id"], iterable2["name"], iterable2["description"],end=" ")
        skill={}
        skill["id"]=iterable2["id"]
        skill["name"]=iterable2["name"]
        skill["description"]=iterable2["description"]
        skills.append(skill)
    champion1=Champion(iterable["id"], iterable["name"], iterable["key"], skills)
    championInfo.insert_champion(champion1)
print()

# 데이터베이스에 챔피언 정보 삽입
if __name__ == '__main__':
    myDB=pymysql.connect(
        user='root',
        password='rlathfals12#',
        host='127.0.0.1',
        db='project',
        charset='utf8'
    )
    cursor=myDB.cursor(pymysql.cursors.DictCursor)
    for i in championInfo.get_info(): #챔피언 정보 테이블 삽입
        # sql = "insert into champ_info values(%s, %s, %s);"
        # data=(i.id, i.champNameKor, i.champNameEng)
        # cursor.execute(sql, data)
        count=4
        for m in i.skill_info: #각 챔피언별 스킬 정보 테이블 삽입
            skill_id=''
            #count별로 스킬id 이름 재구성(Q,W,E,R순)
            if count==4:
                skill_id=i.champNameEng+'Q'
            elif count==3:
                skill_id=i.champNameEng+'W'
            elif count==2:
                skill_id=i.champNameEng+'E'
            elif count==1:
                skill_id=i.champNameEng+'R'
            count=count-1
            sql = "insert into skill_info values(%s, %s, %s, %s);"
            data=(i.id, skill_id, m["name"], m["description"])
            cursor.execute(sql, data)
    myDB.commit()
    