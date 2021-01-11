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
        unimailcheck=University.IsExists(Universitymail)
        error_message=None
        if(unimailcheck):
            error_message="Hei!!! University already Exist !!"
            return render(request,'signup_forms/university_signup.html',{'error':error_message})
        if(Password!=Confirmpassword):
            error_message="Hei!!! Password doesnt Match !!"
            return render(request,'signup_forms/university_signup.html',{'error':error_message})

        else:
            universitysignup.register()
        return redirect('home')
