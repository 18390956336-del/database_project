import mysql.connector

def set_employee_supervisor(ee_ssn, or_ssn):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="UPDATE Employee "\
    "SET Supervisor_ssn=%s "\
    "WHERE ssn=%s;"
    values=(or_ssn, ee_ssn)
    cursor.execute(query, values)
    cnx.commit()
    print(f"set {ee_ssn}'s supervisor's ssn: {or_ssn}")
    cursor.close()
    cnx.close()
