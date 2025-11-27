import mysql.connector

def check_time(date):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="SELECT T.building_name, T.address, Y.type, Y.pj_id " \
    "FROM Location T, Project Y " \
    "WHERE date=%s AND T.pj_id=Y.pj_id;"
    values=(date,)
    cursor.execute(query, values)
    records=cursor.fetchall()
    print(f"{date}:")
    for i in records:
        print(f"{i[2]} Project {i[3]} at {i[0]}, {i[1]}")
    cursor.close()
    cnx.close()

