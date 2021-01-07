from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form= UserCreationForm()
    return render(request,'',{'form':form})
