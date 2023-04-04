from os import system
from api_helper import ShoonyaApiPy
import Variable
import time
import datetime
import Script
import Store
import Cred


def Main(Variables, Cred):
    print(Store)

    api = ShoonyaApiPy()


# make the api call
    ret = api.login(userid=Cred["user"], password=Cred["pwd"], twoFA=Cred["factor2"],
                    vendor_code=Cred["vc"], api_secret=Cred["app_key"], imei=Cred["imei"])

    system('cls')

    print(Variables["Name"])

    Script.Search(api, Variables)


Main(Variable.MyAccount, Cred.MyAccount)
