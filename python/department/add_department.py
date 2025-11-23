import mysql.connector

def add_department(id, num_of_locations, name):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="INSERT INTO Department(dep_id, num_of_locations, dep_name) VALUES (%s, %s, %s);"
    values=(id, num_of_locations, name)
    cursor.execute(query, values)
    cnx.commit()
    print(f"Department {id} is added!")
    cursor.close()
    cnx.close()