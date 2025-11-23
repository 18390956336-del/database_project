import mysql.connector

def set_employee_minit(ssn, minit):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="UPDATE Employee "\
    "SET Minit=%s "\
    "WHERE ssn=%s;"
    values=(minit, ssn)
    cursor.execute(query, values)
    cnx.commit()
    print(f"set {ssn}'s Minit: {minit}")
    cursor.close()
    cnx.close()

