from django.db import models
from django.core.validators import MinLengthValidator

class Stdquery(models.Model):
    Name=models.CharField(max_length=500)
    Email=models.EmailField()
    Phonenumber=models.CharField(max_length=20)
    Date=models.CharField(max_length=10)

    def _str_(self):
        return self.Name

    def register(self):
        self.save()
        return True
