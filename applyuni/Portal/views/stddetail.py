from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from Portal.models.stddetail import Stddetail
from Portal.models.studentinfo import Student
from django.views import View

class stddetail(View):
    def post(self,request):
        print("in post man in stddetail")
        Firstname= request.POST.get('Firstname')
        Lastname= request.POST.get('Lastname')
        Dateofbirth=request.POST.get('Dateofbirth')
        print(Firstname)
        Gender=request.POST.get('Gender')
        Maritial=request.POST.get('Maritial')
        Nationality=request.POST.get('Nationality')
        Email = request.POST.get('Email')
        Address=request.POST.get('Address')
        City=request.POST.get('City')
        State=request.POST.get('State')
        Country=request.POST.get('Country')
        Phonenumber= request.POST.get('Phonenumber')

        Sscqual=request.POST.get('Sscqual')
        Sscname=request.POST.get('Sscname')
        Sscdate=request.POST.get('Sscdate')
        Sscmarks=request.POST.get('Sscmarks')
        Sscgrading=request.POST.get('Sscgrading')
        SscDoc=request.FILES.get('SscDoc')
        Intqual=request.POST.get('Intqual')
        Intname=request.POST.get('Intname')
        Intdate=request.POST.get('Intdate')
        Intmarks=request.POST.get('Intmarks')
        Intgrading=request.POST.get('Intgrading')
        IntDoc=request.POST.get('IntDoc')
        Uniqual=request.POST.get('Uniqual')
        Uniname=request.POST.get('Uniname')
        Unicname=request.POST.get('Unicname')
        Unidate=request.POST.get('Unidate')
        Unimarks=request.POST.get('Unimarks')
        Unigrading=request.POST.get('Unigrading')
        UniDoc=request.POST.get('UniDoc')
        Testeng=request.POST.get('Testeng')
        Yeareng=request.POST.get('Yeareng')
        Overallscoreeng=request.POST.get('Overallscoreeng')
        Uploadeng=request.FILES.get('Uploadeng')
        Testeng1=request.POST.get('Testeng1')
        Yeareng1=request.POST.get('Yeareng1')
        Overallscoreeng1=request.POST.get('Overallscoreeng1')
        Uploadeng1=request.FILES.get('Uploadeng1')

        Testad=request.POST.get('Testad')
        Yearad=request.POST.get('Yearad')
        Overallscoread=request.POST.get('Overallscoread')
        Uploadad=request.FILES.get('Uploadad')

        Testad1=request.POST.get('Testad')
        Yearad1=request.POST.get('Yearad')
        Overallscoread1=request.POST.get('Overallscoread')
        Uploadad1=request.FILES.get('Uploadad')

        Applyingfor=request.POST.get('Applyingfor')
        Date=request.POST.get('Date')
        pcoun1=request.POST.get('pcoun1')
        pcoun2=request.POST.get('pcoun2')
        pcoun3=request.POST.get('pcoun3')
        pcour4=request.POST.get('pcour4')
        pcour5=request.POST.get('pcour5')
        pcour6=request.POST.get('pcour6')
        stddetail=Stddetail(Firstname= Firstname,Lastname= Lastname,Dateofbirth=Dateofbirth,Gender=Gender,
        Maritial=Maritial,Nationality=Nationality,Email = Email,Address=Address,City=City,State=State,
        Country=Country,Phonenumber= Phonenumber,
        Sscqual=Sscqual,Sscname=Sscname,Sscdate=Sscdate,Sscmarks=Sscmarks,Sscgrading=Sscgrading,SscDoc=SscDoc,
        Intqual=Intqual,Intname=Intname,
        Intdate=Intdate,
        Intmarks=Intmarks,Intgrading=Intgrading,IntDoc=IntDoc,Uniqual=Uniqual,Uniname=Uniname,Unicname=Unicname
        ,Unidate=Unidate,Unimarks=Unimarks,Unigrading=Unigrading,UniDoc=UniDoc,
        Testeng=Testeng,Yeareng=Yeareng,Overallscoreeng=Overallscoreeng,Uploadeng=Uploadeng,
        Testeng1=Testeng,Yeareng1=Yeareng,Overallscoreeng1=Overallscoreeng,Uploadeng1=Uploadeng,

        Testad=Testad,Yearad=Yearad,Overallscoread=Overallscoread,Uploadad=Uploadad,
        Testad1=Testad,Yearad1=Yearad,Overallscoread1=Overallscoread,Uploadad1=Uploadad,

        Applyingfor=Applyingfor,Date=Date,pcoun1=pcoun1,pcoun2=pcoun2,pcoun3=pcoun3,pcour4=pcour4,pcour5=pcour5,pcour6=pcour6)
        student=Student.get_student_by_email(Email)
        stddetail1=Stddetail.get_stddetail_by_email(student.Email)
        if(stddetail1):
            stddetail1.delete()

        stddetail.register()

        value={'Firstname': Firstname,'Lastname': Lastname,'Dateofbirth':Dateofbirth,'Gender':Gender,
        'Maritial':Maritial,'Nationality':Nationality,'Email' : Email,'Address':Address,'City':City,'State':State,
        'Country':Country,'Phonenumber': Phonenumber,
        'Sscqual':Sscqual,'Sscname':Sscname,'Sscdate':Sscdate,'Sscmarks':Sscmarks,'Sscgrading':Sscgrading,'SscDoc':SscDoc,
        'Intqual':Intqual,'Intname':Intname,'Intdate':Intdate,'Intmarks':Intmarks,'Intgrading':Intgrading,
        'IntDoc':IntDoc,'Uniqual':Uniqual,'Uniname':Uniname,'Unicname':Unicname,'Unidate':Unidate,'Unimarks': Unimarks,
        'Unigrading':Unigrading,'UniDoc':UniDoc,
        'Testeng': Testeng,'Yeareng':Yeareng,'Overallscoreeng': Overallscoreeng,'Uploadeng':Uploadeng,
        'Testeng1': Testeng1,'Yeareng1':Yeareng1,'Overallscoreeng1': Overallscoreeng1,'Uploadeng1':Uploadeng1,
        'Testad': Testad,'Yearad': Yearad,'Overallscoread':Overallscoread,'Uploadad':Uploadad,
        'Applyingfor':Applyingfor,'Date':Date,'pcoun1':pcoun1,'pcoun2':pcoun2,'pcoun3':pcoun3,'pcour4':pcour4,'pcour5':pcour5,'pcour6':pcour6}
        print(value['Firstname'])
        data={'value':value}
        return render(request,'Admin_portal/stddetail.html',data)
