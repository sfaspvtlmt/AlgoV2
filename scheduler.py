import schedule
import time
from subprocess import call
import subprocess
import os
import datetime
import Variables
import Store
import Cred
# schedule task for execution of secondfile every tuesday using os.startswith()


def start():
    print("Monday ON")
  
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Login/LoginAll.py'])
    time.sleep(20)
    # subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/MyAccount/run.py'])
    # time.sleep(2)
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/MyAccount2/run.py'])
    time.sleep(2)
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Parag1/run.py'])
    time.sleep(2)
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Parag2/run.py'])
    time.sleep(2)
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Dilip1/run.py'])
    time.sleep(2)
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Dilip2/run.py'])
    time.sleep(2)
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Harsh1/run.py'])
    time.sleep(2)
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Harsh2/run.py'])
    time.sleep(2)
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Rajshekhar1/run.py'])
    time.sleep(2)
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Rajshekhar2/run.py'])
    time.sleep(2)
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Rishee/run.py'])
    time.sleep(2)
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Rishee2/run.py'])
    time.sleep(2)
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Riyaaz1/run.py'])
    time.sleep(2)
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Riyaaz2/run.py'])
    time.sleep(2)
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Riyaaz3/run.py'])
    time.sleep(2)
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Sumit1/run.py'])
    time.sleep(2)
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Sumit2/run.py'])
    time.sleep(2)
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Vijet1/run.py'])
    time.sleep(2)
    subprocess.Popen(["open", r'/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Vijet2/run.py'])
    time.sleep(2)





schedule.every().monday.at("09:18").do(start)
schedule.every().tuesday.at("09:30").do(start)
schedule.every().wednesday.at("09:30").do(start)
schedule.every().thursday.at("09:30").do(start)
schedule.every().friday.at("10:00:30").do(start)
# schedule.every().saturday.at("13:43").do(start)
# schedule.every().sunday.at("11:59").do(Thursday)
# start()
while 1:
    now = datetime.datetime.now()
    os.system('clear')
    print(now.hour, ":", now.minute, ":", now.second)
    time.sleep(1)
    schedule.run_pending()
