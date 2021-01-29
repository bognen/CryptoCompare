# View returns all companies from Database
import pymongo
from cryptocloud.models import Coin
from cryptocloud.models import CloudContract

def get_number_of_contracts(company_id):
    result = CloudContract.objects.filter(company=company_id).count()
    return result


def get_mined_coins(company_id):
    result = ''
    count = 0
    contr = CloudContract.objects.filter(company=company_id)
    coins = contr.values_list('coin', flat=True).distinct()
    coins = coins.order_by('coin')

    for c in coins:
        coinInfo = Coin.objects.get(pk=c)
        if count == 0:
            result += coinInfo.name
        else:
            result += (", "+coinInfo.name)
        count += 1
    return result


def get_coin_price_prediction():
    result=[]
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    dbase = client["priceforecast"]
    collection = dbase["price"]

    for item in collection.find({},{ "_id": 0, "coin": 1, "prices": 1 }):
        result.append({
            "coin": item["coin"],
            "prices": item["prices"],
        })
    return result