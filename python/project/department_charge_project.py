import mysql.connector

def department_charge_project(dep_id, pj_id):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="INSERT INTO Department_in_charge_Project (dep_id, pj_id) VALUES (%s, %s)"
    values=(dep_id, pj_id)
    cursor.execute(query, values)   
    cnx.commit()
    print(f"Department {dep_id} is in charge of project {pj_id}")
    cursor.close()
    cnx.close()