import mysql.connector

def supervising(ssn):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="SELECT ssn " \
    "FROM Employee " \
    "WHERE Supervisor_ssn=%s;"
    values=(ssn,)
    cursor.execute(query, values)
    records=cursor.fetchall()
    if(records==[]):
        print("This employee is not a supervisor.")
    else:
        print("Supervising:")
        for i in records:
            print(i[0])
    cursor.close()
    cnx.close() 
