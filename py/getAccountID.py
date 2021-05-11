from opponentsLOL import RiotApi
import sys
import os
import time
print(sys.path[0])

#네이밍 다시 할거임
#rate limit exceeded : 사용자별 일일 api 사용 횟수가 정해져 있음.
#해결법 : 우선은 sleep으로 해야 할 듯
#최대한 여러 id 가져와서 key값을 가져와야 함
#key값을 가져오는 api?

count=0 # rate limit excceed 방지 위한 카운트
accountIDs = []
with open(os.path.join(sys.path[0],'./resource/getSummonerName.txt'),'r', encoding='utf8') as f: # accountID 받아서 accountIDs에 저장
    riotApi1=RiotApi('RGAPI-1e589003-f5ad-4e73-a252-85bbe3ba8871') #내 riotapi key 넣기
    summoner=None #한줄씩 받기 위한 변수
    while summoner!='': # 파일의 내용이 비기 전까지
        count=count+1 # count값 증가-
        if count%99==0 and count>=99: # 2분안에 100개 api 보내기 방지
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
            accountID=riotApi1.get_summoner(summoner)
        except KeyError:
            print(riotApi1.get_summoner_raw(summoner))
            continue
            
        print(count)
        accountIDs.append(accountID+'\n')

with open(os.path.join(sys.path[0],'./resource/getAccountID.txt'),'w', encoding='utf8') as f:
    f.writelines(accountIDs)
