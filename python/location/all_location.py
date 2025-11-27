import mysql.connector

def all_location():
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="SELECT * " \
    "FROM Location;"
    cursor.execute(query)
    records=cursor.fetchall()
    if(records==[]):
        print("No projects here.")
    else:
        for i in records:
            print(i)
    cursor.close()
    cnx.close() 