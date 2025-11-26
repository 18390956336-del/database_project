import mysql.connector
from mysql.connector import Error
import os
def setup_database():
    try:
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="515636"
        )
        
        cursor = cnx.cursor()
        
        print("setting up database...")
        current_dir = os.path.dirname(os.path.abspath(__file__))
        sql_file_path = os.path.join(current_dir, 'database.sql')
        
        with open(sql_file_path , 'r', encoding='utf-8') as file:
            sql_script = file.read()
        
        sql_commands = sql_script.split(';')
        
        for command in sql_commands:
            command = command.strip()
            if command:  
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