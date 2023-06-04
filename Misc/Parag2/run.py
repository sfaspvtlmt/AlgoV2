import sys
sys.path.append(r"/Users/crosshair/Documents/GitHub/AlgoV2/")
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
    f = open(str("/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Login/"+Cred["user"])+'.txt', 'r')
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
        main.Main(Monday.Parag2, api)
    elif (x == 2):
        main.Main(Tuesday.Parag2, api)
    elif (x == 3):
        main.Main(Wednesday.Parag2, api)
    elif (x == 4):
        main.Main(Thursday.Parag2, api)
    elif (x == 5):
        main.Main(Friday.Parag2, api)


ConnectApi(Cred.Parag)
