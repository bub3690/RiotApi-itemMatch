from opponentsLOL import RiotApi
import time
import os
import sys
import pandas as pd
from pandas import DataFrame

class opponentsParser(RiotApi):
    """
    AUTHOR:이종법
    DATE:2021-03-30
    PURPOSE: RiotApi를 상속받아서, 해당 내용을 parsing하는 class
    해당 클래스에서는 requests를 따로 안써도된다.
    
    앞으로 고쳐야할 것 : text파일로 출력하거나 읽는 데이터들은 모두 csv로 바꾼다.
    
    """
    def __init__(self,apikey):
        super().__init__(apikey)
        
        print(self._apikey)    
    
    def getSummonerName(self):
        ### 솔민작성 코드 getSummonerName.py
        ### 결과가 getSummonerName.txt로 출력됨.
        ### 08.11 결과를 getSummonerName.csv로 출력됨.
        
        #403 error : riot api 오류
        total_summoner = []

        for page in range(1,2000): # summoner 정보 2000페이지까지 돌리기
            summoner_data = self.get_league(str(page)) # summoner_data에 페이지별 json데이터 가져오기
            print(page)
            if len(summoner_data) == 0: # json파일이 더이상 넘어오지 않을 경우 for문 종료
                print('stop')
                break
            for items in summoner_data:
                total_summoner.append(items['summonerName'])
            #보통 5페이지 정도 수행.
        #이 부분을 csv로 출력으로 수정함.
        print('summoner 수 : ',len(total_summoner))
        DATA = pd.concat([
            pd.DataFrame(total_summoner),
            ],
            axis=1
        )
        DATA.columns=['summonerName']
        DATA.to_csv("./resource/getSummonerName.csv",index=False,encoding='utf-8-sig')
        print("소환사이름 파일 출력.") 
    
    def getPuuid(self):
        ### 솔민 작성 코드 getAccountID.py
        ### 08.11 엑셀파일 getPuuid.csv 읽는것으로 수정.
        ### getSummonerName.csv를 읽어서 결과가 getAccountID.csv로 출력됨.
        print('getPuuid. 유저 puuid를 출력합니다.')
        
        count=0 # rate limit excceed 방지 위한 카운트
        puuIDs = []# accountID 받아서 accountIDs에 저장
        
        summoners = pd.read_csv('./resource/getSummonerName.csv')['summonerName'].values.tolist()
        #csv를 읽어서, summoners 리스트로 만들어준다.
        
        
        for summoners in summoner:
            count=count+1 # count값 증가-
            if count%98==0 and count>=98: # 2분안에 100개 api 보내기 방지
                #정확히 2분 아니라서 넉넉하게 잡아줘야함

                print("Time to sleep about 130s..")
                time.sleep(130)
            try:
                accountID=self.get_summoner(summoner)
            except KeyError:
                print('--no summoner info \n',self.get_summoner_raw(summoner))
                continue
            print(count)
            puuIDs.append(accountID)
        #리스트들 pandas dataframe 변환
        puuIDs

        with open(os.path.join(sys.path[0],'./resource/getAccountID.txt'),'w', encoding='utf8') as f:
            f.writelines(accountIDs)

    def get_match_ids(self):
        ## 이종법 작성.
        # return [match_ids]
        # test를 위해 작성된 코드. file을 읽어옴.
        ## getAccountId.csv을 읽어서 puuid를 받아서, match_id를 받고. set로 match_id 중복을 제거하여 출력한다.
        
        game_id_set = set() # game_id를 받아서, set에 모두 담아준다. 중복제거됨.
        
        f = open( os.path.join(sys.path[0],"./resource/getAccountId.txt"), 'r',encoding='utf-8')
        test_index = 1
        while True:
            line = f.readline().strip()
            if not line: break
            print(test_index,"처리중")
            #print(line)
            try:
                temp_data =self.get_gameid_byAccountid(line)# 부모클래스인 RiotApi class안에 get_gameid_byAccountid가 있음.
                game_id_set.update(temp_data)
            except:
                print('----오류발생----')
            test_index=test_index+1
            if test_index%100==0 and test_index>=100:
                time.sleep(121)
        f.close()
        print(game_id_set)
        #set를 다시 리스트로 변환 후 ,파일 출력
        game_id_list=list(game_id_set)
        game_id_list = [str(item)+'\n' for item in game_id_list]# game_id가 모두 int로 담아져서 str로 변경후, 개행문자
        print(game_id_list)
        with open( os.path.join(sys.path[0],"./resource/game_id_list.txt"), "w",encoding='utf8') as f:
            f.writelines(game_id_list)
    
    
    
    def get_match_inform(self):
        ## 이종법 작성
        # return none. 대신 match_data.csv 파일을 출력한다.
        # get_match_ids 함수를 통해 출력된 game_id_list.txt를 받아서 실행됨.
        
        #한 게임당 총 14개의 컬럼이 있는 표.
        
        # 1.match_id 2.user_num 번호, 3.champion 번호 4.team_id ,5. win (승1 패0 를 담은것.)
        # 6. spell1Id , 7. spell2Id , 8. perk0, 9. perk1, 10. perk2, 11. perk3, 12. perk4 , 13. perk5,
        # 14. statperk0  15. statperk1  16. statperk0
        # 17. lane
        # 각 컬럼을 리스트로 담음.
        match_id = []
        user_num = []
        champion = []
        team_id = []
        win = []
        spell1Id = []
        spell2Id = []
        perk0 =  []
        perk1 =  []
        perk2 =  []
        perk3 =  []
        perk4 =  []
        perk5 =  []
        statperk0= []
        statperk1= []
        statperk2= []
        lane = []
        
        try:
            match_data =self.get_match_byMatchid('KR_5183897731')# 부모클래스인 RiotApi class안에 get_gameid_byAccountid가 있음.
            
            match_id_var=match_data['info']['gameId']# 처음 읽을때 match_id를 담아둠.
            print("game id : ",match_id_var)
            ## 데이터 파싱 부분
            
            #1. 팀 데이터
            print()
            print("----팀정보 ---")
            teams=match_data['info']['teams']
            print("팀 1 : ",teams[0]['teamId']," Win : ",teams[0]['win'])
            print("팀 2 : ",teams[1]['teamId']," Win : ",teams[1]['win'])
            print("-----팀정보 끝----")
            
            #2. 유저 데이터
            print()
            print("-----유저 데이터------")
            
            participants=match_data['info']['participants']
            for user in participants:
                print("유저 번호:",user['participantId']," 팀 : ",user['teamId'])        
                print("챔피언 : ",user['championName']," 스팰 1: ",user['summoner1Id']," 스팰 2 :",user["summoner2Id"])
                
                if user['teamId']==100:
                    win.append(teams[0]['win'])
                else:
                    win.append(teams[1]['win'])
                
                match_id.append(match_id_var)
                user_num.append(user['participantId'])
                champion.append(user['championId'])
                team_id.append(user['teamId'])
                spell1Id.append(user['summoner1Id'])
                spell2Id.append(user['summoner2Id'])
                
                #stat에서 perk 더 넣어야함.
                stats=user["perks"]["statPerks"]
                statperk0.append(stats["defense"])
                statperk1.append(stats["flex"])
                statperk2.append(stats["offense"])
                #주룬
                primary_perks=user["perks"]["styles"][0]["selections"]
                
                perk0.append(primary_perks[0]["perk"])
                perk1.append(primary_perks[1]["perk"])
                perk2.append(primary_perks[2]["perk"])
                perk3.append(primary_perks[3]["perk"])
                #보조룬
                sub_perks=user["perks"]["styles"][1]["selections"]
                perk4.append(sub_perks[0]["perk"])
                perk5.append(sub_perks[1]["perk"])
                
                #timeline에서 lane 가져오기
                timeline=user["teamPosition"]
                print("라인 : ",timeline)
                lane.append(timeline)
                
                print("----유저 ",user['participantId']," 끝----")
        except Exception as e:
            print('----오류발생----',e)
        
        # test_index=test_index+1
        # if test_index ==2:
        #     #테스트 1게임만 확인
        #     pass
        # if test_index%100==0 and test_index>=100:
        #     time.sleep(121)
                
        ###while문 종료 후, csv 파일로 출력
        # 1.각 리스트를, pandas dataframe으로 바꾸어서, concat해준다.
        
        DATA = pd.concat([
            pd.DataFrame(match_id),
            pd.DataFrame(user_num),
            pd.DataFrame(champion),
            pd.DataFrame(team_id),
            pd.DataFrame(win),
            pd.DataFrame(spell1Id),
            pd.DataFrame(spell2Id),
            pd.DataFrame(perk0),
            pd.DataFrame(perk1),
            pd.DataFrame(perk2),
            pd.DataFrame(perk3),
            pd.DataFrame(perk4),
            pd.DataFrame(perk5),
            pd.DataFrame(statperk0),
            pd.DataFrame(statperk1),
            pd.DataFrame(statperk2),
            pd.DataFrame(lane),
        ],axis=1)
        print(DATA)
        # 2.컬럼명 수정
        DATA.columns=[
            'match_id',
            'user_num',
            'champion',
            'team_id',
            'win',
            'spell1Id',
            'spell2Id',
            'perk0',
            'perk1',
            'perk2',
            'perk3',
            'perk4',
            'perk5',
            'statperk0',
            'statperk1',
            'statperk2',
            'lane'
        ]
        # 3.csv 파일로 출력한다.
        print('통과')
        DATA.to_csv(os.path.join(sys.path[0],'./resource/match_data.csv'),index=False)
        
        print("파일 출력.")
    
    
    
    def get_timeline_inform(self,):
        ## 솔민 작성
        #match_id 들이 담긴 list에서 각각 타임라인을 호출한다.
        #특정 타임라인에서 item 구매 이벤트들을 저장한다.
        #return none.
        #출력: 2개 csv 파일. timeline_skill_data.csv  , timeline_item_data.csv
        
        #사용하는 변수들 정리. 이 컬럼들을 엑셀로 출력한다.
        # timeline_item_data.csv
        item_match_id=[]
        item_participantId=[]
        item_timestamp=[]
        itemId=[]
        
        # timeline_skill_data.csv
        skill_match_id=[]
        skill_participantId=[]
        skill_timestamp=[]
        skillSlot=[]
        
        matchId='KR_5183897731'
        timeline_data=self.get_timeline_byMatchid(matchId)

        count=0
        while count!=1: # test용으로 200개만 가져오기
            count=count+1
            if(count==2):
                #test를 위해 한개 수행하면 종료.
                break

            if count%98==0 and count>=98: # 2분안에 100개 api 보내기 방지
                #정확히 2분 아니라서 넉넉하게 잡아줘야함
                print("Time to sleep about 130s..")
                time.sleep(130)  
            timelineInfo=timeline_data["info"]
            
            #타임라인 정보를 timelineInfo로 가져오기
            frames=timelineInfo["frames"]
            #frames는 타임당 하나 존재.
            #  frames안에 participantFrames안에 champion이 10명이니 "1"~"10"까지 존재.(사용안함.)
            #  frames안에 events가 있고. 비었을 수 도 있다.
            #  events안에 participantId는 와드설치 등의 이유로 비었을 수 있음. 그럴때 pass해야함.
            
            print(frames)
            for frame in frames:
                events=frame["events"]
                
                for event in events:
                    print(event["type"])
                    
                    if "participantId" in event:
                        print("유저 번호: ",event["participantId"])
                        print("시간 timestamp: ",event["timestamp"])
                    else:
                        #와드 설치등의 이벤트는 거르는것.
                        continue
                    # 타입구분(item 구매, )
                    if(event["type"]=='ITEM_PURCHASED'):
                        item_match_id.append(matchId)
                        item_participantId.append(event["participantId"])
                        item_timestamp.append(event["timestamp"])
                        #뭐샀는지 출력
                        print("아이템 구매 itemId: ",event["itemId"])
                        itemId.append(event["itemId"])
                    elif(event["type"]=='SKILL_LEVEL_UP'):
                        skill_match_id.append(matchId)
                        skill_participantId.append(event["participantId"])
                        skill_timestamp.append(event["timestamp"])
                        print("skill slot: ", event["skillSlot"])
                        skillSlot.append(event["skillSlot"])
        #list로 담긴 데이터들을 모두 , pandas dataframe으로 바꾸고
        ITEM_DATA = pd.concat([
            pd.DataFrame(item_match_id),
            pd.DataFrame(item_participantId),
            pd.DataFrame(itemId),
            pd.DataFrame(item_timestamp)],
            axis=1)
        ITEM_DATA.columns=['match_id','participantId','itemId','time_stamp']
        SKILL_DATA = pd.concat([
            pd.DataFrame(skill_match_id),
            pd.DataFrame(skill_participantId),
            pd.DataFrame(skillSlot),
            pd.DataFrame(skill_timestamp)
        ],axis=1)
        SKILL_DATA.columns=['match_id','participantId','skillSlot','time_stamp']
        #엑셀출력
        SKILL_DATA.to_csv(os.path.join(sys.path[0],"./resource/timeline_skill_data.csv"),index=False)
        ITEM_DATA.to_csv(os.path.join(sys.path[0],"./resource/timeline_item_data.csv"),index=False)
        print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ파일 출력.ㅡㅡㅡㅡㅡㅡㅡㅡ")
    
#단위 테스트
if __name__ == '__main__':
    test = opponentsParser('RGAPI-8a956514-6bb5-408d-9404-29f4e00088e4')
    # test.get_match_inform()
    test.get_timeline_inform()
    #test.getSummonerName()
    #time.sleep(120)
    #test.getAccountID()
    #time.sleep(135)
    #test.get_match_ids()
    #test.get_match_inform()
    #test.get_timeline_inform()
    
    
    #games_ids=test.get_match_ids()