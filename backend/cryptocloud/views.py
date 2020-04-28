from django.http import JsonResponse
from django.shortcuts import render

# View returns all companies from Data Base
from cryptocloud.models import CloudCompany


def all_companies(request):
    result = []
    companies = CloudCompany.objects.all()
    for comp in companies:
        result.append({
            "title": comp.title,
            "address": comp.address
        })

    return JsonResponse(result, safe=False)