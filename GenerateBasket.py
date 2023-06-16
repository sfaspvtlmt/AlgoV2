

import Cred
from NorenRestApiPy.NorenApi import NorenApi
from kiteconnect import KiteConnect
import os
import threading
import json
from datetime import datetime
import Cred
import math

file = open("/Users/crosshair/Documents/GitHub/Algo-Zerodha/Misc/Login/" + Cred.Ankit["user_id"] + '.txt', 'r')

Cred.Ankit['access_token'] = file.read()
basket = KiteConnect(api_key=Cred.Ankit["api_key"])
basket.set_access_token(Cred.Ankit["access_token"])


Day = datetime.now().isoweekday()
Day =5
j=0

if(Day == 1):
    ltp = (basket.ltp('NSE:NIFTY FIN SERVICE')).get('NSE:NIFTY FIN SERVICE').get('last_price')
    QtySlicer =40
    INDEX = "FINNIFTY"
    month = "6"
    expiryDate = "13"
    HedgeStrike=350  
    i=0

    JSONFILE={}
    type1={
        "StopLoss":35,
        "Hour": 9,
        "Min": 19,
        "Seconds": 59,
        "Type":"NRML",
        "SLType": "Trailing"
    }
    type2={
        "StopLoss":15,
        "Hour": 9,
        "Min": 44,
        "Seconds": 59,
        "Type":"NRML",
        "SLType": "Trailing"
    }
    type3={
        "StopLoss":35,
        "Hour": 10,
        "Min": 29,
        "Seconds": 59,
        "Type":"NRML",
        "SLType": "Trailing"
    }
elif(Day==2):
    ltp = (basket.ltp('NSE:NIFTY FIN SERVICE')).get('NSE:NIFTY FIN SERVICE').get('last_price')
    QtySlicer =40
    i=0

    INDEX = "FINNIFTY"
    month = "6"
    expiryDate = "20"
    HedgeStrike=200
    JSONFILE={}
    type1={
        "StopLoss":35,
        "Hour": 9,
        "Min": 44,
        "Seconds": 59,
        "Type":"NRML",
        "SLType": "TrailToCost",
       
    }
    type2={
        "StopLoss":35,
        "Hour": 10,
        "Min": 29,
        "Seconds": 59,
        "Type":"NRML",
        "SLType": "TrailToCost",
        "Automatic":"True",
        "CEPrice":0,
        "PEPrice":0,
        "CESL":0,
        "PESL":0,
        "ATMStrike":0
    }
    type3={
        "StopLoss":35,
        "Hour": 11,
        "Min": 29,
        "Seconds": 59,
        "Type":"NRML",
        "SLType": "TrailToCost",
        "Automatic":"True",
        "CEPrice":0,
        "PEPrice":0,
        "CESL":0,
        "PESL":0,
        "ATMStrike":0
    }
elif(Day==3):
    ltp = (basket.ltp('NSE:NIFTY 50')).get('NSE:NIFTY 50').get('last_price')
    QtySlicer =50
    i=0

    INDEX = "NIFTY"
    month = "6"
    expiryDate = "15"
    HedgeStrike=300
    JSONFILE={}
    type1={
        "StopLoss":35,
        "Hour": 9,
        "Min": 44,
        "Seconds": 59,
        "Type":"MIS",
        "SLType": "TrailToCost"
    }
    type2={
        "StopLoss":35,
        "Hour": 10,
        "Min": 29,
        "Seconds": 59,
        "Type":"MIS",
        "SLType": "TrailToCost"
    }
    type3={
        "StopLoss":35,
        "Hour": 11,
        "Min": 29,
        "Seconds": 59,
        "Type":"MIS",
        "SLType": "TrailToCost"
    }
elif(Day==4):
    ltp = (basket.ltp('NSE:NIFTY 50')).get('NSE:NIFTY 50').get('last_price')
    QtySlicer =50
    i=0

    INDEX = "NIFTY"
    month = "6"
    expiryDate = "22"
    HedgeStrike=200
    JSONFILE={}
    type1={
        "StopLoss":35,
        "Hour": 9,
        "Min": 44,
        "Seconds": 59,
        "Type":"NRML",
        "SLType": "TrailToCost"
    }
    type2={
        "StopLoss":35,
        "Hour": 10,
        "Min": 29,
        "Seconds": 59,
        "Type":"NRML",
        "SLType": "TrailToCost"
    }
    type3={
        "StopLoss":35,
        "Hour": 11,
        "Min": 29,
        "Seconds": 59,
        "Type":"NRML",
        "SLType": "TrailToCost"
    }
    
