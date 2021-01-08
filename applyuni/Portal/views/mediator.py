from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse

def home(request):
    return render(request,'landing_page.html')
def login_mediator(request):
    return render(request,'login/login-mediator.html')
def signup_mediator(request):
    return render(request,'login/signup-mediator.html')
def studentsignup(request):
    return render(request,'signup_forms/student_signup.html')
def universitysignup(request):
    return render(request,'signup_forms/university_signup.html')
