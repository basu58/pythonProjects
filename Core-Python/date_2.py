from datetime import date, datetime, timedelta

from pyarrow import timestamp

current_date = datetime.now().strftime("%Y_%m_%d")
print("current_date =", current_date)
today_file='lbd_'+str(current_date)
current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
previous_day = yesterday.strftime("%Y_%m_%d")
print(previous_day)
print(datetime.now())