elif(Day==5):
    ltp = (basket.ltp('NSE:NIFTY FIN SERVICE')).get('NSE:NIFTY FIN SERVICE').get('last_price')
    QtySlicer =40
    i=50
    j=0
    INDEX = "FINNIFTY"
    month = "6"
    expiryDate = "20"
    HedgeStrike=450
    JSONFILE={}
    type1={
        "StopLoss":30,
        "Hour": 10,
        "Min": 29,
        "Seconds": 59,
        "Type":"MIS",
        "SLType": "TrailToCost"
    }
    type2={
        "StopLoss":35,
        "Hour": 11,
        "Min": 44,
        "Seconds": 59,
        "Type":"MIS",
        "SLType": "Trailing"
    }
    type3={
        "StopLoss":30,
        "Hour": 12,
        "Min": 29,
        "Seconds": 59,
        "Type":"MIS",
        "SLType": "Trailing"
    }

mod = int(ltp) % 50
if mod < 25:
    atmStrike = int(math.floor(ltp / 50)) * 50
else:
    atmStrike = int(math.ceil(ltp / 50)) * 50
# x = datetime.now().isoweekday()
global ApiStore
ApiStore =[]
ZerodhaApiStore =[]

CapitalJSON={}
def func(Quantity , Capital , Multiplier, Name , StrikeDiff ,type  ):
    HedgeCode = INDEX + "23" + month + expiryDate + str(atmStrike - HedgeStrike) + "PE"
    peCode = INDEX + "23" + month + expiryDate + str(atmStrike-StrikeDiff) + "PE"
    Capital = Capital *Multiplier
    Qty =Quantity

    hedgeQty = Qty
    newQty = Qty
    newHedgeQty = Qty

    capital =  Capital
    requiredCapital =0
    while (newHedgeQty <=newQty*1.45 ):
        oldBasket =[
            {
                "exchange": "NFO",
                "tradingsymbol": HedgeCode,
                "transaction_type": "BUY",
                "variety": "regular",
                "product": "NRML",
                "order_type": "MARKET",
                "quantity": hedgeQty,
                "price": 0,
                "trigger_price": 0
            },
            {
                "exchange": "NFO",
                "tradingsymbol": peCode,
                "transaction_type": "SELL",
                "variety": "regular",
                "product": "NRML",
                "order_type": "MARKET",
                "quantity": Qty,
                "price": 0,
                "trigger_price": 0
            },
        ]
        newBasket = [
            {
                "exchange": "NFO",
                "tradingsymbol": HedgeCode,
                "transaction_type": "BUY",
                "variety": "regular",
                "product": "NRML",
                "order_type": "MARKET",
                "quantity": newHedgeQty,
                "price": 0,
                "trigger_price": 0
            },
            {
                "exchange": "NFO",
                "tradingsymbol": peCode,
                "transaction_type": "SELL",
                "variety": "regular",
                "product": "NRML",
                "order_type": "MARKET",
                "quantity": newQty,
                "price": 0,
                "trigger_price": 0
            },
        ]
        
        
        requiredCapital = basket.basket_order_margins(newBasket, consider_positions=True, mode=None).get('initial').get('total')
        if(requiredCapital<capital):
            Qty = newQty
            hedgeQty = newHedgeQty
            
        # print(newHedgeQty, newQty, requiredCapital)
        if(requiredCapital< capital):
            
            newQty = newQty+QtySlicer
        
        if(requiredCapital> capital):
            
            newHedgeQty = newHedgeQty+QtySlicer

    JSONFILE[Name] = {
    "Name": Name,
    "Index": INDEX,
    "Month": month,
    "ExpiryDate": expiryDate,
    "Strike": StrikeDiff,
    "HedgeStrike": HedgeStrike,
    "StopLoss": type['StopLoss'],
    "HedgeQty": hedgeQty,
    "Qty": Qty,
    "Hour": type['Hour'],
    "Min": type['Min'],
    "Seconds": type['Seconds'],
    "Type":type['Type'],
    "SLType": type['SLType'],
    "Automatic":"True",
    "CEPrice":0,
    "PEPrice":0,
    "CESL":0,
    "PESL":0,
    "ATMStrike":0
    }
    print("Best Case Scenario " + "Hedge Qty: " + str(hedgeQty) +" , Qty: " + str(Qty) + " , Margin Required: "+str( basket.basket_order_margins(oldBasket, consider_positions=True, mode=None).get('initial').get('total')) +" Capital " +str(Capital)+" "+Name)


