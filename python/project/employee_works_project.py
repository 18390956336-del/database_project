import mysql.connector
#此方法会自动这个员工的部门负责这个项目

def employee_works_project(ssn, pj_id):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    get_department_query = "SELECT works_for_dep FROM Employee WHERE ssn = %s"
    cursor.execute(get_department_query, (ssn,))
    department_result = cursor.fetchone()
    works_for_dep = department_result[0]
    query1 = "INSERT INTO Employee_works_on_Project(ee_ssn, pj_id) VALUES (%s, %s)"
    values1 = (ssn, pj_id)
    cursor.execute(query1, values1)
    query2 = """INSERT IGNORE INTO Department_in_charge_Project(dep_id, pj_id) 
                    VALUES (%s, %s)"""
    values2 = (works_for_dep, pj_id)
    cursor.execute(query2, values2)
    cnx.commit()
    print(f"Employee {ssn} is working project {pj_id}")
    cursor.close()
    cnx.close()