import Store

from time import sleep


import datetime
from api_helper import ShoonyaApiPy
import os


# application callbacks


def event_handler_order_update(message):
    print("order event: " + str(message))


def event_handler_quote_update(message):
    global lastWebsocketTime
    lastWebsocketTime= datetime.datetime.now().strftime("%H:%M:%S")
    # print(lastWebsocketTime)

    if (Var["Type"] == "MIS"):
        Type = "I"
    else:
        Type = "M"

    if ('lp' in message):
        print(message['lp'])

    if ((Store.status1 == "Executed Straddle" or Store.status1 == "PE SL HIT") and Var["SLType"] == "Trailing" and 'lp' in message and message['tk'] == Store.token['CE'] and float(message['lp']) <= Store.Price['CE']-10):
        print("Trailing CE SL")
        Store.Price["CE"] = Store.Price["CE"]-10
        Store.stopLoss["CE"] = Store.stopLoss["CE"]-7
        SlQty = Var["Qty"]

        if (Store.status1 == "PE SL HIT"):
            while (SlQty > maxQty):
                xd.modify_order(exchange='NFO', tradingsymbol=Store.strike['CE'], orderno=Store.orderno1['CE'],
                                newquantity=maxQty, newprice_type='SL-LMT', newprice=Store.stopLoss['CE']+4,
                                newtrigger_price=Store.stopLoss['CE'])
                SlQty = SlQty-maxQty

            if (SlQty > 0):
                xd.modify_order(exchange='NFO', tradingsymbol=Store.strike['CE'], orderno=Store.orderno1['CE'],
                                newquantity=SlQty, newprice_type='SL-LMT', newprice=Store.stopLoss['CE']+4,
                                newtrigger_price=Store.stopLoss['CE'])

    if ((Store.status1 == "Executed Straddle" or Store.status1 == "CE SL HIT") and Var["SLType"] == "Trailing" and 'lp' in message and message['tk'] == Store.token['PE'] and float(message['lp']) <= Store.Price['PE']-10):
        Store.Price["PE"] = Store.Price["PE"]-10
        Store.stopLoss["PE"] = Store.stopLoss["PE"]-7
        SlQty = Var["Qty"]

        while (SlQty > maxQty):

            if (Store.status1 == "CE SL HIT"):
                xd.modify_order(exchange='NFO', tradingsymbol=Store.strike['PE'], orderno=Store.orderno1['PE'],
                                newquantity=maxQty, newprice_type='SL-LMT', newprice=Store.stopLoss['PE']+4,
                                newtrigger_price=Store.stopLoss['PE'])
                SlQty = SlQty-maxQty
                if (SlQty > 0):
                    xd.modify_order(exchange='NFO', tradingsymbol=Store.strike['PE'], orderno=Store.orderno1['PE'],
                                    newquantity=SlQty, newprice_type='SL-LMT', newprice=Store.stopLoss['PE']+4,
                                    newtrigger_price=Store.stopLoss['PE'])
        print("Trailing PE SL")

    if (Store.status1 == "Executed Straddle" and 'lp' in message and message['tk'] == Store.token['CE'] and float(message['lp']) >= Store.stopLoss['CE']):

        if (Var["SLType"] == "TrailToCost"):
            Store.stopLoss = Store.Price

        # print("CE: ", message['lp'])
        print(message['lp'])
        print("CE sl Hit")
        if (Store.status == "PE SL HIT"):
            Store.status1 = False

        else:
            SlQty = Var["Qty"]
            while (Var["HedgeQty"] > maxQty):

                res = xd.place_order(buy_or_sell='B', product_type=Type,
                                     exchange='NFO', tradingsymbol=Store.strike['hedgePE'],
                                     quantity=maxQty, discloseqty=0, price_type='MKT', price=0,
                                     trigger_price=None,
                                     retention='DAY', remarks='9:45 Hedge PE BUY')
                Var["HedgeQty"] = Var["HedgeQty"]-maxQty

            if (Var["HedgeQty"] > 0):
                res = xd.place_order(buy_or_sell='B', product_type=Type,
                                     exchange='NFO', tradingsymbol=Store.strike['hedgePE'],
                                     quantity=Var["HedgeQty"], discloseqty=0, price_type='MKT', price=0,
                                     trigger_price=None,
                                     retention='DAY', remarks='9:45 Hedge PE BUY')

            while (SlQty > maxQty):
                res = xd.place_order(buy_or_sell='S', product_type=Type,
                                     exchange='NFO', tradingsymbol=Store.strike['PE'],
                                     quantity=maxQty, discloseqty=0, price_type='MKT', price=0,
                                     trigger_price=None,
                                     retention='DAY', remarks='9:45 PE SELL')
                SlQty = SlQty-maxQty

            if (SlQty > 200):
                res = xd.place_order(buy_or_sell='S', product_type=Type,
                                     exchange='NFO', tradingsymbol=Store.strike['PE'],
                                     quantity=SlQty-200, discloseqty=0, price_type='MKT', price=0,
                                     trigger_price=None,
                                     retention='DAY', remarks='9:45 PE SELL')
                SlQty = 200
            while (SlQty > 0):

                res = xd.place_order(buy_or_sell='S', product_type=Type,
                                     exchange='NFO', tradingsymbol=Store.strike['PE'],
                                     quantity=minQty, discloseqty=0, price_type='MKT', price=0,
                                     trigger_price=None,
                                     retention='DAY', remarks='9:45 PE SELL')
                SlQty = SlQty-minQty
            SlQty = Var["Qty"]
            while (SlQty > maxQty):
                res = xd.place_order(buy_or_sell='B', product_type=Type,
                                     exchange='NFO', tradingsymbol=Store.strike['PE'],
                                     quantity=maxQty, discloseqty=0, price_type='SL-LMT', price=Store.stopLoss['PE']+6,
                                     trigger_price=Store.stopLoss['PE'],
                                     retention='DAY', remarks='9:45 PE SL')
                SlQty = SlQty-maxQty
            if (SlQty > 200):

                res = xd.place_order(buy_or_sell='B', product_type=Type,
                                     exchange='NFO', tradingsymbol=Store.strike['PE'],
                                     quantity=SlQty-200, discloseqty=0, price_type='SL-LMT', price=Store.stopLoss['PE']+6,
                                     trigger_price=Store.stopLoss['PE'],
                                     retention='DAY', remarks='9:45 PE SL')
                SlQty = 200
            while (SlQty > 0):

                res = xd.place_order(buy_or_sell='B', product_type=Type,
                                     exchange='NFO', tradingsymbol=Store.strike['PE'],
                                     quantity=minQty, discloseqty=0, price_type='SL-LMT', price=Store.stopLoss['PE']+6,
                                     trigger_price=Store.stopLoss['PE'],
                                     retention='DAY', remarks='9:45 PE SL')
                SlQty = SlQty - minQty

            Store.status1 = "CE SL HIT"
            Store.status = "CE SL HIT"

    if (Store.status1 == "Executed Straddle" and 'lp' in message and message['tk'] == Store.token['PE'] and float(message['lp']) >= Store.stopLoss['PE']):
        # print("PE: ", message['lp'])
        print("PE sl Hit")
        if (Var["SLType"] == "TrailToCost"):
            Store.stopLoss = Store.Price

        print(message['lp'])
        if (Store.status == "CE SL HIT"):
            Store.status1 = False

        else:
            SlQty = Var["Qty"]
            while (Var["HedgeQty"] > maxQty):

                res = xd.place_order(buy_or_sell='B', product_type=Type,
                                     exchange='NFO', tradingsymbol=Store.strike['hedgeCE'],
                                     quantity=maxQty, discloseqty=0, price_type='MKT', price=0,
                                     trigger_price=None,
                                     retention='DAY', remarks='9:45 Hedge CE BUY')
                Var["HedgeQty"] = Var["HedgeQty"]-maxQty

            if (Var["HedgeQty"] > 0):
                res = xd.place_order(buy_or_sell='B', product_type=Type,
                                     exchange='NFO', tradingsymbol=Store.strike['hedgeCE'],
                                     quantity=Var["HedgeQty"], discloseqty=0, price_type='MKT', price=0,
                                     trigger_price=None,
                                     retention='DAY', remarks='9:45 Hedge CE BUY')

            while (SlQty > maxQty):
                res = xd.place_order(buy_or_sell='S', product_type=Type,
                                     exchange='NFO', tradingsymbol=Store.strike['CE'],
                                     quantity=maxQty, discloseqty=0, price_type='MKT', price=0,
                                     trigger_price=None,
                                     retention='DAY', remarks='9:45 CE SELL')
                SlQty = SlQty-maxQty

            if (SlQty > 200):
                res = xd.place_order(buy_or_sell='S', product_type=Type,
                                     exchange='NFO', tradingsymbol=Store.strike['CE'],
                                     quantity=SlQty-200, discloseqty=0, price_type='MKT', price=0,
                                     trigger_price=None,
                                     retention='DAY', remarks='9:45 CE SELL')
                SlQty = 200
            while (SlQty > 0):
                res = xd.place_order(buy_or_sell='S', product_type=Type,
                                     exchange='NFO', tradingsymbol=Store.strike['CE'],
                                     quantity=minQty, discloseqty=0, price_type='MKT', price=0,
                                     trigger_price=None,
                                     retention='DAY', remarks='9:45 CE SELL')
                SlQty = SlQty-minQty

            SlQty = Var["Qty"]
            while (SlQty > maxQty):
                res = xd.place_order(buy_or_sell='B', product_type=Type,
                                     exchange='NFO', tradingsymbol=Store.strike['CE'],
                                     quantity=maxQty, discloseqty=0, price_type='SL-LMT', price=Store.stopLoss['CE']+6,
                                     trigger_price=Store.stopLoss['CE'],
                                     retention='DAY', remarks='9:45 CE SL')
                SlQty = SlQty-maxQty
            if (SlQty > 200):

                res = xd.place_order(buy_or_sell='B', product_type=Type,
                                     exchange='NFO', tradingsymbol=Store.strike['CE'],
                                     quantity=SlQty-200, discloseqty=0, price_type='SL-LMT', price=Store.stopLoss['CE']+6,
                                     trigger_price=Store.stopLoss['CE'],
                                     retention='DAY', remarks='9:45 CE SL')
                SlQty = 200
            while (SlQty > 0):

                res = xd.place_order(buy_or_sell='B', product_type=Type,
                                     exchange='NFO', tradingsymbol=Store.strike['CE'],
                                     quantity=minQty, discloseqty=0, price_type='SL-LMT', price=Store.stopLoss['CE']+6,
                                     trigger_price=Store.stopLoss['CE'],
                                     retention='DAY', remarks='9:45 CE SL')
                SlQty = SlQty - minQty
        Store.status1 = "PE SL HIT"
        Store.status = "PE SL HIT"