def formatINR(number):
    number = float(number)
    number = round(number,2)
    is_negative = number < 0
    number = abs(number)
    s, *d = str(number).partition(".")
    r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
    value = "".join([r] + d)
    if is_negative:
       value = '-' + value
    return '₹ '+ value

def CreateApi(Credentials):
    api = None
    global ApiStore
# make the api call
    f = open(str("/Users/crosshair/Documents/GitHub/AlgoV2/Misc/Login/"+Credentials["user"])+'.txt', 'r')
    usertoken = f.read()

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
        userid=Credentials["user"], password=Credentials["pwd"], usertoken=usertoken)
    

   
    ApiStore.append(api)
    
    
def ZerodhaApi(Credentials):
    file = open("/Users/crosshair/Documents/GitHub/Algo-Zerodha/Misc/Login/"+Credentials["user_id"] + '.txt', 'r')

    Credentials['access_token'] = file.read()
    api = KiteConnect(api_key=Credentials["api_key"])
    api.set_access_token(Credentials["access_token"])
    # print(api.margins())
    ZerodhaApiStore.append(api)
 
CreateApi(Cred.MyAccount)
CreateApi(Cred.Joshi)
CreateApi(Cred.Rahul)
CreateApi(Cred.Sumit)
CreateApi(Cred.Harsh)
CreateApi(Cred.Sumit)
CreateApi(Cred.Rajshekhar)
CreateApi(Cred.Vijet)
CreateApi(Cred.Parag)
CreateApi(Cred.Dilip)
CreateApi(Cred.Riyaaz1)
CreateApi(Cred.Riyaaz2)
CreateApi(Cred.Riyaaz3)
CreateApi(Cred.Rishee)
CreateApi(Cred.Rishee2)
CreateApi(Cred.MyAccount)
ZerodhaApi(Cred.Ankit)
ZerodhaApi(Cred.Manjunath)
ZerodhaApi(Cred.Sanam)
ZerodhaApi(Cred.Milan)
ZerodhaApi(Cred.Nirmal)

def CapitalZerodha(api):
        capital = api.margins()
        # print(capital)
        capital = (capital.get("equity").get("available").get("cash") + (capital).get("equity").get("available").get("collateral"))
        return capital

def CapitalShoonya(api):
    
    limits = api.get_limits()
  
    capital = float(limits['collateral'] if  'collateral' in limits else 0)+ float(limits['cash'])+float(limits['payin'])
    return capital

shoonyaCapital =0
zerodhaCapital =0

# for api in ZerodhaApiStore:
#         # print(api.margins())
#         print()
# #    zerodhaCapital = zerodhaCapital+ CapitalZerodha(api)
   
# for api in ApiStore:
#     print()
# #    shoonyaCapital = shoonyaCapital+ CapitalShoonya(api)

def funcShoonya(k):
         Capital = CapitalShoonya(ApiStore[k])
         ret = ApiStore[k].get_positions()
         UID = ApiStore[k].get_limits()
         day_m2m =0 
         mtm = 0
         pnl = 0
         if(ret != None):
           for i in ret:
             mtm += float(i['urmtom'])
             pnl += float(i['rpnl'])
             day_m2m = mtm + pnl
         else :
             
          if(day_m2m ==None):
               day_m2m =0
        #  print(int((Capital + day_m2m)/1000)*1000, ret[0]['uid'])
         CapitalJSON[UID['uid']] = int((Capital + day_m2m)/1000)*1000

def funcZerodha(api):
         positions = api.positions() 
         Capital = CapitalZerodha(api)
         profile =api.profile()['user_id']
        #  UID = positions[0]['uid']
         net =positions.get("net")
         day =positions.get("day")
         i=0

         day_m2m=0
         while(i<len(net)):
          day_m2m += net[i].get("pnl")
          i=i+1
         while(i<len(day)):
          day_m2m += day[i].get("pnl")
          i=i+1
        #  print(int((Capital + day_m2m)/1000)*1000,profile )
         CapitalJSON[profile] = int((Capital + day_m2m)/1000)*1000

       

