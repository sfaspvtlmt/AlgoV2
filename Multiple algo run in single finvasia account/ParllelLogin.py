import sys
sys.path.append(r"C:\Users\Arush Sarna\Documents\GitHub\AlgoV2")
import Cred
from NorenRestApiPy.NorenApi import  NorenApi
import json
import datetime
import pandas as pd
import time
   
 
 

#update the user token generated during first script execution
usertoken = '46f53b0d9f5993c6f003c27f5ba7e219d28cd510b54ca6a9fe8196b666aa399e'

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

    login_status = api.set_session(
        userid=Cred["user"], password=Cred["pwd"], usertoken=usertoken)
    print(api.get_limits())


# ConnectApi(Cred.MyAccount)
ConnectApi(Cred.Harsh)
