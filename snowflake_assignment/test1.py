import snowflake.connector

# Snowflake Connection Details
snowflake_account = 'xd35915.ap-southeast-1'
snowflake_user = 'BASUDEVC'
snowflake_password = 'Basu@123'
snowflake_database = 'BBI_ASSIGNMENT'
snowflake_warehouse = 'BBI_WH'
snowflake_schema = 'TEST_1'

# Snowflake Connection
conn = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account,
    warehouse=snowflake_warehouse,
    database=snowflake_database,
    schema=snowflake_schema
)


def create_table_with_sequence(table_name, seq_name, columns):
    try:
        cursor = conn.cursor()

        # Create sequence
        create_sequence_sql = f'''
        CREATE SEQUENCE "{seq_name}"
        '''
        cursor.execute(create_sequence_sql)

        # Create table with sequence
        create_table_sql = f'''
        CREATE OR REPLACE TABLE "{table_name}" (
            id_column INT DEFAULT "{seq_name}".NEXTVAL,
            {', '.join([f'"{col["name"]}" {col["type"]}' for col in columns])},
            PRIMARY KEY (id_column)
        )
        '''
        cursor.execute(create_table_sql)

        cursor.close()
        conn.close()
    except Exception as E:
        print(E)


# Define columns for the table
columns = [
    {"name": "column1_name", "type": "VARCHAR(50)"},
    {"name": "column2_name", "type": "INT"},
    {"name": "column3_name", "type": "TIMESTAMP"}
]

# Specify table name and sequence name
table_name = 'sample_dynamic'
seq_name = 'seq_dynamic'

# Call the function to create the table with sequence
create_table_with_sequence(table_name, seq_name, columns)
