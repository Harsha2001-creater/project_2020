from django.db import models

# Create your models here.

class User(models.Model):
    firstname=models.CharField(max_length=250)
    phone = models.IntegerField(null= false)