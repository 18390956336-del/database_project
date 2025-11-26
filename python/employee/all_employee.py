import mysql.connector

def all_employee():
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="SELECT * " \
    "FROM Employee;"
    cursor.execute(query)
    records=cursor.fetchall()
    if(records==[]):
        print("No employees here.") 
    else:
        for i in records:
            print(i)
    cursor.close()
    cnx.close() 