
import sys
sys.path.append(r"/Users/crosshair/Documents/GitHub/AlgoV2/")

from NorenRestApiPy.NorenApi import  NorenApi
import pyotp
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta as td
import Cred

            

api = None

def ConnectApi(Cred):
    global api

    try:
        class ShoonyaApiPy(NorenApi):
            def __init__(self):
                NorenApi.__init__(self, host='https://api.shoonya.com/NorenWClientTP/', websocket='wss://api.shoonya.com/NorenWSTP/', eodhost='https://api.shoonya.com/chartApi/getdata/')
                
        api = ShoonyaApiPy()
    except Exception as e:
        class ShoonyaApiPy(NorenApi):
            def __init__(self):
                NorenApi.__init__(self, host='https://api.shoonya.com/NorenWClientTP/', websocket='wss://api.shoonya.com/NorenWSTP/')
                
        api = ShoonyaApiPy()
        pass

    login_status = api.login(userid=Cred["user"], password=Cred["pwd"], twoFA=Cred["factor2"],
                             vendor_code=Cred["vc"], api_secret=Cred["app_key"], imei=Cred["imei"])
    
    #print(f"login_status = {login_status}")
    print(login_status)
    f=open("/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Login/" +str(Cred["user"])+'.txt','w')
    f.write(login_status.get('susertoken'))
    f.close()

    login_status = login_status.get('uname') + " " + login_status.get('stat') + " token = " + login_status.get('susertoken')
    print(login_status)
    


ConnectApi(Cred.MyAccount)
# ConnectApi(Cred.Sumit)
# ConnectApi(Cred.Harsh)
# ConnectApi(Cred.Sumit)
# ConnectApi(Cred.Rajshekhar)
# ConnectApi(Cred.Vijet)
# ConnectApi(Cred.Parag)
# ConnectApi(Cred.Dilip)
# ConnectApi(Cred.Riyaaz1)
# ConnectApi(Cred.Riyaaz2)
# ConnectApi(Cred.Riyaaz3)

# ConnectApi(Cred.Rishee2)
# ConnectApi(Cred.Rishee)
# ConnectApi(Cred.Rahul)
