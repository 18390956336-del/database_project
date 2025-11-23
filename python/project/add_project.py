import mysql.connector

def add_project(pj_id, name):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="INSERT INTO Project(pj_id, pj_name) VALUES (%s, %s);"
    values=(pj_id, name)
    cursor.execute(query, values)
    cnx.commit()
    print(f"Project {pj_id} is added!")
    cursor.close()
    cnx.close()