import mysql.connector

def show_department(dep_id):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="SELECT * " \
    "FROM Department T " \
    "WHERE T.dep_id=%s;"
    values=(dep_id,)
    cursor.execute(query, values)
    records=cursor.fetchall()
    for i in records:
        print(i)
    cursor.close()
    cnx.close() 