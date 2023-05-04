import currentStrike
from os import system
import math
import RollingStraddle
import Store
import Execute
import time

def Search(api, Variables):
    Store.atmStrike = currentStrike.currentStrike(
        api, Variables["Index"])
    # Search Scripts and Store them
    print("HI")
    
    hedgeCE = api.searchscrip("NFO", Variables["Index"] + " " +
                              str(Store.atmStrike + Variables["HedgeStrike"]) + " CE")

    Store.strike['hedgeCE'] = hedgeCE['values'][0]['tsym']
    Store.token['hedgeCE'] = hedgeCE['values'][0]['token']

    hedgePE = api.searchscrip("NFO", Variables["Index"] + " " +
                              str(Store.atmStrike - Variables["HedgeStrike"]) + " PE")
    Store.strike['hedgePE'] = hedgePE['values'][0]['tsym']
    Store.token['hedgePE'] = hedgePE['values'][0]['token']

    CE = api.searchscrip(
        "NFO", Variables["Index"] + " " + str(Store.atmStrike + Variables["Strike"]) + " CE")
    Store.strike['CE'] = CE['values'][0]['tsym']
    Store.token['CE'] = CE['values'][0]['token']

    PE = api.searchscrip(
        "NFO", Variables["Index"] + " " + str(Store.atmStrike - Variables["Strike"]) + " PE")
    Store.strike['PE'] = PE['values'][0]['tsym']
    Store.token['PE'] = PE['values'][0]['token']

    # Storing Price and StopLoss

    res = api.get_quotes("NFO", Store.token['CE'])
    Store.Price['CE'] = float(res['lp'])

    Store.stopLoss['CE'] = math.ceil(
        float(res['lp']) * (1 + Variables["StopLoss"]/100))

    res = api.get_quotes("NFO", Store.token['PE'])
    Store.Price['PE'] = float(res['lp'])
    Store.stopLoss['PE'] = math.ceil(
        float(res['lp']) * (1 + Variables["StopLoss"]/100))
    
    res = api.place_order(buy_or_sell='B', product_type="I",
                                     exchange='NFO', tradingsymbol=Store.strike['hedgeCE'],
                                     quantity=Variables['HedgeQty'], discloseqty=0, price_type='MKT', price=0,
                                     trigger_price=None,
                                     retention='DAY', remarks='9:45 CE SELL')
    print(res)
    res = api.place_order(buy_or_sell='B', product_type="I",
                                     exchange='NFO', tradingsymbol=Store.strike['hedgePE'],
                                     quantity=Variables['HedgeQty'], discloseqty=0, price_type='MKT', price=0,
                                     trigger_price=None,
                                     retention='DAY', remarks='9:45 CE SELL')
    res = api.place_order(buy_or_sell='S', product_type="I",
                                     exchange='NFO', tradingsymbol=Store.strike['CE'],
                                     quantity=Variables['Qty'], discloseqty=0, price_type='MKT', price=0,
                                     trigger_price=None,
                                     retention='DAY', remarks='9:45 CE SELL')
    res = api.place_order(buy_or_sell='S', product_type="I",
                                     exchange='NFO', tradingsymbol=Store.strike['PE'],
                                     quantity=Variables['Qty'], discloseqty=0, price_type='MKT', price=0,
                                     trigger_price=None,
                                     retention='DAY', remarks='9:45 CE SELL')



    print(Store.Price)
    print(Store.stopLoss)
    Store.status1 = "Executed Straddle"
    RollingStraddle.sl(api, Variables)
