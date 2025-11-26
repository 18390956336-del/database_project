import mysql.connector

def employee_working_this(pj_id):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="""SELECT T.ssn, T.Fname, T.Lname, 
                  (SELECT H.working_time 
                   FROM Employee_works_on_Project H 
                   WHERE T.ssn = H.ee_ssn AND H.pj_id = %s 
                   LIMIT 1) as working_time
           FROM Employee T 
           WHERE T.ssn IN (SELECT H.ee_ssn 
                           FROM Employee_works_on_Project H 
                           WHERE H.pj_id = %s)"""
    values=(pj_id, pj_id)
    cursor.execute(query, values)
    records=cursor.fetchall()
    for i in records:
        print(i[0], i[1], i[2], "has worked for", i[3], "hours")
    cursor.close()
    cnx.close() 