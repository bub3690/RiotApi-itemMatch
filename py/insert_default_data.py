import pymysql.cursors
from champ_info import championInfo


connection = pymysql.connect(host='52.78.93.239', port=52879, user='root', password='',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

#champion information insert    
champ_info=championInfo.get_info()                    
# try:
#     with connection.cursor() as cursor:
#         for i in champ_info:
#             sql = "insert into champ_info values(%s,%s,%s)"
#             cursor.execute(sql, (i.id, i.champNameEng, i.champNameKor))
#     # connection is not autocommit by default. So you must commit to save changes.
#     connection.commit()
# finally:
#     connection.close()

#skill information insert
try:
    with connection.cursor() as cursor:
        for i in champ_info:
            for m in i.skill_info:
                sql = "insert into skill_info values(%s,%s,%s,%s)"
                print(m["id"])
                cursor.execute(sql, (i.id, m["id"], m["name"],m["description"]))
    # connection is not autocommit by default. So you must commit to save changes.
    connection.commit()
finally:
    connection.close()