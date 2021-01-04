from django.db import models

# Create your models here.

class User(models.Model):
    Nmae=models.CharField(max_length=250)