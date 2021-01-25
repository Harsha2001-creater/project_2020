from django.shortcuts import render,redirect,HttpResponseRedirect
from Portal.models.universityinfo import University
from Portal.models.univdetail import Univdetail
from django.http import HttpResponse
from django.views import View

class overview(View):
    def get(self,request,pk=0):
        try:
            Email=request.session['university_Email']
        except:
            objdetail=University.objects.get(pk=pk)
            print(objdetail.Universitymail)
            Email=objdetail.Universitymail
            
        univdetail=Univdetail.get_univdetail_by_email(Email)
        print(univdetail)
        request.session['About']=univdetail.About
        request.session['Campuses']=univdetail.Campuses
        request.session['Departments']=univdetail.Departments
        request.session['Education']=univdetail.Education
        request.session['Intake']=univdetail.Intake
        request.session['Staff']=univdetail.Staff
        request.session['Students']=univdetail.Students

        request.session['Location']=univdetail.Location
        request.session['Phonenumber']=univdetail.Phonenumber
        request.session['Email']=univdetail.Email
        print(request.session['Staff'])

        university=University.get_university_by_email(Email)
        print(university.Universityname)
        Name=university.Universityname
        About=request.session['About']
        Campuses=request.session['Campuses']
        Departments=request.session['Departments']
        Education=request.session['Education']
        Intake=request.session['Intake']
        Staff=request.session['Staff']
        Students=request.session['Students']

        Location=request.session['Location']
        Phonenumber=request.session['Phonenumber']
        Email=request.session['Email']

        value={}
        value={'Name':Name,'About':About,'Campuses':Campuses,
        'Departments':Departments,'Education':Education,'Intake':Intake,
        'Staff':Staff,'Students':Students,'Location':Location,'Phonenumber':Phonenumber,'Email':Email}
        data={'value':value}
        return render(request,'university_page/overview.html',data)
