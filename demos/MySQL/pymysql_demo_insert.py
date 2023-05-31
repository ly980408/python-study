import pymysql

name = input("Input your name:")
age = input("Input your age:")

# 创建连接
conn = pymysql.connect(host="127.0.0.1", port=3306,
                       user="root", password="123456",
                       db="test_db", charset="utf8")

# 创建游标
cursor = conn.cursor()

# 执行sql (不要用字符串格式化的方式去做sql拼接，有安全隐患，使用pymysql提供的占位符实现)
# sql = "INSERT INTO user_table (name, age) VALUES (%s, %s);"
# cursor.execute(sql, ['user_added_by_py', 9])
# or
sql = "INSERT INTO user_table (name, age) VALUES (%(name)s, %(age)s);"
cursor.execute(sql, {'name': name, 'age': age})

conn.commit()

# 关闭连接
cursor.close()
conn.close()
