from os import system
from api_helper import ShoonyaApiPy

import time
import datetime
import Script
import Store
import rollingstraddleScript


def Main(Variables, Cred):
    print(Store)

    api = ShoonyaApiPy()


# make the api call
    ret = api.login(userid=Cred["user"], password=Cred["pwd"], twoFA=Cred["factor2"],
                    vendor_code=Cred["vc"], api_secret=Cred["app_key"], imei=Cred["imei"])

    print(ret)

    while True:
        now = datetime.datetime.now()
        system('cls')
        print(Store.status)
        print(Variables["Name"])
        print(now.hour, ":", now.minute, ":", now.second)
        time.sleep(1)
        if int(now.hour) == Variables["Hour"] and int(now.minute) == Variables["Min"] and int(now.second)>= Variables["Seconds"]:
            Script.Search(api, Variables)
        # rollingstraddleScript.Search(api, Variables)


