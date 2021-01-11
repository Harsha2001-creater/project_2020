from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
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
        Gender=postData.get('Gender')
        print(Gender)
        Phonenumber=postData.get('Phonenumber')
        Email=postData.get('Email')
        Password=postData.get('Password')
        Confirmpassword=postData.get('Confirmpassword')

        error_message=None
        studentsignup1=Student.IsExists(Email)
        value={'Firstname':Firstname,'Lastname':Lastname,'Dateofbirth':Dateofbirth,'Gender':Gender,'Phonenumber':Phonenumber,'Email':Email,'Password':Password,'Confirmpassword':Confirmpassword}



        if(studentsignup1):
            error_message="Email already Exists !!"
            data={'value':value , 'error': error_message}
            return render(request,'signup_forms/student_signup.html',data)
        if(Password !=Confirmpassword ):
            error_message="Password is not valid"
            data={'value':value , 'error': error_message}
            return render(request,'signup_forms/student_signup.html',data)

        studentsignup=Student(
    Firstname =Firstname,Lastname=Lastname,Dateofbirth=Dateofbirth,Gender=Gender,Phonenumber=Phonenumber,Email=Email
    ,Password=Password,Confirmpassword=Confirmpassword )
        studentsignup.Password=make_password(studentsignup.Password)
        studentsignup.Confirmpassword=make_password(studentsignup.Confirmpassword)
        studentsignup.register()

        return redirect('home')
