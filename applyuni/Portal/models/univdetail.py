from django.db import models
from django.core.validators import MinLengthValidator
from django.http import HttpResponse

class Univdetail(models.Model):
    Institutemode= models.CharField(max_length=500)
    Institutetype= models.CharField(max_length=500)
    Year=models.CharField(max_length=50,null=True)
    Rank=models.CharField(max_length=50,null=True)
    About=models.CharField(max_length=50,null=True)
    Campuses=models.CharField(max_length=50)
    Departments = models.CharField(max_length=50)
    Education=models.CharField(max_length=50)
    Feeug=models.CharField(max_length=50)
    Feepg=models.CharField(max_length=50)
    Intake= models.CharField(max_length=50)
    #sscgrading=(('M','Marks'),('%','Percentage'),('C','CGPA'))
    Awards=models.CharField(max_length=50)
    Staff=models.CharField(max_length=50)
    Students=models.CharField(max_length=50)
    Location=models.CharField(max_length=10,null=True)
    Phonenumber=models.CharField(max_length=10)
    Email=models.CharField(max_length=50)

    Applyfee=models.CharField(max_length=50,null=True)
    Currency=models.CharField(max_length=50)
    Amount=models.CharField(max_length=50)
    Applyform=models.FileField(upload_to="")
    Duration=models.CharField(max_length=50)
    Applypro1=models.CharField(max_length=50)
    Applypro2=models.CharField(max_length=50)
    Applypro3=models.CharField(max_length=50)
    Applypro4=models.CharField(max_length=50)
    Doc1=models.CharField(max_length=50)
    Doc2=models.CharField(max_length=50)
    Doc3=models.CharField(max_length=50)
    Doc4=models.CharField(max_length=50)
    Doc5=models.CharField(max_length=50)
    Doc6=models.CharField(max_length=50)
    Doc7=models.CharField(max_length=50)
    Doc8=models.CharField(max_length=50)
    Doc9=models.CharField(max_length=50)
    Term1=models.CharField(max_length=500)
    Term2=models.CharField(max_length=500)
    Term3=models.CharField(max_length=500)
    Term4=models.CharField(max_length=500)

    Coursename=models.CharField(max_length=50,null=True)  
    Coursetype=models.CharField(max_length=50,null=True)
    Facultyname=models.CharField(max_length=50,null=True)
    Courseapproval=models.CharField(max_length=50,null=True)
    Approvalauthority=models.CharField(max_length=50,null=True)
    Tutionfee=models.CharField(max_length=50,null=True)
    Amount1=models.CharField(max_length=50 ,null=True)
    Sem1=models.CharField(max_length=50,null=True)
    Sem2=models.CharField(max_length=50,null=True)
    Sem3=models.CharField(max_length=50,null=True)
    Sem4=models.CharField(max_length=50,null=True)
    Sem5=models.CharField(max_length=50,null=True)
    Sem6=models.CharField(max_length=50,null=True)
    Duration1=models.CharField(max_length=50,null=True)
    Noofsems=models.CharField(max_length=50,null=True)
    Criteria1=models.CharField(max_length=50,null=True)
    Criteria2=models.CharField(max_length=50,null=True)
    Criteria3=models.CharField(max_length=50,null=True)  
    









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
