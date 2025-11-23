import mysql.connector

def add_dependent(ssn, name, sex, birth_date):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="INSERT INTO Dependent(employee_ssn, ful_name, sex, birth_date) VALUES (%s, %s, %s, %s);"
    values=(ssn, name, sex, birth_date)
    cursor.execute(query, values)
    cnx.commit()
    print(f"Dependent {name} is added!")
    cursor.close()
    cnx.close()