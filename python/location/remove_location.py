import mysql.connector

def remove_location(building_name, address):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="DELETE FROM Project " \
    "WHERE building_name=%s AND address=%s;"
    values=(building_name, address)
    cursor.execute(query, values)
    cnx.commit()
    print(f"Location has been deleted")
    cursor.close()
    cnx.close()
