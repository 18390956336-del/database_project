import mysql.connector

def set_workingtime(ee_ssn, pj_id, workingtime):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="UPDATE Employee_works_on_Project "\
    "SET working_time=%s "\
    "WHERE ee_ssn=%s AND pj_id=%s;"
    values=(workingtime, ee_ssn, pj_id)
    cursor.execute(query, values)
    cnx.commit()
    print(f"Employee {ee_ssn} has worked for {workingtime} hours on project {pj_id}")
    cursor.close()
    cnx.close()
