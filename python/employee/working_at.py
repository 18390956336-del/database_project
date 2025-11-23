import mysql.connector

def working_at(ssn):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="SELECT pj_id " \
    "FROM Employee_works_on_Project " \
    "WHERE ee_ssn=%s;"
    values=(ssn,)
    cursor.execute(query, values)
    records=cursor.fetchall()
    for i in records:
        print("Project: ",i[0])
        print("\n")
    cursor.close()
    cnx.close() 