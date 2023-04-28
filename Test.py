 

from os import system
from api_helper import ShoonyaApiPy
import Cred
from datetime import datetime

import pymongo
import Store


def Main(Cred):

    api = ShoonyaApiPy()


# make the api call
    Cred = Cred.Rajshekhar
    print(Cred)
    name = api.login(userid=Cred["user"], password=Cred["pwd"], twoFA=Cred["factor2"],
                     vendor_code=Cred["vc"], api_secret=Cred["app_key"], imei=Cred["imei"])

    ret = api.get_positions()
    print(ret)

Main(Cred)