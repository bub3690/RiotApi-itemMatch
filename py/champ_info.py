import cassiopeia as cass
import requests
import pandas
import numpy
url='https://ddragon.leagueoflegends.com/cdn/11.13.1/data/ko_KR/championFull.json'
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
    passive_skill={}
    passive_skill["id"]=iterable["id"]+'_'+'passive'
    passive_skill["name"]=iterable["passive"]["name"]
    passive_skill["description"]=iterable["passive"]["description"]
    #https://developer.riotgames.com/docs/lol#data-dragon_other 태그내용 추출 가능
    skills.append(passive_skill)
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
print(championInfo.print_champinfo('아트록스'))
# championInfo.print_champinfo('제이스')


# print(championInfo.champion[0].skill_info[0]["description"])

# cass.set_riot_api_key("RGAPI-61907ad8-2ccc-4750-97f9-0565eea7ffd5")  # This overrides the value set in your configuration/settings.
# cass.set_default_region("KR")

# champions=cass.get_champions()
# print(cass.core.staticdata.champion.Champion)

# with open(os.path.join(sys.path[0],'./resource/championInfo.txt'),'w',encoding='utf8') as f:
#     f.writelines(str(champions))

# challenger_league = cass.get_challenger_league(queue=cass.Queue.ranked_solo_fives)
# for i in challenger_league:
#     for m in i:
#         print(m)