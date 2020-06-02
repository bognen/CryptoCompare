#from django.core import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_meets_djongo.serializers import DjongoModelSerializer

from cryptocloud.models import CloudCompany
from cryptocloud.models import Coin
from cryptocloud.models import CloudContract


class CloudCompanySerializer(DjongoModelSerializer):
    class Meta:
        model = CloudCompany
        fields = ["_id","title", "location", "founded", "image", "website", "legitimacy", "description"]


class CoinSerializer(DjongoModelSerializer):
    class Meta:
        model = Coin
        fields = "__all__"


class ContractSimpleSerializer(DjongoModelSerializer):
    class Meta:
        model = CloudContract
        fields = "__all__"


class ContractSerializer(DjongoModelSerializer):
    _id = serializers.CharField(max_length=128)
    name = serializers.CharField(max_length=128)
    image = serializers.CharField(max_length=128)
    duration = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=15, decimal_places=2)
    hashRate = serializers.DecimalField(max_digits=15, decimal_places=2)
    description = serializers.CharField(max_length=5000)
    coin = CoinSerializer(many=False, read_only=True)
    company = CloudCompanySerializer(many=False, read_only=True)

    class Meta:
        model = CloudContract
        fields = [
            '_id',
            'name',
            'image',
            'duration',
            'price',
            'hashRate',
            'description',
            'coin',
            'company'
        ]