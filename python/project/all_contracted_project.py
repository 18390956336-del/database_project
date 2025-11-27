import mysql.connector

def all_contracted_project():
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="SELECT * " \
    "FROM Project " \
    "WHERE contractor IS NOT NULL;"
    cursor.execute(query)
    records=cursor.fetchall()
    if(records==[]):
        print("No projects here.")
    else:
        for i in records:
            print(f"{i[2]} Project {i[0]}, {i[1]}: {i[3]}")
    cursor.close()
    cnx.close() 