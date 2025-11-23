import mysql.connector

def num_of_employees(dep_id):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="SELECT COUNT(*) " \
    "FROM Employee T " \
    "WHERE T.works_for_dep=%s;"
    values=(dep_id,)
    cursor.execute(query, values)
    records=cursor.fetchall()
    for i in records:
        print(i[0])
    cursor.close()
    cnx.close() 