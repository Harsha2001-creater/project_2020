from django.shortcuts import render,redirect,HttpResponseRedirect
from Portal.models.universityinfo import University
from Portal.models.univdetail import Univdetail
from Portal.models.newcourse import Newcourse
from django.http import HttpResponse
from django.views import View

class overview(View):
    def get(self,request,name="a"):
        try:
            Email=request.session['university_Email']
        except:
            print("moish")
            objdetail=University.objects.get(Universityname=name)
            print(objdetail.Universitymail)
            Email=objdetail.Universitymail
            
        univ_courses=Newcourse.objects.filter(Universitymail=Email)    
        univdetail=Univdetail.get_univdetail_by_email(Email)
        

        university=University.get_university_by_email(Email)
        print(university.Universityname)
        Name=university.Universityname
        About=univdetail.About
        Campuses=univdetail.Campuses
        Departments=univdetail.Departments
        Education=univdetail.Education
        Intake=univdetail.Intake
        Staff=univdetail.Staff
        Students=univdetail.Students

        Location=univdetail.Location
        Phonenumber=univdetail.Phonenumber
        Email=univdetail.Email

        value={}
        value={'Name':Name,'About':About,'Campuses':Campuses,
        'Departments':Departments,'Education':Education,'Intake':Intake,
        'Staff':Staff,'Students':Students,'Location':Location,'Phonenumber':Phonenumber,'Email':Email}
        data={'value':value,'univ_courses':univ_courses}
        return render(request,'university_page/overview.html',data)
