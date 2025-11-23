import mysql.connector

def show_project(pj_id):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="SELECT * " \
    "FROM Project T " \
    "WHERE T.pj_id=%s;"
    values=(pj_id,)
    cursor.execute(query, values)
    records=cursor.fetchall()
    for i in records:
        print(i)
    cursor.close()
    cnx.close() 