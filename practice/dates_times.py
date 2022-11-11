import datetime
from datetime import time
import time

print(datetime.datetime.now())
print(time.time())
ct = time.time()
print(time.ctime(ct))
print('tread start...')
# time.sleep(5)
print('thread end...')
print(datetime.datetime.now().day)
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().strftime('%A'))
print(datetime.datetime(2020, 5, 5).strftime('%a'))
print(datetime.datetime(2020, 5, 5).strftime('%A'))
print(datetime.datetime(2020, 5, 5).strftime('%d'))
print(datetime.datetime(2020, 6, 5).strftime('%b'))
print(datetime.datetime(2020, 6, 6).strftime('%B'))
print(datetime.datetime(2020, 5, 5).strftime('%c'))
print(datetime.datetime(2120, 5, 5).strftime('%C'))


