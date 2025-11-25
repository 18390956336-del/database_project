import mysql.connector
from mysql.connector import Error
import os
def setup_database():
    try:
        # 连接MySQL服务器（不指定数据库）
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="515636"
        )
        
        cursor = cnx.cursor()
        
        print("seting up database...")
        current_dir = os.path.dirname(os.path.abspath(__file__))
        sql_file_path = os.path.join(current_dir, 'database.sql')
        
        # 读取SQL文件
        with open(sql_file_path , 'r', encoding='utf-8') as file:
            sql_script = file.read()
        
        # 分割SQL语句并执行
        sql_commands = sql_script.split(';')
        
        for command in sql_commands:
            command = command.strip()
            if command:  # 跳过空命令
                try:
                    cursor.execute(command)
                    if command.upper().startswith('CREATE DATABASE'):
                        cursor.execute("USE company")
                    
                except Error as e:
                    print(f"error: {e}")
        
        cnx.commit()
        print("get ready!")
        
    except Error as e:
        print(f"error: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'cnx' in locals() and cnx:
            cnx.close()


setup_database()