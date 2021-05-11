#RGAPI-a822c8e4-49e9-4cf2-8789-595846e13ab9
#RGAPI-a822c8e4-49e9-4cf2-8789-595846e13ab9
from opponentsLOL import RiotApi
import os, sys


riotApi1=RiotApi('RGAPI-2c57b69e-3636-433d-bbd5-bdb5a3bdd474') #내 riotapi key 넣기

#403 error : riot api 오류
total_summoner = []

for page in range(1,2000): # summoner 정보 2000페이지까지 돌리기
    summoner_data = riotApi1.get_league(str(page)) # summoner_data에 페이지별 json데이터 가져오기
    print(page)
    if len(summoner_data) == 0: # json파일이 더이상 넘어오지 않을 경우 for문 종료
        print('stop')
        break
    
    for items in summoner_data:
        total_summoner.append(items["summonerName"]+'\n') # 공백으로 구분해서 받음

with open(os.path.join(sys.path[0],'./resource/getSummonerName.txt'),'w',encoding='utf8') as f:
    f.writelines(total_summoner)

