import pymysql

conn = pymysql.connect(host="127.0.0.1", port=3306,
                       user="root", password="123456",
                       db="test_db", charset="utf8")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

cursor.execute("SELECT * FROM user_table;")

# print(cursor.fetchone())
# print(cursor.fetchmany(3))

user_list = cursor.fetchall()

for user in user_list:
    print(user)

cursor.close()
conn.close()
