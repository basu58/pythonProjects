from datetime import datetime, timedelta, date
from tkinter import Variable

import boto3, botocore

key_id = Variable.get("AWS_ACCESS_KEY_ID")
secret_key_id = Variable.get("AWS_SECRET_ACCESS_KEY")
bucket_name = "training-pyspark"
key = "loan_transaction/lt_dedup.parquet"


def check_file_in_s3():
    today = date.today()
    current_date = datetime.now().strftime("%Y_%m_%d")
    print(current_date)
    file = 'lbd_' + str(current_date)
    s3 = boto3.resource('s3', aws_access_key_id=key_id, aws_secret_access_key=secret_key_id)
    try:
        s3.Object(bucket_name, {file}.parquet).load()
        return True
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":  # 404 file does not found error
            # print("file does not exist")
            return False
        else:
            return f"error : {e}"


print(check_file_in_s3())
