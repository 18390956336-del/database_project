import mysql.connector

def set_date(building_name, address, date):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="UPDATE Location "\
    "SET date=%s "\
    "WHERE building_name=%s AND address=%s;"
    values=(date, building_name, address)
    cursor.execute(query, values)
    cnx.commit()
    print(f"{building_name} at {address} will have a project at date: {date}")
    cursor.close()
    cnx.close()

