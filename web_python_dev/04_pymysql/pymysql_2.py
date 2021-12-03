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
sql = "select * from books order by price"
with connection.cursor() as cursor:
    cursor.execute(sql)  # 执行sql语句
    result1 = cursor.fetchone()  # 获取查询结果
    result2 = cursor.fetchall()  # 获取查询结果

print(result1)
print("*" * 10)
for res in result2:
    print(res)

connection.close()  # 关闭连接