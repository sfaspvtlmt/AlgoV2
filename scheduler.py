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
    os.startfile(r'C:\Users\arush\Documents\AlgoV2\Misc\MyAccount\run.py')
    time.sleep(2)
    # os.startfile(r'C:\Users\arush\Documents\AlgoV2\Misc\MyAccount2\run.py')
    time.sleep(2)
    os.startfile(r'C:\Users\arush\Documents\AlgoV2\Misc\Rishee\run.py')
    time.sleep(2)
    os.startfile(r'C:\Users\arush\Documents\AlgoV2\Misc\Riyaaz2\run.py')
    time.sleep(2)
    os.startfile(r'C:\Users\arush\Documents\AlgoV2\Misc\Riyaaz1\run.py')
    time.sleep(2)
    os.startfile(r'C:\Users\arush\Documents\AlgoV2\Misc\Riyaaz3\run.py')
    time.sleep(2)
    os.startfile(r'C:\Users\arush\Documents\AlgoV2\Misc\Rishee2\run.py')





schedule.every().monday.at("07:09").do(start)
schedule.every().tuesday.at("09:18").do(start)
schedule.every().wednesday.at("09:18").do(start)
schedule.every().thursday.at("09:18").do(start)
schedule.every().friday.at("10:00").do(start)
# schedule.every().sunday.at("11:59").do(Thursday)

while 1:
    now = datetime.datetime.now()
    os.system('cls')
    print(now.hour, ":", now.minute, ":", now.second)
    time.sleep(1)
    schedule.run_pending()
