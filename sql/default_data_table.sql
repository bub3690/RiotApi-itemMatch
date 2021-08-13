
--솔민 작성 08/13
create table champ_info(
    id integer not null primary key,
    kor_name varchar(20) not null,
    eng_name varchar(20) not null,
    img_url varchar(200)
)default character set utf8 collate utf8_general_ci;

create table skill_info(
	id integer not null,
	skill_id varchar(40) not null,
	skill_name varchar(40) not null,
	description varchar(500),
	img_url varchar(200),
	primary key(id, skill_id),
	FOREIGN key(id) REFERENCES champ_info(id)
)default character set utf8 collate utf8_general_ci;

create table rune_info(
    id integer not null primary key,
    category varchar(20) not null,
    eng_category varchar(20) not null,
    kor_name varchar(20) not null,
    eng_name varchar(20) not null,

    decription varchar(500) not null,
    img_url varchar(200)
)default character set utf8 collate utf8_general_ci;
create table spell_info(
    id integer not null primary key,
    kor_name varchar(20) not null,
    eng_name varchar(40) not null,
    decription varchar(500) not null,
    img_url varchar(200)
)default character set utf8 collate utf8_general_ci;

create table item_info(
    id integer not null primary key,
    kor_name varchar(20) not null,
    category varchar(20),
    decription varchar(1000) not null,
    img_url varchar(200)
)default character set utf8 collate utf8_general_ci;

