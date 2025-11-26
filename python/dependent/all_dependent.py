import mysql.connector

def all_dependent():
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="SELECT * " \
    "FROM Dependent;"
    cursor.execute(query)
    records=cursor.fetchall()
    if(records==[]):
        print("No dependents here.")    
    else:
        for i in records:
            print(f"{i[0]}'s dependent {i[1]}: {i[2]}, born on {i[3]}")
    cursor.close()
    cnx.close() 