#from django.db import models
from djongo import models


# Create your models here.
LegitimacyStatus = [('OK', 'Checked'),('QS', 'Questionable'),('BAD', 'Scam')]


class Coin(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=128, default="KwaCoin")
    token = models.CharField(max_length=128, default="KwaToken")
    image = models.CharField(max_length=128, null=True, blank=True)
    algorithm = models.CharField(max_length=128, null=True, blank=True)
    website = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField(max_length=5000, null=True, blank=True)
    maxSupply = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    startDate = models.DateField()
    coinGecko = models.CharField(max_length=128, null=True, blank=True)
    # DYNAMIC FIELDS
    # Current Price
    # Projection Price


class CloudCompany(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=128, default="KwaKwa LTD")
    image = models.CharField(max_length=128, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    website = models.CharField(max_length=35, null=True, blank=True)
    coins = models.ManyToManyField('cryptocloud.Coin')
    founded = models.CharField(max_length=12, null=True, blank=True)
    description = models.CharField(max_length=5000, null=True, blank=True)
    legitimacy = models.CharField(max_length=12, choices=LegitimacyStatus, default='Questionable')
    # DYNAMIC FIELD
    # Number of Contracts


class CloudContract(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=128, default="KwaContract")
    image = models.CharField(max_length=128, null=True, blank=True)
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    hasRate = models.DecimalField(max_digits=15, decimal_places=2)
    company = models.ForeignKey('cryptocloud.CloudCompany', on_delete=models.CASCADE)
    coins = models.ForeignKey('cryptocloud.Coin', on_delete=models.CASCADE)
