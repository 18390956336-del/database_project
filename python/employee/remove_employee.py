import mysql.connector

def remove_employee(ssn):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="DELETE FROM Employee " \
    "WHERE ssn=%s"
    values=(ssn,)
    cursor.execute(query, values)
    cnx.commit()
    print(f"Employee {ssn} has been deleted")
    cursor.close()
    cnx.close()
