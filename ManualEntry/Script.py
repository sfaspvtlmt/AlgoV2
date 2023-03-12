from os import system
import math

import Store
import Execute


def Search(api, Variables):
    print(Variables["atmStrike"])
    # Search Scripts and Store them

    hedgeCE = api.searchscrip("NFO", Variables["Index"] + " " +
                              str(Variables["atmStrike"] + Variables["HedgeStrike"]) + " CE")

    Store.strike['hedgeCE'] = hedgeCE['values'][0]['tsym']
    Store.token['hedgeCE'] = hedgeCE['values'][0]['token']

    hedgePE = api.searchscrip("NFO", Variables["Index"] + " " +
                              str(Variables["atmStrike"] - Variables["HedgeStrike"]) + " PE")
    Store.strike['hedgePE'] = hedgePE['values'][0]['tsym']
    Store.token['hedgePE'] = hedgePE['values'][0]['token']

    CE = api.searchscrip("NFO", Variables["Index"] + " " + str(
        Variables["atmStrike"] + Variables["Strike"]) + " CE")
    Store.strike['CE'] = CE['values'][0]['tsym']
    Store.token['CE'] = CE['values'][0]['token']

    PE = api.searchscrip("NFO", Variables["Index"] + " " + str(
        Variables["atmStrike"] - Variables["Strike"]) + " PE")
    Store.strike['PE'] = PE['values'][0]['tsym']
    Store.token['PE'] = PE['values'][0]['token']

    # Storing Price and StopLoss

    Store.Price['CE'] = float(Variables["PriceCE"])

    Store.stopLoss['CE'] = math.ceil(
        float(Variables["PriceCE"]) * (1 + Variables["StopLoss"]/100))

    Store.Price['PE'] = float(Variables["PricePE"])
    Store.stopLoss['PE'] = math.ceil(
        float(Variables["PricePE"]) * (1 + Variables["StopLoss"]/100))
    system('cls')

    print(Store.Price)
    print(Store.stopLoss)
    Store.status1 = "Executed Straddle"
    Execute.sl(api, Variables)
