import mysql.connector

def add_location(building_name, address, pj_id):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="INSERT INTO Location(building_name, address, pj_id) VALUES (%s, %s, %s);"
    values=(building_name, address, pj_id)
    cursor.execute(query, values)
    cnx.commit()
    print(f"Location is added!")
    cursor.close()
    cnx.close()