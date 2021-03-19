#!/usr/bin/env python
# coding: utf-8

# In[15]:


import requests
import pandas
import numpy

class  RiotApi:
    """
    AUTHOR:이종법
    DATE:2021-03-19
    PURPOSE: 라이엇API에서, MATCH-V4 , LEAGUE-EXP-V4 , SUMMONER-V4 를 불러오는 CLASS

    """
    url='https://kr.api.riotgames.com'
    url_summoner_v4 = '/lol/summoner/v4/summoners/by-name/' # + summonername
    url_league_exp_v4='/lol/league-exp/v4/entries/RANKED_SOLO_5x5/GRANDMASTER/I?page='
    #league_exp_v4는 ?page=페이지수&api_key={} 로 요청해야한다.
    #단, 그랜드마스터 한정
    url_match_v4_accountid = '/lol/match/v4/matchlists/by-account/' # + account_id?api_key=
    url_match_v4_matchid = '/lol/match/v4/matches/' # + match_id?api_key=
    query='?api_key='
    query2='&api_key='
    
    def __init__(self,apikey,):
        self._apikey=apikey
        print("RiotApi init")
    
    def get_summoner(self,summoner_name):
        #소환사 이름만 입력해주면 작동한다.
        return requests.get(RiotApi.url+
                            RiotApi.url_summoner_v4+
                            summoner_name+
                            RiotApi.query+self._apikey)
    
    def get_league(self,page):
        #페이지만 입력해주면 작동한다.
        return requests.get(RiotApi.url+
                            RiotApi.url_league_exp_v4+
                            page+
                            RiotApi.query2+self._apikey)
    
    def get_gameid(self,account_id):
        #account_id를 받아서, 게임아이디를 출력하기 위해서 사용.
        #match_v4 중 account_id를 받는것 사용.
        
        return requests.get(RiotApi.url+
                            RiotApi.url_match_v4_accountid+
                            RiotApi.account+
                            RiotApi.query1+self._apikey)
    

if __name__ == '__main__':
    #단위테스트
    test = RiotApi(apikey="")
    print(test.get_summoner('종버버버').text)
    summoner_name
    
    

