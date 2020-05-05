from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.shortcuts import render

# View returns all companies from Data Base
from cryptocloud.models import CloudCompany
from cryptocloud.serializers import CloudCompanySerializer
from cryptocloud.models import Coin
from cryptocloud.serializers import CoinSerializer


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
            "id" : str(c._id),
            "name": c.name,
            "token": c.token,
            "image": c.image,
            "max_supply": c.maxSupply,
            "start_date": c.startDate,
        })

    return JsonResponse(result, safe=False)


def get_company(request, company_id):
    company = CloudCompany.objects.get(pk=company_id)
    # result = {
    #     "title": company.title,
    #     'location': company.location,
    #     "founded": company.founded,
    #     "image": company.image,
    #     "website": company.website,
    #     "legitimacy": company.legitimacy,
    #     "description": company.description
    # }
    # return JsonResponse(result, safe=False)
    serializer = CloudCompanySerializer(company)
    return JsonResponse(serializer.data)