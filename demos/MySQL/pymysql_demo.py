import pymysql

# 创建连接
conn = pymysql.connect(host="127.0.0.1", port=3306,
                       user="root", password="123456",
                       db="test_db", charset="utf8")

# 创建游标
cursor = conn.cursor()

# 执行sql
# cursor.execute("SELECT * FROM user_table;")
cursor.execute("INSERT INTO user_table (name) VALUES ('test_user');")
conn.commit()

# 关闭连接
cursor.close()
conn.close()
