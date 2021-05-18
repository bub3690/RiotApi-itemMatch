from opponentsLOL import RiotApi
import time
import os
import sys

apikey1="RGAPI-1e589003-f5ad-4e73-a252-85bbe3ba8871"

count=0

# class participants():

#     def __init__(self, )

with open(os.path.join(sys.path[0],'./resource/game_id_list.txt'),'r', encoding='utf8') as f: # gameidlist 불러오기
    riotapi1=RiotApi(apikey1)
    matchId=None
    while count!=1: # test용으로 200개만 가져오기
        count=count+1

        if count%98==0 and count>=98: # 2분안에 100개 api 보내기 방지
            #정확히 2분 아니라서 넉넉하게 잡아줘야함
            print("Time to sleep about 130s..")
            time.sleep(130)  

        matchId=f.readline().strip()
        timelineInfo=riotapi1.get_timeline_byMatchid(matchId)
        #타임라인 정보를 timelineInfo로 가져오기
        frames=timelineInfo["frames"]
        for i in frames:
            events=i["events"]
            for n in events:
                print(n["participantId"])
                # for m in n:
                #     print(m["participantId"])
                #     print(m["type"])
                #     if m["type"]=="ITEM_PURCHASED":
                #         print(m["itemId"])
                #     elif m["type"]=="SKILL_LEVEL_UP":
                #         print(m["skillSlot"])
                    
