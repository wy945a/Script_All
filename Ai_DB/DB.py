import json
import re
import mysql.connector
import ai
# 创建连接
def db_connection():
    db_connection = mysql.connector.connect(
        host="******",  # 替换为数据库主机地址
        user="root",  # 替换为用户名
        password="*****",  # 替换为密码
        database="test"  # 替换为数据库名称
    )

    # 创建游标对象
    cursor = db_connection.cursor()

    # 执行查询
    cursor.execute("SHOW CREATE TABLE users_dctuser;")  # 替换为你要查询的表

    # 获取查询结果
    result = cursor.fetchall()

    # 打印查询结果
    for row in result:
        print(row[1])

    # 关闭游标和连接
    cursor.close()
    db_connection.close()
    return row[1]

def table_info():
    # 创建连接
    conn = mysql.connector.connect(
        host="11.22.33.44",  # 替换为数据库主机地址
        user="root",  # 替换为用户名
        password="1234",  # 替换为密码
        database="test"  # 替换为数据库名称
    )

    # 创建游标
    cursor = conn.cursor()

    # 获取表结构信息
    table_name = "users_dctuser"  # 替换为你要查看的表名
    cursor.execute(f"PRAGMA table_info({table_name})")

    # 获取并打印表结构
    for column in cursor.fetchall():
        print(column)

    # 关闭连接
    cursor.close()
    conn.close()

if __name__ == '__main__':
    info = db_connection()
    question = "帮我查出来最近时间登录的两条数据和最晚的登录时间一条"
    answer = ai.get_response(str(info) + '\n' + "上述表结构中，给我写一个sql：" + question)
    print("answer的值:", answer)
    answer = json.loads(answer)
    content = answer['choices'][0]['message']['content']
    # 使用正则表达式查找SQL代码块
    sql_pattern = re.compile(r'```sql(.*?)```', re.DOTALL)
    match = sql_pattern.search(content)
    if match:
        # 提取SQL语句并去除多余的空白符
        sql_statement = match.group(1).strip()
        print(sql_statement)
    else:
        print("No SQL statement found.")
