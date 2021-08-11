import cassiopeia as cass
import requests
import pandas
import numpy
import pymysql
version='11.16.1'
url='https://ddragon.leagueoflegends.com/cdn/'+version+'/data/ko_KR/championFull.json'
champ_img_url='https://ddragon.leagueoflegends.com/cdn/'+version+'/img/champion/'
skill_img_url='https://ddragon.leagueoflegends.com/cdn/'+version+'/img/spell/'
champions_data=requests.get(url).json()

class Champion():
    """
        THIS CLASS is for storing each champion information
    """
    def __init__(self,_champNameEng,_champNameKor, _id, _skill_info, _champ_url):
        self.champNameEng=_champNameEng
        self.champNameKor=_champNameKor
        self.id=_id
        self.skill_info=_skill_info
        self.champ_url=_champ_url

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
    count=4 #skill id를 위한 카운트
    for iterable2 in iterable["spells"]:
        # print(iterable2["id"], iterable2["name"], iterable2["description"],end=" ")
        skill={}
        if count==4:
            skill["id"]=i+'Q'
        elif count==3:
            skill["id"]=i+'W'
        elif count==2:
            skill["id"]=i+'E'
        elif count==1:
            skill["id"]=i+'R'
        count=count-1
        skill["name"]=iterable2["name"]
        skill["description"]=iterable2["description"]
        skill["skill_url"]=skill_img_url+iterable2["id"]+'.png'
        skills.append(skill)
    skill={}
    skill["id"]=i+'Passive'
    skill["name"]=iterable["passive"]["name"]
    skill["description"]=iterable["passive"]["description"]
    skill["skill_url"]=skill_img_url+i+'.png'
    skills.append(skill)
    champ_url=champ_img_url+iterable["id"]+'.png'
    champion1=Champion(iterable["id"], iterable["name"], iterable["key"], skills, champ_url)
    championInfo.insert_champion(champion1)
print()

# 데이터베이스에 챔피언 정보 삽입, pymysql 패키지 사용
if __name__ == '__main__':
    #로컬 데이터베이스 추가, 변경 사항
    myDB=pymysql.connect(
        user='root',
        password='rlathfals12#',
        host='127.0.0.1',
        db='project',
        charset='utf8'
    )
    ################################
    cursor=myDB.cursor(pymysql.cursors.DictCursor)
    for i in championInfo.get_info(): #챔피언 정보 테이블 삽입
        sql = "insert into champ_info values(%s, %s, %s, %s);"
        # 챔피언 아이콘 이미지 url 삽입 추가
        data=(i.id, i.champNameKor, i.champNameEng, champ_img_url+i.champ_url)
        cursor.execute(sql, data)
        count=5
        for m in i.skill_info: #각 챔피언별 스킬 정보 테이블 삽입
            
            count=count-1
            sql = "insert into skill_info values(%s, %s, %s, %s, %s);"
            data=(i.id, m["id"], m["name"], m["description"], m["skill_url"])
            cursor.execute(sql, data)
    myDB.commit()   
    