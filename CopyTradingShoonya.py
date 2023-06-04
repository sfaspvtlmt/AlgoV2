import Store
from time import sleep
import Cred
import datetime
from api_helper import ShoonyaApiPy
import os
import json

# application callbacks


def event_handler_order_update(message):
   
    print(message)
    if (message['status'] == "REJECTED"):
        res = api2.place_order(buy_or_sell=message['trantype'], product_type=message['pcode'],
                     exchange=message['exch'], tradingsymbol=message['tsym'],
                     quantity=message["qty"], discloseqty=0, price_type='MKT', price=0,
                     trigger_price=None,
                     retention='DAY', remarks='Copied Trade')
    

def event_handler_quote_update(message):
    print(message)
def open_callback():

    print('app is connected')


# end of callbacks
api = ShoonyaApiPy()
api2 = ShoonyaApiPy()

Credentials = Cred.MyAccount
Credentials2 = Cred.MyAccount2
# make the api call
ret = api.login(userid=Credentials["user"], password=Credentials["pwd"], twoFA=Credentials["factor2"],
                vendor_code=Credentials["vc"], api_secret=Credentials["app_key"], imei=Credentials["imei"])

api2.login(userid=Credentials2["user"], password=Credentials2["pwd"], twoFA=Credentials2["factor2"],
           vendor_code=Credentials2["vc"], api_secret=Credentials2["app_key"], imei=Credentials2["imei"])
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
