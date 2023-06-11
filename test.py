from datetime import datetime
import time
# start time
now = datetime.now()
now = now.strftime("%H:%M:%S")


# convert time string to datetime
t1 = datetime.strptime(now, "%H:%M:%S")
print('Start time:', t1.time())
time.sleep(2)
now = datetime.now()
now = now.strftime("%H:%M:%S")
t2 = datetime.strptime(now, "%H:%M:%S")
print('End time:', t2.time())

# get difference
delta = t2 - t1

# time difference in seconds
print(2==delta.total_seconds())

# time difference in milliseconds
ms = delta.total_seconds() * 1000
print(f"Time difference is {ms} milliseconds")
