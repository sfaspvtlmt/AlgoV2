

import sys
sys.path.append(r"C:\Users\arush\Documents\AlgoV2")

import Cred
from Variables import Monday
from Variables import Tuesday
from Variables import Wednesday
from Variables import Thursday
from Variables import Friday
import main

from datetime import datetime

x = datetime.now().isoweekday()

if(x==1):
    main.Main(Monday.MyAccount, Cred.MyAccount)
elif(x ==2):
    main.Main(Tuesday.MyAccount, Cred.MyAccount)
elif(x==3):
    main.Main(Wednesday.MyAccount, Cred.MyAccount)
elif(x ==4):
    main.Main(Thursday.MyAccount, Cred.MyAccount)
elif(x==5):
    main.Main(Friday.MyAccount, Cred.MyAccount)
