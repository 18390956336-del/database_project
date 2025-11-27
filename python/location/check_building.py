import mysql.connector

def check_building(building_name):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="SELECT T.date, Y.type, Y.pj_id " \
    "FROM Location T, Project Y " \
    "WHERE building_name=%s AND T.pj_id=Y.pj_id;"
    values=(building_name,)
    cursor.execute(query, values)
    records=cursor.fetchall()
    print(f"{building_name}:")
    for i in records:
        print(f"{i[1]} Project {i[2]}: {i[0]}")
    cursor.close()
    cnx.close()

