from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from Portal.models.universityinfo import University
from django.views import View
from django.contrib.auth.hashers import make_password
import smtplib
import random
import string
a=""

class temp_pass:
    def do(Email):
        global a
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('techclub.cse.sse@gmail.com','techclubcse@saveetha')
        letters=string.ascii_lowercase
        a=str(''.join(random.choice(letters) for i in range(10)))
        print(a)
        b=a+'    '+'Use this as Your Temporary Password'
        server.sendmail('techclub.cse.sse@gmail.com',Email,b)
        return a

class emailvalid1(View):
    def get(self,request):
        return render(request,'login/password_reset.html')
    def post(self,request):
        Email=request.POST.get('Universitymail')
        a1=Student.IsExists(Email)
        if(a1):
            if(temp_pass.do(Email)):
                error_message="Email has been sent successfully"
                return render(request,'login/password_reset.html',{'error':error_message})
        else:
            error_message1="Please Enter Valid Email"
            return render(request,'login/password_reset.html',{'error1':error_message1})
class tempvalidator1(View):
    def get(self,request):
        return render(request,'login/password_reset_confirm.html')
    def post(self,request):
        temp_pass=request.POST.get('temp_pass')
        Password=request.POST.get('Password')
        Confirmpassword=request.POST.get('Confirmpassword')
        university=University.get_university_by_email(request.session['university_Email'])
        #student.Password=None
        print(temp_pass)
        print(a)
        if(temp_pass==a):
            print("nanda")
            university.Password=make_password(Password)
            university.Confirmpassword=make_password(Confirmpassword)
            university.temp_pass=None
            university.register()
            print(university.Password)
            return render(request,'login/universitylogin.html')
        else:
            error_message2="Please Enter Valid Temporary Password"
            return render(request,'login/password_reset_confirm.html',{'error2':error_message2})
