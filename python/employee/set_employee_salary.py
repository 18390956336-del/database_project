import mysql.connector

def set_employee_salary(ssn, Salary):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="UPDATE Employee "\
    "SET Salary=%s "\
    "WHERE ssn=%s;"
    values=(Salary, ssn)
    cursor.execute(query, values)
    cnx.commit()
    print(f"set {ssn}'s salary: {Salary}")
    cursor.close()
    cnx.close()

