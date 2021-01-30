from django.db import models
from django.core.validators import MinLengthValidator

class Newcourse(models.Model):
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
    Universitymail=models.EmailField()

    def register(self):
        self.save()
        return True

   