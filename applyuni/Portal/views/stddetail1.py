from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from Portal.models.stddetail import Stddetail
from Portal.models.studentinfo import Student
from django.views import View

def home(request):
    return render(request,'Admin_portal\stddetail.html')