k=0
AllThreads =[]
while (k<len(ApiStore)):
        thread = threading.Thread(target = funcShoonya , args=[k])
        AllThreads.append(thread)
        k= k+1
for api in ZerodhaApiStore:
    thread = threading.Thread(target=funcZerodha, args =[api])
    AllThreads.append(thread)

for thread in AllThreads:
    
    thread.start()
for thread in AllThreads:
    
    thread.join()
    
out_file = open("/Users/crosshair/Documents/GitHub/Algo-Zerodha/Variables/Capital.json", "w")

json.dump(CapitalJSON, out_file, indent = 6)



out_file = open("/Users/crosshair/Documents/GitHub/AlgoV2/Variables/Capital.json", "w")

json.dump(CapitalJSON, out_file, indent = 6)

# # Sanam
t27 = threading.Thread(target = func , args=[0, CapitalJSON[Cred.Sanam['user_id']], 0.47, "Sanam1", j ,type1 ])
t1 = threading.Thread(target = func , args=[0, CapitalJSON[Cred.Sanam['user_id']], 0.47, "Sanam2", i ,type2 ])
t2 = threading.Thread(target = func , args=[600, CapitalJSON[Cred.Riyaaz1['user']], 0.91, "Riyaaz1",j,type1 ])
t3 = threading.Thread(target = func , args=[600, CapitalJSON[Cred.Riyaaz2['user']], 0.91, "Riyaaz2", i ,type2 ])
t4 = threading.Thread(target = func , args=[200, CapitalJSON[Cred.Riyaaz3['user']], 0.91, "Riyaaz3", j ,type3 ])
t5 = threading.Thread(target = func , args=[0, CapitalJSON[Cred.MyAccount['user']], 0.45, "MyAccount", j ,type1 ])
t6 = threading.Thread(target = func , args=[0, CapitalJSON[Cred.MyAccount['user']], 0.45, "MyAccount2", i ,type2 ])
t7 = threading.Thread(target = func , args=[200, CapitalJSON[Cred.Parag['user']], 0.45, "Parag1", j ,type1 ])
t8 = threading.Thread(target = func , args=[200, CapitalJSON[Cred.Parag['user']], 0.45, "Parag2", i ,type2 ])
t9 = threading.Thread(target = func , args=[200, CapitalJSON[Cred.Dilip['user']], 0.45, "Dilip1",j,type1 ])
t10 = threading.Thread(target = func , args=[200, CapitalJSON[Cred.Dilip['user']], 0.45, "Dilip2", i,type2 ])
t11= threading.Thread(target = func , args=[800, CapitalJSON[Cred.Vijet['user']], 0.45, "Vijet1", j ,type1 ])
t12 = threading.Thread(target = func , args=[800, CapitalJSON[Cred.Vijet['user']], 0.45, "Vijet2", i ,type2 ])
t13= threading.Thread(target = func , args=[800, CapitalJSON[Cred.Rajshekhar['user']], 0.45, "Rajshekhar1", j ,type1 ])
t14= threading.Thread(target = func , args=[800, CapitalJSON[Cred.Rajshekhar['user']], 0.45, "Rajshekhar2", i ,type2 ])
t15= threading.Thread(target = func , args=[0, CapitalJSON[Cred.Sumit['user']], 0.45, "Sumit1",j,type1 ])
t16= threading.Thread(target = func , args=[0, CapitalJSON[Cred.Sumit['user']], 0.45, "Sumit2", i,type2 ])
t17= threading.Thread(target = func , args=[200, CapitalJSON[Cred.Rishee['user']], 0.91, "Rishee1", j,type1 ])
t18= threading.Thread(target = func , args=[200, CapitalJSON[Cred.Rishee2['user']], 0.91, "Rishee2", i ,type2 ])
t19= threading.Thread(target = func , args=[600, CapitalJSON[Cred.Ankit['user_id']], 0.47, "Ankit1",j,type1 ])
t20= threading.Thread(target = func , args=[600, CapitalJSON[Cred.Ankit['user_id']], 0.47, "Ankit2", i ,type2 ])
t21= threading.Thread(target = func , args=[600, CapitalJSON[Cred.Harsh['user']], 0.45, "Harsh1", j,type1 ])
t22= threading.Thread(target = func , args=[600, CapitalJSON[Cred.Harsh['user']], 0.45, "Harsh2", i ,type2 ])
t23= threading.Thread(target = func , args=[400, CapitalJSON[Cred.Milan['user_id']], 0.47, "Milan1", j,type1 ])
t24= threading.Thread(target = func , args=[400, CapitalJSON[Cred.Milan['user_id']], 0.47, "Milan2", i ,type2 ])
t25= threading.Thread(target = func , args=[400, CapitalJSON[Cred.Nirmal['user_id']], 0.47, "Nirmal1", j ,type1 ])
t26= threading.Thread(target = func , args=[400, CapitalJSON[Cred.Nirmal['user_id']], 0.47, "Nirmal2", i ,type2 ])
t28= threading.Thread(target = func , args=[400, CapitalJSON[Cred.Manjunath['user_id']], 0.47, "Manjunath1",j,type1 ])
t29= threading.Thread(target = func , args=[400, CapitalJSON[Cred.Manjunath['user_id']], 0.47, "Manjunath2", i ,type2 ])
t30= threading.Thread(target = func , args=[0, CapitalJSON[Cred.Rahul['user']], 0.45, "Rahul1",j,type1 ])
t31= threading.Thread(target = func , args=[0, CapitalJSON[Cred.Rahul['user']], 0.45, "Rahul2", i ,type2 ])
t32= threading.Thread(target = func , args=[400, CapitalJSON[Cred.Joshi['user']], 0.45, "Joshi1",j,type1 ])
t33= threading.Thread(target = func , args=[400, CapitalJSON[Cred.Joshi['user']], 0.45, "Joshi2", i ,type2 ])



