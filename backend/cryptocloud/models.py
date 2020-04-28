#from django.db import models
from djongo import models


# Create your models here.
class CloudCompany(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=128)
    address = models.CharField(max_length=500)
