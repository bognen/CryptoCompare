
from django.contrib import admin
from django.urls import path
from cryptocloud.views import all_companies
from cryptocloud.views import all_coins
from cryptocloud.views import get_company

urlpatterns = [
    path('companies/', all_companies),
    path('coins/', all_coins),
    path('company/<str:company_id>/', get_company),
]