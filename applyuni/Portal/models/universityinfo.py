from django.db import models
from django.core.validators import MinLengthValidator

class University(models.Model):
    Universityname=models.CharField(max_length=500)
    Univcontactnumber=models.CharField(max_length=50)
    Universitymail=models.EmailField()
    Password=models.CharField(max_length=500)
    Confirmpassword=models.CharField(max_length=500)

    def __str__(self):
        return self.Universityname

    def register(self):
        self.save()

    @staticmethod
    def get_university_by_email(email):
        try:
            return University.objects.get(Universitymail=email)
        except:
            return False

    def IsExists(self):
        if University.objects.filter(Universitymail=self.Universitymail) :
            return True

        return False
