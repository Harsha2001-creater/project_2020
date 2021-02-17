from django.db import models
from django.core.validators import MinLengthValidator
from django.http import HttpResponse

class Univdetail(models.Model):
    Institutemode= models.CharField(max_length=500,null=True)
    Institutetype= models.CharField(max_length=500,null=True)
    Year=models.CharField(max_length=50,null=True)
    Rank=models.CharField(max_length=50,null=True)
    About=models.CharField(max_length=50,null=True)
    Campuses=models.CharField(max_length=50,null=True)
    Departments = models.CharField(max_length=50,null=True)
    Education=models.CharField(max_length=50,null=True)
    Feeug=models.CharField(max_length=50,null=True)
    Feepg=models.CharField(max_length=50,null=True)
    Intake= models.CharField(max_length=50,null=True)
    #sscgrading=(('M','Marks'),('%','Percentage'),('C','CGPA'))
    Awards=models.CharField(max_length=50,null=True)
    Staff=models.CharField(max_length=50,null=True)
    Students=models.CharField(max_length=50,null=True)
    Location=models.CharField(max_length=10,null=True)
    Phonenumber=models.CharField(max_length=10,null=True)
    Email=models.CharField(max_length=50,null=True)

    Applyfee=models.CharField(max_length=50,null=True)
    Currency=models.CharField(max_length=50,null=True)
    Amount=models.CharField(max_length=50,null=True)
    Applyform=models.FileField(upload_to="",null=True)
    Duration=models.CharField(max_length=50,null=True)
    Applypro1=models.CharField(max_length=50,null=True)
    Applypro2=models.CharField(max_length=50,null=True)
    Applypro3=models.CharField(max_length=50,null=True)
    Applypro4=models.CharField(max_length=50,null=True)
    Doc1=models.CharField(max_length=50,null=True)
    Doc2=models.CharField(max_length=50,null=True)
    Doc3=models.CharField(max_length=50,null=True)
    Doc4=models.CharField(max_length=50,null=True)
    Doc5=models.CharField(max_length=50,null=True)
    Doc6=models.CharField(max_length=50,null=True)
    Doc7=models.CharField(max_length=50,null=True)
    Doc8=models.CharField(max_length=50,null=True)
    Doc9=models.CharField(max_length=50,null=True)
    Term1=models.CharField(max_length=500,null=True)
    Term2=models.CharField(max_length=500,null=True)
    Term3=models.CharField(max_length=500,null=True)
    Term4=models.CharField(max_length=500,null=True)












    def __str__(self):
        return self.Email
    def register(self):
        self.save()
        return True
    @staticmethod

    def get_univdetail_by_email(Email):
            #print(Email)
            #print(Stddetail.objects.all())
            #print(Stddetail.objects.get(Email=Email))
            print("nanda")
            try:
                print("Nanda")
                print(Univdetail.objects.get(Email=Email))
                return Univdetail.objects.get(Email=Email)
            except:
                False
