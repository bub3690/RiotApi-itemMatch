with Opponents as(
    select * from match_info as A, match_info as B where A.match_id=B.match_id
        and a.lane='top' and b.lane='top' and a.champ='gnar' and b.champ='Irelia'
)
select * from Opponents;
    