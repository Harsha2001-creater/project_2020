from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
def payment(request):
	return render(request,'payment/payment.html')
