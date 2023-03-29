from os import system
from api_helper import ShoonyaApiPy
import Cred
import datetime

import Store


def Main( Cred):

    api = ShoonyaApiPy()


# make the api call
    ret = api.login(userid=Cred["user"], password=Cred["pwd"], twoFA=Cred["factor2"],
                    vendor_code=Cred["vc"], api_secret=Cred["app_key"], imei=Cred["imei"])

  
    print(ret)
    
Main( Cred.MyAccount2)
