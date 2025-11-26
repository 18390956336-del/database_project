import mysql.connector

def all_project():
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="SELECT * " \
    "FROM Project;"
    cursor.execute(query)
    records=cursor.fetchall()
    if(records==[]):
        print("No projects here.")
    else:
        for i in records:
            print(f"Project {i[0]}: {i[1]}")
    cursor.close()
    cnx.close() 