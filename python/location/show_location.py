import mysql.connector

def show_location(pj_id):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="SELECT * " \
    "FROM Location T " \
    "WHERE T.pj_id=%s;"
    values=(pj_id,)
    cursor.execute(query, values)
    records=cursor.fetchall()
    if(records==[]):
        print("Nothing")
    else:
        for i in records:
            print(f"{i[0]},", i[1])
    cursor.close()
    cnx.close() 