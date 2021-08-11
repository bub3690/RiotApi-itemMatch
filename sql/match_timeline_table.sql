-- 0803 이종법 작성부분
-- match_data
CREATE TABLE match_info
(
	match_id varchar(20) NOT NULL,
    user_number INT NOT NULL,
    champion INT NOT NULL,
    team_id	INT NOT NULL,
    win	varchar(10) NOT NULL,
    spell1Id INT NOT NULL,
    spell2Id INT NOT NULL,
    perk0	INT NOT NULL,
    perk1	INT NOT NULL,
    perk2	INT NOT NULL,
    perk3	INT NOT NULL,
    perk4	INT NOT NULL,
    perk5	INT NOT NULL,
    lane	varchar(10),
    CONSTRAINT PK_match_info PRIMARY KEY (match_id,user_number)
)default character set utf8 collate utf8_general_ci;

-- timeline에서 스킬 레벨업 데이터
CREATE TABLE timeline_skill
(
	match_id varchar(20) NOT NULL,
    participantId INT NOT NULL,
    skillSlot INT NOT NULL,
    time_stamp varchar(10) NOT NULL
)default character set utf8 collate utf8_general_ci;

-- timeline에서 아이템 구매 데이터
CREATE TABLE timeline_item
(
	match_id varchar(20) NOT NULL,
    participantId INT NOT NULL,
    itemId INT NOT NULL,
    time_stamp varchar(10) NOT NULL
)default character set utf8 collate utf8_general_ci;