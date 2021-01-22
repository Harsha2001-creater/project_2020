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
        if(student):
            stddetail=Stddetail.get_stddetail_by_email(student.Email)

        error_message= None
        if student :
            flag= check_password(Password,student.Password)
            print("hai")
            if flag:
                request.session['student']=student.id
                request.session['Firstname']=student.Firstname
                request.session['Email']=student.Email
                if(stddetail):
                    value={'Firstname': stddetail.Firstname,'Lastname': stddetail.Lastname,'Dateofbirth':stddetail.Dateofbirth,'Gender':stddetail.Gender,
                    'Maritial':stddetail.Maritial,'Nationality':stddetail.Nationality,'Email' : stddetail.Email,'Address':stddetail.Address,'City':stddetail.City,'State':stddetail.State,
                    'Country':stddetail.Country,'Phonenumber': stddetail.Phonenumber,
                    'Sscqual':stddetail.Sscqual,'Sscname':stddetail.Sscname,'Sscdate':stddetail.Sscdate,'Sscmarks':stddetail.Sscmarks,'Sscgrading':stddetail.Sscgrading,'SscDoc':stddetail.SscDoc,
                    'Intqual':stddetail.Intqual,'Intname':stddetail.Intname,'Intdate':stddetail.Intdate,'Intmarks':stddetail.Intmarks,'Intgrading':stddetail.Intgrading,
                    'IntDoc':stddetail.IntDoc,'Uniqual':stddetail.Uniqual,'Uniname':stddetail.Uniname,'Unicname':stddetail.Unicname,'Unidate':stddetail.Unidate,'Unimarks': stddetail.Unimarks,
                    'Unigrading':stddetail.Unigrading,'UniDoc':stddetail.UniDoc,
                    'Testeng': stddetail.Testeng,'Yeareng':stddetail.Yeareng,'Overallscoreeng': stddetail.Overallscoreeng,'Uploadeng':stddetail.Uploadeng,
                    'Testeng1':stddetail.Testeng1,'Yeareng1':stddetail.Yeareng1,'Overallscoreeng1': stddetail.Overallscoreeng1,'Uploadeng1':stddetail.Uploadeng1,
                    'Testad': stddetail.Testad,'Yearad': stddetail.Yearad,'Overallscoread':stddetail.Overallscoread,'Uploadad':stddetail.Uploadad,
                    'Applyingfor':stddetail.Applyingfor,'Date':stddetail.Date,'pcoun1':stddetail.pcoun1,'pcoun2':stddetail.pcoun2,'pcoun3':stddetail.pcoun3,'pcour4':stddetail.pcour4,'pcour5':stddetail.pcour5,'pcour6':stddetail.pcour6}
                    data={'value':value}

                    return render(request,'Admin_portal/stddetail.html',data)
                else:
                    return render(request,'Admin_portal/stddetail.html')

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
