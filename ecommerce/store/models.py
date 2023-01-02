from django.db import models
from django.db.models.aggregates import Max
from django.db.models.fields import EmailField

# Create your models here.
class Login (models.Model):
    email    = models.CharField(max_length=100)
    password = models.CharField(max_length=25)
    address  = models.CharField(max_length=200)
    city     = models.Choices
    zip      = models.BooleanField  
    def __str__(self):
        return self.email