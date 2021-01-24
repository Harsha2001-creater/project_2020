from django.db import models
from django.core.validators import MinLengthValidator

class Student(models.Model):
    gender=(('M','Male'),('F','Female'))
    Firstname= models.CharField(max_length=500)
    Lastname= models.CharField(max_length=500)
    Dateofbirth=models.DateField(max_length=50)
    Gender=models.CharField(max_length=50)
    Email = models.EmailField()
    Phonenumber= models.CharField(max_length=50)
    Password = models.CharField(max_length=500)
    Confirmpassword = models.CharField(max_length=500)
    

    def __str__(self):
        return self.Firstname
    def register(self):
        self.save()

    @staticmethod
    def get_student_by_email(Email):
        try:
            #print(Email)
            #print(Student.objects.all())
            #print(Student.objects.get(Email=Email))
            return Student.objects.get(Email=Email)
        except:
            return False

    def IsExists(Email):
        if Student.objects.filter(Email=Email) :
            return True

        return False
