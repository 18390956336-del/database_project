import mysql.connector
import num_of_employees

def show_department(dep_id):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="SELECT * " \
    "FROM Department T " \
    "WHERE T.dep_id=%s;"
    values=(dep_id,)
    cursor.execute(query, values)
    records=cursor.fetchall()
    if(records==[]):
        print("No such department.")
    else:
        for i in records:
            number=num_of_employees.num_of_employees(dep_id)
            print(f"Department {i[0]} {i[1]} with {number} employees.")
    cursor.close()
    cnx.close() 