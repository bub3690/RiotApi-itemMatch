# RiotApi-itemMatch

### INTRODUCE
```
Give item-tree information of your lol Champion when laning phase for every enemy champion.

기존 OP.GG에서는 라인전 상대에 따른 챔피언 아이템 트리를 제공하지 않는다.
RIOT API를 이용해서, 챔피언 상대별 아이템 트리를 제공하여, 웹페이지 운영이 최종목표이다.
https://www.notion.so/Opponents-lol-b16f8bc8ba6446e8913c699f71e36046
```

### 1. 컴퓨터 구성 / 필수 조건 안내 (Prerequisites)
```
1. python (3.8)
2. python library - requests
3. python library - pandas
4. python library - numpy
```


### 2. 설치안내 ( Project Setup )
```
1. www.python.org 사이트 접속 후 아키텍쳐와 운영체제에 맞는 python 다운로드 및 설치
2. pip show requests requests pandas numpy로 패키지 설치여부 확인
3. 미설치된 패키지들은 pip install [패키지명]으로 설치
```

### 3. 사용법 ( Getting Started )
```
유저는 추후에 만들어질 opponents.lol domain 접속 후 기타 전적검색 사이트와 동일한 방식으로
원하는 정보를 가져올 수 있다. Grandmaster 매치정보 기반으로 데이터를 제공한다.
원하는 라인 선택 -> 캐릭터 선택 -> 상대 캐릭터 선택 시 그에 맞는 추천 스킬트리, 아이템트리, 룬 정보를
제공하며 유저들끼리 정보를 주고받을 수 있는 팁 게시판을 사용할 수 있다.
```
### 4. 파일 정보 및 목록 ( File Manifest )

### 5. 저작권 및 사용권 정보 (Copyright / End User License)

### 6. 배포자 및 개발자의 연락처 정보 (Contact Information)

### 7. 알려진 버그 (Known Issues)

### 8. 문제 발생에 대한 해결책 (Troubleshooting)

### 9. credit

### 10. 업데이트 정보 (Change Log)

### 11. git 사용법
```
포크한 깃허브 저장소를 원본 저장소와 동기화 하기

// 현재 설정된 리모트 저장소 조회
$ git remote -v

// 리모트 저장소 추가
git remote add upstream https://github.com/ax5ui/ax5ui-kernel

//리모트 저장소 패치하기
git fetch upstream
	
// 리모트 저장소 merge
$ git merge upstream/master

git push origin master


```