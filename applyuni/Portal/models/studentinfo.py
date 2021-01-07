from django.db import models
from django.core.validators import MinLengthValidator

class Student(models.Model):
    gender=(('M','Male'),('F','Female'))
    Firstname= models.CharField(max_length=500)
    Lastname= models.CharField(max_length=500)
    Gender=models.CharField(choices=gender,max_length=50)
    email = models.EmailField()
    phonenumber= models.CharField(max_length=50)
    password = models.CharField(max_length=500)
    confirm_password = models.CharField(max_length=500)


    def __str__(self):
        return self.Firstname
    def register(self):
        self.save()

    @staticmethod
    def get_student_by_email(email):
        try:
            return Student.objects.get(email=email)
        except:
            return False

    def IsExists(self):
        if Student.objects.filter(email=self.email) :
            return True

        return False
