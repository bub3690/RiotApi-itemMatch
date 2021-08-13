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
    url_v5='https://asia.api.riotgames.com/lol/match/v5/matches/' #match_v5와 timeline에 사용
    url_summoner_v4 = '/lol/summoner/v4/summoners/by-name/' # + summonername
    url_league_exp_v4='/lol/league-exp/v4/entries/RANKED_SOLO_5x5/GRANDMASTER/I?page='
    #league_exp_v4는 ?page=페이지수&api_key={} 로 요청해야한다.
    #단, 그랜드마스터 한정
    url_match_v4_accountid = '/lol/match/v4/matchlists/by-account/' # + account_id?api_key=
    url_match_v4_matchid = '/lol/match/v4/matches/' # + match_id?api_key=
    url_match_v4_timeline_matchid='/lol/match/v4/timelines/by-match/' # + match_id?api_key=
    query='?api_key='
    query2='&api_key='
    query_queue="?queue=420"## 랭크 5vs5 게임만 출력위해서 get_gameid_byAccountid 함수에서 사용.
    #timeline url
    
    #timeline -> url_v5+'/KR_'+matchid+'/timeline'+query+api_key
    

    
    
    #puuid : /lol/match/v5/matches/by-puuid/{puuid}/ids
    #match_id: https://asia.api.riotgames.com/lol/match/v5/matches/KR_5173018625?api_key=RGAPI-c186a251-9936-4aa6-8ef3-3e742f274ac2
    #timeline: https://asia.api.riotgames.com/lol/match/v5/matches/KR_5173018625/timeline?api_key=RGAPI-c186a251-9936-4aa6-8ef3-3e742f274ac2

    
    
    def __init__(self,apikey,):
        self._apikey=apikey
        print("RiotApi init")
    
    def get_summoner(self,summoner_name):
        #return puuid
        #소환사 이름만 입력해주면 작동한다.
        ## 08.11 puuid 출력하는것으로 변경.
        summoner_data=requests.get(RiotApi.url+
                            RiotApi.url_summoner_v4+
                            summoner_name+
                            RiotApi.query+self._apikey).json()
        print(summoner_data)
        return summoner_data["puuid"]
    

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
    
    def get_gameid_byPuuid(self,puuid):
        #return [game_id]
        #game_id는 굉장히 많기때문에 리스트로 출력된다.
        
        #account_id를 받아서, 게임아이디를 출력하기 위해서 사용.
        #match_v4 중 account_id를 받는것 사용.
        
        ## 추가. 05.11. queryparameter를 추가하여, queue가 420 (rank 5vs5 만 가져온다.)
        ## 추가. 05.11. match중 lane="NONE"은 다시하기 게임이라서 제외함.
        ## 추가. 08.11. match_v5 패치로 get_gameid_byPuuid로 수정.
        
        #match_v5_by_puuid -> url_v5+'/by-puuid/'+puuid+'/ids'+ # puuid로 matchid 캐는것.
        '''
        print(RiotApi.url_v5+'by-puuid/'
                            +puuid
                            +'/ids'
                            +RiotApi.query_queue
                            +RiotApi.query2
                            +self._apikey)
        '''
        
        return requests.get(RiotApi.url_v5+'by-puuid/'
                            +puuid
                            +'/ids'
                            +RiotApi.query_queue
                            +RiotApi.query2
                            +self._apikey).json()
    
    def get_match_byMatchid(self,match_id):
        """
        0810. match_v5 반영
        match_v5_matchid -> url_v5+'KR_'+matchid+query+api_key
        print(RiotApi.url_v5+'KR_'+
                            match_id+
                            RiotApi.query+
                            self._apikey)
        """
        return requests.get(RiotApi.url_v5+
                            match_id+
                            RiotApi.query+
                            self._apikey).json()
#match_v5 -> url_v5+matchid+query+api_key
#timeline -> url_v5+matchid+'/timeline'+query+api_key    
    
    def get_timeline_byMatchid(self,match_id):
        #08.11 match v5 수정
        print(RiotApi.url_v5+
                            match_id+
                            '/timeline'+
                            RiotApi.query+
                            self._apikey)
        return requests.get(RiotApi.url_v5+
                            match_id+
                            '/timeline'+
                            RiotApi.query+
                            self._apikey).json()

if __name__ == '__main__':
    #단위테스트
    test = RiotApi(apikey="RGAPI-90ac4bcf-883d-406a-b5da-0bc3e8bc9418")
    #print(test.get_league(1))
    #user_puuId=test.get_summoner('Hide on bush')
    #print(test.get_summoner_raw('Hide on bush'))
    #user_puuId='uqy66cXvaNu5cUS7nGRvKXRFyX9kSu3vptCijcNBO9hKVUXNaagQ5PYCYSuvItgBAaPXs_svQZrtkA'
    #game_ids=test.get_gameid_byPuuid(user_puuId)
    # print(game_ids[0])
    #match_info = test.get_match_byMatchid('KR_5381618137')#match_v5 test
    # time_line=test.get_timeline_byMatchid('KR_5381618137')
    test.get_timeline_byMatchid('KR_5183897731')
    #test_gameId=games_ids[0] # 게임아이디 하나 받아서, timeline 테스트에 사용
    #test_timeline=test.get_timeline_byMatchid(str(test_gameId))
    #RhV9CBcTzyNArJhyiFMXYT-nOt8j4K8_cMjarSPdDscs0VP0_XvM0CFEi2NIgLNWAG7xLGL1G-ndkQ :puuid
    
    
    #print(test.get_league('1').json())
    
    #games_data


#games_ids
#match_info
#print(len(games_ids))
#test_timeline
#time_line