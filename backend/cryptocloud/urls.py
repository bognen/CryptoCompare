
from django.contrib import admin
from django.urls import path
from cryptocloud.views import all_companies, all_contracts
from cryptocloud.views import all_coins
from cryptocloud.views import get_company
from cryptocloud.views import get_contract
from cryptocloud.views import delete_contract
from cryptocloud.views import get_best_contract
from cryptocloud.views import get_contract_by_company
from cryptocloud.views import getPricePrediction


urlpatterns = [
    path('companies/', all_companies),
    path('coins/', all_coins),
    path('company/<str:company_id>/', get_company),
    path('contracts/', all_contracts),
    path('contract/<str:contract_id>/', get_contract),
    path('deletecontract/<str:contract_id>', delete_contract),
    path('filtered-contract/<str:comp_id>', get_contract_by_company),
    path('most-profitable/', get_best_contract),
    path('prices/', getPricePrediction),
]