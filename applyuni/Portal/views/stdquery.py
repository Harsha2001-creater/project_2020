from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from Portal.models.stdquery import Stdquery
from django.views import View

class stdquery(View):
    def post(self,request):
        message=''
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        Phonenumber=request.POST.get('Phonenumber')
        Date=request.POST.get('Date')
        studentquery=Stdquery(Name=Name,Email=Email,Phonenumber=Phonenumber,Date=Date)
        if(studentquery.register()):
            message="Your appoitment will be scheduled soon"
        return render(request,'landing_page.html',{'Message':message})
