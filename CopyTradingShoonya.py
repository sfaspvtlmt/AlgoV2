import Store
from time import sleep
import Cred
import datetime
from api_helper import ShoonyaApiPy
import os
import json
from NorenRestApiPy.NorenApi import NorenApi


# application callbacks


def event_handler_order_update(message):
   
    print(message)
    if (message['status'] == "COMPLETE"):
        res = api2.place_order(buy_or_sell=message['trantype'], product_type=message['pcode'],
                     exchange=message['exch'], tradingsymbol=message['tsym'],
                     quantity=message["qty"], discloseqty=0, price_type='MKT', price=0,
                     trigger_price=None,
                     retention='DAY', remarks='Copied Trade')
        print(res)

def event_handler_quote_update(message):
    print(message)
def open_callback():

    print('app is connected')


# end of callbacks
api = ShoonyaApiPy()
api2 = ShoonyaApiPy()

Credentials = Cred.MyAccount
Credentials2 = Cred.MyAccount2
api2.get_limits()
# make the api call

def ConnectApi(Cred):
    f = open(str("/Users/Arush Sarna/Documents/GitHub/AlgoV2/Misc/Login/"+Cred["user"])+'.txt', 'r')
    usertoken = f.read()
   
    

    try:
        class ShoonyaApiPy(NorenApi):
            def __init__(self):
                NorenApi.__init__(self, host='https://api.shoonya.com/NorenWClientTP/',
                                  websocket='wss://api.shoonya.com/NorenWSTP/', eodhost='https://api.shoonya.com/chartApi/getdata/')

        xd = ShoonyaApiPy()
    except Exception as e:
        class ShoonyaApiPy(NorenApi):
            def __init__(self):
                NorenApi.__init__(self, host='https://api.shoonya.com/NorenWClientTP/',
                                  websocket='wss://api.shoonya.com/NorenWSTP/')

        xd = ShoonyaApiPy()
        pass
    xd.get_limits()    
    login_status = xd.set_session(
        userid=Cred["user"], password=Cred["pwd"], usertoken=usertoken)
    return xd


api  = ConnectApi(Cred.MyAccount)
api2  = ConnectApi(Cred.MyAccount2)

def sl(api):
   
    socket_opened=True

    api.start_websocket(order_update_callback=event_handler_order_update,
                       subscribe_callback=event_handler_quote_update, socket_open_callback=open_callback)

    while socket_opened:

        now = datetime.datetime.now()

        while socket_opened:
            # os.system('clear')
            # print("Running")
            sleep(1)
            break


sl(api)
