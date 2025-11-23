import mysql.connector

def show_dependent(ssn):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="SELECT * " \
    "FROM Dependent T " \
    "WHERE T.employee_ssn=%s;"
    values=(ssn,)
    cursor.execute(query, values)
    records=cursor.fetchall()
    for i in records:
        print(i)
    cursor.close()
    cnx.close() 