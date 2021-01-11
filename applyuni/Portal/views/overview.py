from django.shortcuts import render,redirect,HttpResponseRedirect
from Portal.models.universityinfo import University
from Portal.models.univdetail import Univdetail
from django.http import HttpResponse
from django.views import View

class overview(View):
    def get(self,request):
        Email=request.session['university_Email']
        univdetail=Univdetail.get_univdetail_by_email(Email)
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


        university=University.get_university_by_email(Email)
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
        value={'Name':Name,'About':About,'Campuses':Campuses,About:'About',Campuses:'Campuses',
        Departments:'Departments',Education:'Education',Intake:'Intake',
        Staff:'Staff',Students:'Students',Location:'Location',Phonenumber:'Phonenumber',Email:'Email'}
        data={'value':value}
        return render(request,'university_page/overview.html',data)
