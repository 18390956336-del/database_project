import mysql.connector

def department_charge_this(pj_id):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="SELECT dep_id " \
    "FROM Department_in_charge_Project " \
    "WHERE pj_id=%s"
    values=(pj_id,)
    cursor.execute(query, values)
    records=cursor.fetchall()
    for i in records:
        print(f"Department {i[0]}")
    cursor.close()
    cnx.close() 
