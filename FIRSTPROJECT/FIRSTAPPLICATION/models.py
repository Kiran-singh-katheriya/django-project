from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length =255)
    id=models.IntegerField(primary_key=True)
    contact=models.IntegerField()
    address=models.CharField(max_length =255)

