import mysql.connector

def remove_dependent(ssn):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="DELETE FROM Dependent " \
    "WHERE employee_ssn=%s"
    values=(ssn,)
    cursor.execute(query, values)
    cnx.commit()
    print(f"{ssn}'s dependent has been deleted")
    cursor.close()
    cnx.close()
