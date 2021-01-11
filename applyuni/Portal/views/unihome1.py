from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
class unihome1(View):
    def get(self,request):
        print(request.session['university_Email'])
        return render(request,'login/universitylogin.html')
