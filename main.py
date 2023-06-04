from os import system
from api_helper import ShoonyaApiPy

import time
import datetime
import Script
import Store



def Main(Variables, api):
    print(Store)

   

    while True:
        now = datetime.datetime.now()
        system('clear')
        print(Store.status)
        print(Variables["Name"])
        print(now.hour, ":", now.minute, ":", now.second)
        time.sleep(1)
        if int(now.hour) == Variables["Hour"] and int(now.minute) == Variables["Min"] and int(now.second)>= Variables["Seconds"]:
         Script.Search(api, Variables)


