from opponentsLOL import RiotApi
import sys
import os
import time
print(sys.path[0])

with open(os.path.join(sys.path[0],'./resource/getSummonerName.txt'),'r', encoding='utf8') as f: # accountID 받아서 accountIDs에 저장
    line=None
    while line!='':
        line=f.readline()
        print(line, end="")