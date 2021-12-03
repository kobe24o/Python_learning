import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='michaeldata',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor  # 游标类型
    )
    print("连接成功：", connection)
except Exception as e:
    print("连接失败：", e)

# sql 语句
sql = '''
create table if not exists books(
    id int not null auto_increment,
    name varchar(255) not null,
    category varchar(50) not null,
    price decimal(10, 2) default '0',
    publish_time date default null,
    primary key (id)
) engine = InnoDB auto_increment=1 
default charset = utf8mb4 collate = utf8mb4_0900_ai_ci;
'''

cursor = connection.cursor()  # 获取游标对象
cursor.execute(sql)  # 执行sql语句

# sql1 = 'insert into books(name, category, price, publish_time) values("python web开发", "python", "98.8", "2020-01-01")'
# cursor.execute(sql1)  # 执行sql语句
# connection.commit()  # connection 提交才能生效

# 数据列表
data = [("零基础学Python", 'Python', '79.80', '2018-5-20'),
        ("Python从入门到精通", 'Python', '69.80', '2018-6-18'),
        ("零基础学PHP", 'PHP', '69.80', '2017-5-21'),
        ("PHP项目开发实战入门", 'PHP', '79.80', '2016-5-21'),
        ("零基础学Java", 'Java', '69.80', '2017-5-21'),
        ]
try:
    cursor.executemany('insert into books(name, category, price, publish_time) values(%s, %s, %s, %s)', data)
    connection.commit()  # connection 提交才能生效
except Exception as e:
    connection.rollback()  # 回滚

cursor.close()  # 先关闭游标
connection.close()  # 再关闭连接，或者使用 with as
