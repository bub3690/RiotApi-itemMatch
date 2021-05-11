#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
import pandas
import numpy

class  RiotApi:
    """
    AUTHOR:이종법
    DATE:2021-03-19
    PURPOSE: 라이엇API에서, MATCH-V4 , LEAGUE-EXP-V4 , SUMMONER-V4, 를 불러오는 CLASS
    간단히 말하면, 이 class에서만 requests를 사용한다.
    
    앞으로 이 클래스는 RIOT API를 불러오기만 하고,
    파싱 클래스는 opponentsParser 이용
    
    """
    url='https://kr.api.riotgames.com'
    url_summoner_v4 = '/lol/summoner/v4/summoners/by-name/' # + summonername
    url_league_exp_v4='/lol/league-exp/v4/entries/RANKED_SOLO_5x5/GRANDMASTER/I?page='
    #league_exp_v4는 ?page=페이지수&api_key={} 로 요청해야한다.
    #단, 그랜드마스터 한정
    url_match_v4_accountid = '/lol/match/v4/matchlists/by-account/' # + account_id?api_key=
    url_match_v4_matchid = '/lol/match/v4/matches/' # + match_id?api_key=
    url_match_v4_timeline_matchid='/lol/match/v4/timelines/by-match/' # + match_id?api_key=
    query='?api_key='
    query2='&api_key='
    query_queue="?queue=420"
    #timeline url
    
    
    
    
    def __init__(self,apikey,):
        self._apikey=apikey
        print("RiotApi init")
    
    def get_summoner(self,summoner_name):
        #return account_id
        #소환사 이름만 입력해주면 작동한다.
        summoner_data=requests.get(RiotApi.url+
                            RiotApi.url_summoner_v4+
                            summoner_name+
                            RiotApi.query+self._apikey).json()
        print(summoner_data)
        return summoner_data["accountId"]
    

    def get_summoner_raw(self,summoner_name):
            #return account_id
        #소환사 이름만 입력해주면 작동한다.
        summoner_data=requests.get(RiotApi.url+
                        RiotApi.url_summoner_v4+
                        summoner_name+
                        RiotApi.query+self._apikey).json()
        return summoner_data
    
    
    def get_league(self,page):
        page = str(page)
        #페이지만 입력해주면 작동한다.
        return requests.get(RiotApi.url+
                            RiotApi.url_league_exp_v4+
                            page+
                            RiotApi.query2+self._apikey).json()
    
    def get_gameid_byAccountid(self,account_id):
        #return [game_id]
        #game_id는 굉장히 많기때문에 리스트로 출력된다.
        
        #account_id를 받아서, 게임아이디를 출력하기 위해서 사용.
        #match_v4 중 account_id를 받는것 사용.
        
        ## 추가. 05.11. queryparameter를 추가하여, queue가 420 (rank 5vs5 만 가져온다.)
        ## 추가. 05.11. match중 lane="NONE"은 다시하기 게임이라서 제외함.
        
        account_id=str(account_id)

        print(RiotApi.url+RiotApi.url_match_v4_accountid
                            +account_id
                            +self.query_queue
                            +RiotApi.query2
                            +self._apikey)
        
        game_data=requests.get(RiotApi.url+
                            RiotApi.url_match_v4_accountid
                            +account_id
                            +self.query_queue
                            +RiotApi.query2
                            +self._apikey).json()
        print(game_data)
        matches=[]
        for match in game_data["matches"]:
            if match["lane"]!="NONE" :
                matches.append(match['gameId'])
        return matches
    
    def get_timeline_byMatchid(self,match_id):
        return requests.get(RiotApi.url+
                            RiotApi.url_match_v4_timeline_matchid+
                            match_id+
                            RiotApi.query+
                            self._apikey).json()

if __name__ == '__main__':
    #단위테스트
    test = RiotApi(apikey="RGAPI-f7922aa7-1787-4f61-be99-432393122bc2")
    print(test.get_league(1))
    #user_accountId=test.get_summoner('종버버버')
    user_accountId='anXYP4yARxqIKeKuBd6F9FFDVQhPs-wr7uTZ4IE6NJp4'
    games_ids=test.get_gameid_byAccountid(user_accountId)
    #test_gameId=games_ids[0] # 게임아이디 하나 받아서, timeline 테스트에 사용
    #test_timeline=test.get_timeline_byMatchid(str(test_gameId))
    
    
    
    #print(test.get_league('1').json())
    
    #games_data
    
#games_ids
#print(len(games_ids))
#test_timeline
#games_ids

