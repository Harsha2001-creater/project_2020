from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from Portal.models.studentinfo import Student
from django.views import View
from django.shortcuts import render,redirect
class studentsignup(View):
    def get(self,request):
        return render(request,'signup_forms/student_signup.html')
    def post(self,request):
        postData = request.POST
        Firstname=postData.get('Firstname')
        Lastname=postData.get('Lastname')
        Dateofbirth=postData.get('Dateofbirth')
        Phonenumber=postData.get('Phonenumber')
        Email=postData.get('Email')
        Password=postData.get('Password')
        Confirmpassword=postData.get('Confirmpassword')
        studentsignup=Student(
    Firstname =Firstname,Lastname=Lastname,Dateofbirth=Dateofbirth,Phonenumber=Phonenumber,Email=Email
    ,Password=Password,Confirmpassword=Confirmpassword )
        studentsignup.register()
        return redirect('home')
