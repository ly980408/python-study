from flask import Flask, render_template, request, url_for
import pymysql

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

def connect_db():
    return pymysql.connect(host="127.0.0.1", port=3306,
                           user="root", password="123456",
                           db="test_db", charset="utf8")

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return render_template('add_user.html')

    name = request.form.get('name')
    age = request.form.get('age')

    if name.strip() == '':
        return '姓名不能为空！'

    if age.strip() == '':
        age = None
    else:
        age = int(age)

    # insert data into db
    conn = connect_db()
    cursor = conn.cursor()
    sql = "INSERT INTO user_table (name, age) VALUES (%(name)s, %(age)s);"
    cursor.execute(sql, {'name': name, 'age': age})

    conn.commit()

    # 关闭连接
    cursor.close()
    conn.close()

    return '添加成功'

@app.route('/get_user_list', methods=['GET'])
def get_user_list():
    conn = connect_db()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    
    cursor.execute("SELECT * FROM user_table;")

    user_list = cursor.fetchall()

    cursor.close()
    conn.close()

    return user_list

@app.route('/user_list', methods=['GET'])
def user_list():
    user_list = get_user_list()
    return render_template('user_list.html', user_list=user_list)


if __name__ == '__main__':
    app.run()
