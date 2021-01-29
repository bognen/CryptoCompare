import json
import random

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from bson import ObjectId

# Models and Serializers
from cryptocloud.models import CloudCompany
from cryptocloud.models import Coin
from cryptocloud.models import CloudContract
from cryptocloud.serializers import ContractSerializer
from cryptocloud.serializers import ContractSimpleSerializer

# Servcices
from cryptocloud.services import get_number_of_contracts
from cryptocloud.services import get_mined_coins
from cryptocloud.services import get_coin_price_prediction


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,ObjectId):
            return str(o)
        return json.JSONEncoder.default(self,o)

def all_companies(request):
    result = []
    companies = CloudCompany.objects.all()
    for comp in companies:
        result.append({
            "id" : str(comp._id),
            "title": comp.title,
            "location": comp.location,
            "founded": comp.founded,
            "image": comp.image,
            "website": comp.website,
            "legitimacy": comp.legitimacy,
            "num_of_contracts": get_number_of_contracts(comp._id),
            "description": comp.description
        })

    return JsonResponse(result, safe=False)


def all_coins(request):
    coins = Coin.objects.all()
    # serializer = CoinSerializer(coins, many=True)
    # return JsonResponse(serializer.data)
    result = []
    for c in coins:
        result.append({
            "id": str(c._id),
            "name": c.name,
            "token": c.token,
            "image": c.image,
            "algorithm": c.algorithm,
            "website": c.website,
            "description": c.description,
            "max_supply": c.maxSupply,
            "start_date": c.startDate,
            "coinGecko": c.coinGecko
        })

    return JsonResponse(result, safe=False)


def get_company(request, company_id):
    company = CloudCompany.objects.get(pk=company_id)
    result = {
        "_id": str(company._id),
        "title": company.title,
        'location': company.location,
        "founded": company.founded,
        "image": company.image,
        "website": company.website,
        "legitimacy": company.legitimacy,
        "description": company.description,
        "coins": get_mined_coins(company_id),
        "num_of_contracts": get_number_of_contracts(company_id)
    }
    return JsonResponse(result, safe=False)
    # serializer = CloudCompanySerializer(company)
    # return JsonResponse(serializer.data)


def get_contract(request, contract_id):

    # If contract ID is not provided just return dummy Json object
    if contract_id == 'undefined':
        response = {"result": "Emplty request"}
        return JsonResponse(response, safe=False)
    contract = CloudContract.objects.get(pk=contract_id)
    serializer = ContractSerializer(contract)
    return JsonResponse(JSONEncoder().encode(serializer.data), safe=False)


def get_contract_by_company(request, comp_id):
    response = []
    contr = CloudContract.objects.filter(company=comp_id)
    coins = contr.values_list('coin', flat=True).distinct()
    coins = coins.order_by('coin')

    for c in coins:

        # seletc thew hole info on contracts with given company and coin
        contrByCoin = CloudContract.objects.filter(company=comp_id, coin=c)
        serializer = ContractSerializer(contrByCoin, many=True)
        filteredContracts = serializer.data

        # select Name Id and Image from coins
        coinInfo = Coin.objects.get(pk=c)
        response.append({
            "CoinName": coinInfo.name,
            "CoinToken": coinInfo.token,
            "CoinImage": coinInfo.image,
            "Contracts": filteredContracts
        })

    return JsonResponse(response, safe=False)


@api_view(['GET','PUT','POST'])
@csrf_exempt
def all_contracts(request):

    if request.method == 'GET':
        contracts = CloudContract.objects.all()
        serializer = ContractSerializer(contracts, many=True)
        return JsonResponse(JSONEncoder().encode(serializer.data), safe=False)

    elif request.method == 'PUT':
        contractId = request.data['_id']
        try:
            contract = CloudContract.objects.get(pk=contractId)
        except CloudContract.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)
        serializer = ContractSimpleSerializer(contract, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(JSONEncoder().encode(serializer.data), status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = ContractSimpleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(JSONEncoder().encode(serializer.data), status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@csrf_exempt
def delete_contract(request, contract_id):
    try:
        contract = CloudContract.objects.get(pk=contract_id)
        contract.delete()
        response = {"result": "Item deleted"}
        return JsonResponse(response, status=status.HTTP_200_OK)
    except CloudContract.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)


# The method returns the most profitable contract
# For now it just returns random contract
def get_best_contract(request):
    pks = CloudContract.objects.values_list('pk', flat=True)
    random_idx = random.randint(0, len(pks) - 1)
    contract = CloudContract.objects.get(pk=pks[random_idx])
    serializer = ContractSerializer(contract)
    return JsonResponse(JSONEncoder().encode(serializer.data), safe=False)


def getPricePrediction(request):
    result = get_coin_price_prediction()
    return JsonResponse(result, safe=False)