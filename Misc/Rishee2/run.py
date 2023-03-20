
import sys
sys.path.append(r"C:\Users\arush\Documents\AlgoV2")

from datetime import datetime
import main
from Variables import Friday
from Variables import Thursday
from Variables import Wednesday
from Variables import Tuesday
from Variables import Monday
import Cred


x = datetime.now().isoweekday()

if (x == 1):
    main.Main(Monday.Rishee2, Cred.Rishee2)
elif (x == 2):
    main.Main(Tuesday.Rishee2, Cred.Rishee2)
elif (x == 3):
    main.Main(Wednesday.Rishee2, Cred.Rishee2)
elif (x == 4):
    main.Main(Thursday.Rishee2, Cred.Rishee2)
elif (x == 5):
    main.Main(Friday.Rishee2, Cred.Rishee2)
