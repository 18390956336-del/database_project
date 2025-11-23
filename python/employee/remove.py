import mysql.connector

def remove(ssn):
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
    print(f"{ssn} has been deleted")
    cursor.close()
    cnx.close()
