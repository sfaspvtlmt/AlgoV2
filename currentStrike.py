
import math


def currentStrike(api , index):

    if(index =="BANKNIFTY"):
      res = api.get_quotes("NSE", "Nifty Bank")
      ltp = float(res['lp'])
      mod = int(ltp) % 100
      if mod < 50:
            atmStrike = int(math.floor(ltp/100))*100
      else:
            atmStrike = int(math.ceil(ltp/100))*100

    elif(index =="NIFTY"):   
      res = api.get_quotes("NSE", "Nifty 50")
      ltp = float(res['lp'])
      mod = int(ltp) % 50
      if mod < 25:
            atmStrike = int(math.floor(ltp/50))*50
      else:
            atmStrike = int(math.ceil(ltp/50))*50

    elif(index =="FINNIFTY"):   
      res = api.get_quotes("NSE", "Nifty Fin Service")
      ltp = float(res['lp'])
      mod = int(ltp) % 50
      if mod < 25:
            atmStrike = int(math.floor(ltp/50))*50
      else:
            atmStrike = int(math.ceil(ltp/50))*50
    
    
    return atmStrike
