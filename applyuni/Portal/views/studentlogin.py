from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from Portal.models.studentinfo import Student
from Portal.models.stddetail import Stddetail
from django.contrib.auth.hashers import check_password
from django.views import View
# Create your views here.
class studentlogin(View):
    return_url = None
    def get(self,request):
        studentlogin.return_url = request.GET.get('return_url')
        return render(request,'login/studentlogin.html')

    def post(self,request):
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        student=Student.get_student_by_email(Email)
        error_message= None
        if student :
            flag= check_password(Password,student.Password)
            print("hai")
            if flag:
                request.session['student']=student.id
                request.session['Firstname']=student.Firstname
                request.session['Email']=student.Email
                return render(request,'student_portal/studenthome.html')

                '''
                if studentlogin.return_url():
                    return HttpResponseRedirect(return_url)
                else:
                    studentlogin.return_url=None
                    return redirect('homepage')
                    '''
            else:
                error_message='Password is invalid!!!'
        else:
            error_message='Email is invalid!!!'
        return render(request,'login/studentlogin.html',{'error':error_message})
def logout(request):

    request.session.clear()
    return redirect('studentloginpage')
