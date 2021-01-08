from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from Portal.models.universityinfo import University
from django.views import View
from django.shortcuts import render,redirect
class universitysignup(View):
    def get(self,request):
        return render(request,'signup_forms/university_signup.html')
    def post(self,request):
        postData = request.POST
        Universityname=postData.get('Universityname')
        Univcontactnumber=postData.get('Univcontactnumber')
        Universitymail=postData.get('Universitymail')
        Password=postData.get('Password')
        Confirmpassword=postData.get('Confirmpassword')
        universitysignup=University(Universityname=Universityname,Univcontactnumber=Univcontactnumber,
        Universitymail=Universitymail,Password=Password,Confirmpassword=Confirmpassword)
        universitysignup.register()
        return redirect('home')
