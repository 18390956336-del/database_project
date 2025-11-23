import mysql.connector

def employee_manage(dep_id, ssn):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="UPDATE Employee "\
    "SET manage_dep=%s "\
    "WHERE ssn=%s;"
    values=(dep_id, ssn)
    cursor.execute(query, values)
    cnx.commit()
    print(f"{ssn} is managing {dep_id}")
    cursor.close()
    cnx.close()

