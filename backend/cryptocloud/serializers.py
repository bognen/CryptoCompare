from django.core import serializers
from rest_framework.serializers import ModelSerializer
from cryptocloud.models import CloudCompany
from cryptocloud.models import Coin


class CloudCompanySerializer(ModelSerializer):
    class Meta:
        model = CloudCompany
        fields = ["title", "location", "founded", "image", "website", "legitimacy", "description"]


class CoinSerializer(ModelSerializer):
    class Meta:
        model = Coin
        fields = "__all__"