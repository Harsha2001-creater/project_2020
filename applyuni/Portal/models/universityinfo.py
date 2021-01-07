from django.db import models
from django.core.validators import MinLengthValidator

class University(models.Model):
    universityname= models.CharField(max_length=500)
    phonenumber= models.CharField(max_length=50)
    institute_email = models.EmailField()
    personal_email = models.EmailField()
    password = models.CharField(max_length=500)
    confirm_password = models.CharField(max_length=500)

    def __str__(self):
        return self.universityname

    def register(self):
        self.save()

    @staticmethod
    def get_university_by_email(email):
        try:
            return University.objects.get(email=email)
        except:
            return False

    def IsExists(self):
        if University.objects.filter(email=self.email) :
            return True

        return False
