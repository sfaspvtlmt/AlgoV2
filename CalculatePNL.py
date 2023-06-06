

import Cred
from NorenRestApiPy.NorenApi import NorenApi
from kiteconnect import KiteConnect
import os

# x = datetime.now().isoweekday()
global ApiStore
ApiStore =[]
ZerodhaApiStore =[]



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
    ZerodhaApiStore.append(api)
 
CreateApi(Cred.MyAccount)
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
    # print(limits)
    
    capital = float(limits['collateral'] if  'collateral' in limits else 0)+ float(limits['cash'])+float(limits['payin'])
    return capital

shoonyaCapital =0
zerodhaCapital =0

for api in ZerodhaApiStore:
        # print(api.margins())
        # print()
   zerodhaCapital = zerodhaCapital+ CapitalZerodha(api)
   
for api in ApiStore:
   shoonyaCapital = shoonyaCapital+ CapitalShoonya(api)


while(True):
    PNL =0
    k  =0 
    j=0
    
    while (k<len(ApiStore)):
         ret = ApiStore[k].get_positions()
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
         PNL = PNL+day_m2m
        #  print("Day M2M:",day_m2m)

         k= k+1
         
    while(j< len(ZerodhaApiStore)):
         positions = ZerodhaApiStore[j].positions() 
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
         PNL = PNL + day_m2m
         j = j+1
        
    os.system('clear')  
    # print(locale.currency(100.52, grouping=True))

    print("PNL: ",formatINR(PNL*2) , "Capital: ", formatINR((shoonyaCapital + zerodhaCapital)*2) ,round(PNL/(shoonyaCapital + zerodhaCapital)*100,2) ," %")
        
        
    
    
    

