from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse

from django.views import View


def Cons(request):
     return render(request,'consultancy/signup.html')
