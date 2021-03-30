from opponentsLOL import RiotApi

riotApi1=RiotApi('RGAPI-2c57b69e-3636-433d-bbd5-bdb5a3bdd474') #내 riotapi key 넣기
#네이밍 다시 할거임

accountIDs = []
with open('C:/Project/py/resource/getSummonerName.txt','r') as f: # accountID 받아서 accountIDs에 저장
    for line in f:
        summoner = f.readline().strip() #개행문자도 같이 받아서 삭제하는 작업 해줘야 함
        print(summoner)
        if len(summoner)==0:
            break
        try:
            accountID=riotApi1.get_summoner(summoner) # 
        except KeyError:
            print('no summoner info!')
            continue
        print('get Succeed!')
        accountIDs.append(accountID+'\n')

with open('C:/Project/py/resource/getAccountId.txt','w') as f:
    f.writelines(accountIDs)