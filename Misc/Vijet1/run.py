import sys
sys.path.append(r"C:\Users\arush\Documents\AlgoV2")
from Variables import Monday
import time
from NorenRestApiPy.NorenApi import NorenApi
import Cred
import pandas as pd
import datetime
import json
from datetime import datetime
import main
from Variables import Friday
from Variables import Thursday
from Variables import Wednesday
from Variables import Tuesday


# update the user token generated during first script execution

api = None


def ConnectApi(Cred):
    f = open(str("Misc/Login/"+Cred["user"])+'.txt', 'r')
    usertoken = f.read()
    global api

    try:
        class ShoonyaApiPy(NorenApi):
            def __init__(self):
                NorenApi.__init__(self, host='https://api.shoonya.com/NorenWClientTP/',
                                  websocket='wss://api.shoonya.com/NorenWSTP/', eodhost='https://api.shoonya.com/chartApi/getdata/')

        api = ShoonyaApiPy()
    except Exception as e:
        class ShoonyaApiPy(NorenApi):
            def __init__(self):
                NorenApi.__init__(self, host='https://api.shoonya.com/NorenWClientTP/',
                                  websocket='wss://api.shoonya.com/NorenWSTP/')

        api = ShoonyaApiPy()
        pass

    login_status = api.set_session(
        userid=Cred["user"], password=Cred["pwd"], usertoken=usertoken)

    print(api.get_limits())
    x = datetime.now().isoweekday()

    if (x == 1):
        main.Main(Monday.Vijet1, api)
    elif (x == 2):
        main.Main(Tuesday.Vijet1, api)
    elif (x == 3):
        main.Main(Wednesday.Vijet1, api)
    elif (x == 4):
        main.Main(Thursday.Vijet1, api)
    elif (x == 5):
        main.Main(Friday.Vijet1, api)


ConnectApi(Cred.Vijet)
