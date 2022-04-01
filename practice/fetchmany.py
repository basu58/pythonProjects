import cx_Oracle
import config

sql = 'select * from employees'
batch_size = 20
try:
    with cx_Oracle.connect(
            config.username,
            config.password,
            config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            # execute the SQL statement
            cursor.execute(sql)
            while True:
                # fetch rows
                rows = cursor.fetchmany(batch_size)
                if not rows:
                    break
                # display rows
                for row in rows:
                    print(row)
except cx_Oracle.Error as error:
    print(error)
