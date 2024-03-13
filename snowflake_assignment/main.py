import snowflake.connector
import boto3
from datetime import datetime

# Snowflake Connection Details
snowflake_account = 'xd35915.ap-southeast-1'
snowflake_user = 'BASUDEVC'
snowflake_password = 'Basu@123'
snowflake_database = 'BBI_ASSIGNMENT'
snowflake_warehouse = 'BBI_WH'
snowflake_schema = 'TEST_1'

# AWS S3 Details
aws_access_key = 'AKIA3FLDX2HLZ2H3LMYM'
aws_secret_key = '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'
s3_bucket_name = 'bbi-assignment'

# Snowflake Connection
conn = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account,
    warehouse=snowflake_warehouse,
    database=snowflake_database,
    schema=snowflake_schema
)

# AWS S3 Client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)


# Function to Load Data into Snowflake
def load_data(table_name, file_path):
    # Load data into Snowflake
    cursor = conn.cursor()
    cursor.execute(f'COPY INTO "{table_name}" FROM @mystage/"{file_path}" FILE_FORMAT=(TYPE=CSV)')

    # Move file to processed directory
    s3.copy_object(Bucket=s3_bucket_name, CopySource=f'{s3_bucket_name}/incoming/{file_path}',
                   Key=f'processed/{file_path}')

    # Capture loading stats in audit table
    audit_table_name = f'{table_name}_audit'
    cursor.execute(f'INSERT INTO {audit_table_name} (table_name, load_time) VALUES (%s, %s)',
                   (table_name, datetime.now()))


# Function to create Dimension Table
def create_table(table_name, columns):
    cursor = conn.cursor()
    try:
        # Check if the sequence exists
        cursor.execute(f'SHOW SEQUENCES LIKE \'{table_name}_SEQ\'')
        result = cursor.fetchone()
        if not result:
            # Create sequence if it doesn't exist
            cursor.execute(f'CREATE SEQUENCE {table_name}_seq')

        # Create table with sequence
        create_table_sql = f'''
        CREATE OR REPLACE TABLE "{table_name}" (
            id_column INT DEFAULT {table_name}_seq.NEXTVAL,
            {', '.join([f'"{col["name"]}" {col["type"]}' for col in columns])},
            PRIMARY KEY (id_column)
        )
        '''
        cursor.execute(create_table_sql)

        # If the table is stores, create store_history table
        if table_name == 'stores':
            create_store_history_table(cursor)

    except Exception as e:
        print(e)

    finally:
        cursor.close()


# Function to create store_history Table
def create_store_history_table(cursor):
    try:
        create_table_sql = '''
        CREATE OR REPLACE TABLE store_history (
            store_id INT,
            name VARCHAR(30),
            location VARCHAR(30),
            change_type VARCHAR(10),
            change_time TIMESTAMP
        )
        '''
        cursor.execute(create_table_sql)

    except Exception as e:
        print(e)


# Function to capture changes in the stores' table
def capture_store_changes():
    cursor = conn.cursor()

    try:
        # Drop the trigger if it already exists
        cursor.execute("DROP TRIGGER IF EXISTS store_change_trigger")

        # Create a trigger to capture changes in the stores table
        create_trigger_query = """
        CREATE OR REPLACE TRIGGER store_change_trigger
        AFTER INSERT OR UPDATE OR DELETE ON stores
        FOR EACH ROW
        AS
        $$
        BEGIN
            IF (TG_OP = 'INSERT' OR TG_OP = 'UPDATE') THEN
                INSERT INTO store_history (store_id, name, location, change_type, change_time)
                VALUES (NEW.store_id, NEW.name, NEW.location, TG_OP, CURRENT_TIMESTAMP);
            ELSE
                INSERT INTO store_history (store_id, name, location, change_type, change_time)
                VALUES (OLD.store_id, OLD.name, OLD.location, TG_OP, CURRENT_TIMESTAMP);
            END IF;
        END;
        $$;
        """

        # Execute the query to create the trigger
        cursor.execute(create_trigger_query)

    except Exception as e:
        print(e)

    finally:
        cursor.close()


# Function to query data based on user's region
def get_user_region_data(user_id):
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM stores WHERE user_id = %s', (user_id,))
    return cursor.fetchall()


customer_columns = [
    {"name": "customer", "type": "INT"},
    {"name": "name", "type": "VARCHAR(30)"},
    {"name": "email", "type": "VARCHAR(30)"},
    {"name": "phone", "type": "VARCHAR(30)"}
]

product_columns = [
    {"name": "product_id", "type": "INT"},
    {"name": "name", "type": "VARCHAR(30)"},
    {"name": "category", "type": "VARCHAR(30)"},
    {"name": "price", "type": "NUMBER(30,3)"}
]

transaction_columns = [
    {"name": "transaction_id", "type": "INT"},
    {"name": "customer_id", "type": "INT"},
    {"name": "product_id", "type": "INT"},
    {"name": "region_id", "type": "INT"},
    {"name": "store_id", "type": "INT"},
    {"name": "amount", "type": "NUMBER(30,3)"},
    {"name": "date", "type": "DATE"}
]

store_columns = [
    {"name": "store_id", "type": "INT"},
    {"name": "name", "type": "VARCHAR(30)"},
    {"name": "location", "type": "VARCHAR(30)"}
]

region_columns = [
    {"name": "region_id", "type": "INT"},
    {"name": "region_name", "type": "VARCHAR(30)"}
]

# Create Tables
create_table('customer', customer_columns)
create_table('products', product_columns)
create_table('regions', region_columns)
create_table('stores', store_columns)
create_table('transaction', transaction_columns)

# Load Data into Tables
load_data('customer', 'customer.csv')
load_data('products', 'products.csv')
load_data('regions', 'regions.csv')
load_data('stores', 'stores.csv')
load_data('transaction', 'transactions.csv')

# Capture Changes in Stores Table
capture_store_changes()

# Get User's Region Data
user_id = 123
user_region_data = get_user_region_data(user_id)
print(user_region_data)

# Close Snowflake Connection
conn.close()
