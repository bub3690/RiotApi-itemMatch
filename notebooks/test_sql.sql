use test;

create table test_item(
	match_id varchar(30) not null,
    participantId int not null,
	itemId int not null,
	time_stamp int not null,
    primary key(match_id)
);

select * from test_item;