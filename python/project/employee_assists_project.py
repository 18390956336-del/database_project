import mysql.connector
#此方法不会让这个员工的部门负责这个项目

def employee_assists_project(ssn, pj_id):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="INSERT INTO Employee_works_on_Project (ee_ssn, pj_id) VALUES (%s, %s)"
    values=(ssn, pj_id)
    cursor.execute(query, values)   
    cnx.commit()
    print(f"Employee {ssn} is assisting project {pj_id}")
    cursor.close()
    cnx.close()