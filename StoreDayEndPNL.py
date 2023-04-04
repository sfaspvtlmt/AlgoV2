from os import system
from api_helper import ShoonyaApiPy
import Cred
from datetime import datetime

import pymongo
import Store


def Main( Cred):

    api = ShoonyaApiPy()


# make the api call
    name = api.login(userid=Cred["user"], password=Cred["pwd"], twoFA=Cred["factor2"],
                    vendor_code=Cred["vc"], api_secret=Cred["app_key"], imei=Cred["imei"])
    
    ret = api.get_positions()
    day_m2m =0 
    print(name)
    mtm = 0
    pnl = 0
    for i in ret:
        mtm += float(i['urmtom'])
        pnl += float(i['rpnl'])
        day_m2m = mtm + pnl
    
    if(day_m2m ==None):
        day_m2m =0
    # Connect to the MongoDB server
    client = pymongo.MongoClient(
        "mongodb+srv://arush:arush123@cluster0.my8esq9.mongodb.net/?retryWrites=true&w=majority")

    # Select the database and collection to store the data in
    my_db = client["Cult"]
    my_collection = my_db["ProfitNLoss"]
    now = datetime.now()
    search_criteria = {"ClientID": Cred['user'], "Date": "2023-03-31"
                    }

    # Define the new data to replace or insert
    limits = api.get_limits()
    print(limits)
    capital = float(limits['collateral'] if  'collateral' in limits else 0)+ float(limits['cash'])+float(limits['payin'])
    result = my_collection.find_one(
        search_criteria)
    print(result)
    new_data = {
        "ClientID": Cred['user'],
        "ClientName": name['uname'],
        "Date": now.strftime( "%Y-%m-%d"),
        "PNL": day_m2m,
        "Drawdown": 0,
        "PNLPercent": round(day_m2m/capital *100,2),
        "Capital": round(capital,2),
        "High": result['Capital']
    }
    if(day_m2m>0  and result['Drawdown']>day_m2m):
        new_data['Drawdown'] = result['Drawdown']-day_m2m
    elif (day_m2m < 0):
        new_data['Drawdown'] = result['Drawdown']-day_m2m
    
    if(new_data["Capital"]+day_m2m>result['High']):
        new_data['High']= new_data['Capital']+day_m2m

    # Use update_one() to replace or insert the data
    search_criteria = {"ClientID": Cred['user'], "Date": now.strftime("%Y-%m-%d"),
                       }
    result = my_collection.update_one(
        search_criteria, {"$set": new_data}, upsert=True)

    # Print the result of the operation
    # print("Matched count:", result.matched_count)
    # print("Modified count:", result.modified_count)
    # print("Upserted ID:", result.upserted_id)
        
Main( Cred.MyAccount)
Main( Cred.MyAccount2)
Main( Cred.Riyaaz1)
Main( Cred.Riyaaz2)
Main( Cred.Riyaaz3)
Main( Cred.Rishee)
Main( Cred.Rishee2)
