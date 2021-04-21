import requests

from pymongo import MongoClient


#Step 1: Connect to MongoDB - Note: Change connection string as needed

client = MongoClient("mongodb+srv://Aryman:Demo1234@cluster0.1y4le.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client.project

myreqest = requests.get("https://api.twelvedata.com/time_series?symbol=AAPL,EUR/USD,ETH/BTC:Huobi,RY:TSX&interval=1min&apikey=71591a285e17485aa0dc839fc4f51c8c")

if myreqest.status_code == 200:
    currency = myreqest.json()
    result = db.universal.insert_one(currency)
    print(currency)