def open_callback():
    socket_opened = True
    global lastWebsocketTime
    lastWebsocketTime= datetime.datetime.now().strftime("%H:%M:%S")

    print('app is connected')

    xd.subscribe(["NFO|"+Store.token['CE'], "NFO|"+Store.token['PE']])

# end of callbacks


def sl(api, Variables):
    global lastWebsocketTime
    lastWebsocketTime= datetime.datetime.now().strftime("%H:%M:%S")

    
    global Var
    Var = Variables
    global socket_opened
    socket_opened = True
    global xd
    xd = api
    global minQty
    global maxQty
    if (Var["Index"] == "BANKNIFTY"):
        minQty = 25
        maxQty = 1200
    if (Var["Index"] == "FINNIFTY"):
        minQty = 40
        maxQty = 1800

    if (Var["Index"] == "NIFTY"):
        minQty = 50
        maxQty = 1800

    print(Store.token)

    xd.start_websocket(order_update_callback=event_handler_order_update,
                       subscribe_callback=event_handler_quote_update, socket_open_callback=open_callback)

    while socket_opened:
        

        now = datetime.datetime.now()
        # lastWebsocketTime= datetime.datetime.now().strftime("%H:%M:%S")
        currentTime = now.strftime("%H:%M:%S")
        # print(currentTime)
        # print(lastWebsocketTime)
        t2 = datetime.datetime.strptime(currentTime, "%H:%M:%S")
        t1 = datetime.datetime.strptime(lastWebsocketTime, "%H:%M:%S")
        delta = t2 - t1
       


        while socket_opened:
            os.system('clear')
            if(delta.total_seconds()>5):
                print("Dead")
                # xd.unsubscribe(["NFO|"+Store.token['CE'], "NFO|"+Store.token['PE']])
                
                # xd.subscribe(["NFO|"+Store.token['CE'], "NFO|"+Store.token['PE']])
                xd.close_websocket()
                sleep(2)
                xd.start_websocket(order_update_callback=event_handler_order_update,
                       subscribe_callback=event_handler_quote_update, socket_open_callback=open_callback)
                
                
            print(delta.total_seconds())

            print(Variables["Name"])
            print(now.hour, ":", now.minute, ":", now.second)
            print(Store.status)
            print(Store.atmStrike)
            print(Var["Index"])
            print("StopLoss:", Store.stopLoss)
            print("Price:", Store.Price)
            sleep(1)
            break
