import cx_Oracle

try:
    con = cx_Oracle.connect('c##scott/tiger@localhost:1521/xe')
    print(con.version)

    cursor = con.cursor()

    cursor.execute("create table x(name integer)")
    #print(x.fetchall())
    print("Table Created successfully")

except cx_Oracle.DatabaseError as e:
    print("There is a problem with oracle")

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()


