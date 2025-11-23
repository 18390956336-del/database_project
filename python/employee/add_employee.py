import mysql.connector

def add_employee(ssn, Fname, Lname, Bdate, ee_address, dep_id):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="INSERT INTO Employee(ssn, Fname, Lname, Bdate, ee_address, works_for_dep) VALUES (%s, %s, %s, %s, %s, %s);"
    values=(ssn, Fname, Lname, Bdate, ee_address, dep_id)
    cursor.execute(query, values)
    cnx.commit()
    print(f"employee {Fname} {Lname} is added!")
    cursor.close()
    cnx.close()