import mysql.connector

def managed_by(dep_id):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="SELECT ssn, Fname, Lname " \
    "FROM Employee " \
    "WHERE manage_dep=%s;"
    values=(dep_id,)
    cursor.execute(query, values)
    records=cursor.fetchall()
    if(records==[]):
        print("This department has no manager.")
    else:
        print(records[0][1], records[0][2], "with SSN", records[0][0], "manages this department.")
    cursor.close()
    cnx.close() 