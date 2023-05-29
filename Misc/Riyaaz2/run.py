
import sys
sys.path.append(r"C:\Users\Arush Sarna\Documents\GitHub\AlgoV2")
from api_helper import ShoonyaApiPy

from datetime import datetime
import main
from Variables import Friday
from Variables import Thursday
from Variables import Wednesday
from Variables import Tuesday
from Variables import Monday
import Cred


x = datetime.now().isoweekday()

api = ShoonyaApiPy()

Cred = Cred.Riyaaz2
# make the api call
ret = api.login(userid=Cred["user"], password=Cred["pwd"], twoFA=Cred["factor2"],
                vendor_code=Cred["vc"], api_secret=Cred["app_key"], imei=Cred["imei"])
if (x == 1):
    main.Main(Monday.Riyaaz2, api)
elif (x == 2):
    main.Main(Tuesday.Riyaaz2, api)
elif (x == 3):
    main.Main(Wednesday.Riyaaz2, api)
elif (x == 4):
    main.Main(Thursday.Riyaaz2, api)
elif (x == 5):
    main.Main(Friday.Riyaaz2, api)
