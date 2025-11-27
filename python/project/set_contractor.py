import mysql.connector

def set_contractor(pj_id, contractor):
    cnx=mysql.connector.connect(
        host="localhost",
        user="root",
        password="515636",
        database="company"
    )

    cursor=cnx.cursor()
    query="UPDATE Project "\
    "SET contractor=%s "\
    "WHERE pj_id=%s;"
    values=(contractor, pj_id)
    cursor.execute(query, values)
    cnx.commit()
    print(f"Project {pj_id} is set to contractor {contractor}")
    cursor.close()
    cnx.close()