t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
t13.start()
t14.start()
t15.start()
t16.start()
t17.start()
t18.start()
t19.start()
t20.start()
t21.start()
t22.start()
t23.start()
t24.start()
t25.start()
t26.start()
t27.start()
t28.start()
t29.start()
t30.start()
t31.start()
t32.start()
t33.start()






t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
t11.join()
t12.join()
t13.join()
t14.join()
t15.join()
t16.join()
t17.join()
t18.join()
t19.join()
t20.join()
t21.join()
t22.join()
t23.join()
t24.join()
t25.join()
t28.join()
t29.join()
t30.join()
t31.join()
t32.join()
t33.join()










if(Day == 1):
    out_file = open("/Users/crosshair/Documents/GitHub/Algo-Zerodha/Variables/Monday.json", "w")

    json.dump(JSONFILE, out_file, indent = 6)



    out_file = open("/Users/crosshair/Documents/GitHub/AlgoV2/Variables/Monday.json", "w")

    json.dump(JSONFILE, out_file, indent = 6)
if(Day == 2):
    out_file = open("/Users/crosshair/Documents/GitHub/Algo-Zerodha/Variables/Tuesday.json", "w")

    json.dump(JSONFILE, out_file, indent = 6)



    out_file = open("/Users/crosshair/Documents/GitHub/AlgoV2/Variables/Tuesday.json", "w")

    json.dump(JSONFILE, out_file, indent = 6)
if(Day == 3):
    out_file = open("/Users/crosshair/Documents/GitHub/Algo-Zerodha/Variables/Wednesday.json", "w")

    json.dump(JSONFILE, out_file, indent = 6)



    out_file = open("/Users/crosshair/Documents/GitHub/AlgoV2/Variables/Wednesday.json", "w")

    json.dump(JSONFILE, out_file, indent = 6)
if(Day == 4):
    out_file = open("/Users/crosshair/Documents/GitHub/Algo-Zerodha/Variables/Thursday.json", "w")

    json.dump(JSONFILE, out_file, indent = 6)



    out_file = open("/Users/crosshair/Documents/GitHub/AlgoV2/Variables/Thursday.json", "w")

    json.dump(JSONFILE, out_file, indent = 6)
if(Day == 5):
    out_file = open("/Users/crosshair/Documents/GitHub/Algo-Zerodha/Variables/Friday.json", "w")

    json.dump(JSONFILE, out_file, indent = 6)



    out_file = open("/Users/crosshair/Documents/GitHub/AlgoV2/Variables/Friday.json", "w")

    json.dump(JSONFILE, out_file, indent = 6)



Qty=0  
for i in JSONFILE:
  Qty += JSONFILE[i]['Qty']
  
print(Qty*2)
Qty=0  
for i in JSONFILE:
  Qty += JSONFILE[i]['HedgeQty']
  
print(Qty*2)



