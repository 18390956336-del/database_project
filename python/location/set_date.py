import mysql.connector

def set_date(pj_id, date):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="UPDATE Location "\
    "SET date=%s "\
    "WHERE pj_id=%s;"
    values=(date, pj_id)
    cursor.execute(query, values)
    cnx.commit()
    print(f"Project {pj_id}'s date: {date}")
    cursor.close()
    cnx.close()

