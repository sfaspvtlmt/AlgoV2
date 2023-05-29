

import sys
sys.path.append(r"C:\Users\Arush Sarna\Documents\GitHub\AlgoV2")

import Cred
from Variables import Monday
from Variables import Tuesday
from Variables import Wednesday
from Variables import Thursday
from Variables import Friday
import main

from datetime import datetime
from api_helper import ShoonyaApiPy
x = datetime.now().isoweekday()

api = ShoonyaApiPy()

Cred= Cred.Rishee
# make the api call
ret = api.login(userid=Cred["user"], password=Cred["pwd"], twoFA=Cred["factor2"],
                vendor_code=Cred["vc"], api_secret=Cred["app_key"], imei=Cred["imei"])

print(ret)
if(x==1):
    main.Main(Monday.Rishee, api)
elif(x ==2):
    main.Main(Tuesday.Rishee, api)
elif(x==3):
    main.Main(Wednesday.Rishee, api)
elif(x ==4):
    main.Main(Thursday.Rishee, api)
elif(x==5):
    main.Main(Friday.Rishee, api)

