#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ipynb 파일 불러오기 위해서
#!pip install import_ipynb
import import_ipynb


# In[ ]:



from opponentsLOL import RiotApi
import time
import os
import sys

class opponentsParser(RiotApi):
    """
    AUTHOR:이종법
    DATE:2021-03-30
    PURPOSE: RiotApi를 상속받아서, 해당 내용을 parsing하는 class
    해당 클래스에서는 requests를 따로 안써도된다.
    
    
    """

    
    def __init__(self,apikey):
        super().__init__(apikey)
        
        print(self._apikey)    
    
    def getSummonerName(self):
        ### 솔민작성 코드 getSummonerName.py
        ### 결과가 getSummonerName.txt로 출력됨.
        
        #403 error : riot api 오류
        total_summoner = []

        for page in range(1,2000): # summoner 정보 2000페이지까지 돌리기
            summoner_data = self.get_league(str(page)) # summoner_data에 페이지별 json데이터 가져오기
            print(page)
            if len(summoner_data) is 0: # json파일이 더이상 넘어오지 않을 경우 for문 종료
                print('stop')
                break
            for items in summoner_data:
                total_summoner.append(items['summonerName']+'\n') # 공백으로 구분해서 받음
            #보통 5페이지 정도 수행.
        with open('./resource/getSummonerName.txt','w',encoding='utf8') as f:
            f.writelines(total_summoner)
    
    def getAccountID(self):
        ### 솔민 작성 코드 getAccountID.py
        ### getSummonerName.txt를 읽어서 결과가 getAccountID.txt로 출력됨.
        
        count=0 # rate limit excceed 방지 위한 카운트
        accountIDs = []
        with open(os.path.join(sys.path[0],'./resource/getSummonerName.txt'),'r', encoding='utf8') as f: # accountID 받아서 accountIDs에 저장
            summoner=None #한줄씩 받기 위한 변수
            while summoner!='': # 파일의 내용이 비기 전까지
                count=count+1 # count값 증가-
                if count%98==0 and count>=98: # 2분안에 100개 api 보내기 방지
                    #정확히 2분 아니라서 넉넉하게 잡아줘야함

                    print("Time to sleep about 130s..")
                    time.sleep(130)  

                summoner = f.readline().strip() #개행문자도 같이 받아서 삭제하는 작업 해줘야 함
                print(summoner)
                if len(summoner)==0:
                    break
                # try:
                #     accountID=riotApi1.get_summoner(summoner) # 
                # except KeyError:
                #     print('no summoner info!')
                #     continue
                try:
                    accountID=self.get_summoner(summoner)
                except KeyError:
                    print(self.get_summoner_raw(summoner))
                    continue

                print(count)
                accountIDs.append(accountID+'\n')

        with open(os.path.join(sys.path[0],'./resource/getAccountID.txt'),'w', encoding='utf8') as f:
            f.writelines(accountIDs)

    def get_match_ids_test(self):
        # return [match_ids]
        # test를 위해 작성된 코드. file을 읽어옴.
        # file을 읽어서 account_id를 받아서. game_id를 받고. set로 game_id 중복을 제거하여 출력해준다.
        
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
    
    
    def timeline_to_items(self,match_ids):
        
        #match_id 들이 담긴 list에서 각각 타임라인을 호출한다.
        #특정 타임라인에서 item 구매 이벤트들을 저장한다.
        
        
        pass

    def timeline_to_skills(self,timeline_data):
        #특정 타임라인에서 skill levelup 이벤트들을 저장한다.
        
        pass

    
#단위 테스트
if __name__ == '__main__':
    test = opponentsParser('RGAPI-f7922aa7-1787-4f61-be99-432393122bc2')
    
    #test.getSummonerName()
    #time.sleep(120)
    #test.getAccountID()
    #time.sleep(135)
    test.get_match_ids_test()
    
    
    #games_ids=test.get_match_ids_test()
    
    

