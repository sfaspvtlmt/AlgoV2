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


api = None
Day =None


def ConnectApi(Cred):
    f = open(str("/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Login/"+Cred["user"])+'.txt', 'r')
    usertoken = f.read()
    global api
    global Day

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

    x = datetime.now().isoweekday()
    if (x == 1):
        with open("/Users/crosshair/Documents/GitHub/AlgoV2/Variables/Monday.json") as f:
         Day = json.load(f)
    elif (x == 2):
        with open("/Users/crosshair/Documents/GitHub/AlgoV2/Variables/Tuesday.json") as f:
         Day = json.load(f)
    elif (x == 3):
        with open("/Users/crosshair/Documents/GitHub/AlgoV2/Variables/Wednesday.json") as f:
         Day = json.load(f)
    elif (x == 4):
        with open("/Users/crosshair/Documents/GitHub/AlgoV2/Variables/Thursday.json") as f:
         Day = json.load(f)
    elif (x == 5):
        with open("/Users/crosshair/Documents/GitHub/AlgoV2/Variables/Friday.json") as f:
         Day = json.load(f)


ConnectApi(Cred.Dilip)
Day = Day['Dilip2']
main.Main(Day , api)
