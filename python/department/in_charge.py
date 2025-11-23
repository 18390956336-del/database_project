import mysql.connector

def in_charge(dep_id):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="SELECT pj_id " \
    "FROM  Department_in_charge_Project " \
    "WHERE dep_id=%s;"
    values=(dep_id,)
    cursor.execute(query, values)
    records=cursor.fetchall()
    for i in records:
        print("Project: ",i[0])
        print("\n")
    cursor.close()
    cnx.close() 