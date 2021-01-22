from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from Portal.models.stddetail import Stddetail
from django.core.files.storage import FileSystemStorage
from Portal.models.studentinfo import Student
from django.views import View


class stddetail(View):
    def get(self,request):
        student=Student.get_student_by_email(request.session['Email'])
        if(student):
            stddetail=Stddetail.get_stddetail_by_email(student.Email)
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
        SscDoc=request.FILES['SscDoc']

        fs=FileSystemStorage()
        name=fs.save(SscDoc.name,SscDoc)
        url=fs.url(name)
        print(url)
        Intqual=request.POST.get('Intqual')
        Intname=request.POST.get('Intname')
        Intdate=request.POST.get('Intdate')
        Intmarks=request.POST.get('Intmarks')
        Intgrading=request.POST.get('Intgrading')
        IntDoc=request.FILES['IntDoc']

        name1=fs.save(IntDoc.name,IntDoc)
        url1=fs.url(name1)
        Uniqual=request.POST.get('Uniqual')
        Uniname=request.POST.get('Uniname')
        Unicname=request.POST.get('Unicname')
        Unidate=request.POST.get('Unidate')
        Unimarks=request.POST.get('Unimarks')
        Unigrading=request.POST.get('Unigrading')
        UniDoc=request.FILES['UniDoc']

        name2=fs.save(UniDoc.name,UniDoc)
        url2=fs.url(name2)
        Testeng=request.POST.get('Testeng')
        Yeareng=request.POST.get('Yeareng')
        Overallscoreeng=request.POST.get('Overallscoreeng')


        Testeng1=request.POST.get('Testeng1')
        Yeareng1=request.POST.get('Yeareng1')
        Overallscoreeng1=request.POST.get('Overallscoreeng1')


        Testad=request.POST.get('Testad')
        Yearad=request.POST.get('Yearad')
        Overallscoread=request.POST.get('Overallscoread')


        Testad1=request.POST.get('Testad')
        Yearad1=request.POST.get('Yearad')
        Overallscoread1=request.POST.get('Overallscoread1')


        Applyingfor=request.POST.get('Applyingfor')
        Date=request.POST.get('Date')
        pcoun1=request.POST.get('pcoun1')
        pcoun2=request.POST.get('pcoun2')
        pcoun3=request.POST.get('pcoun3')
        pcour4=request.POST.get('pcour4')
        pcour5=request.POST.get('pcour5')
        pcour6=request.POST.get('pcour6')
        try:
            Uploadeng=request.FILES['Uploadeng']
            name3=fs.save(Uploadeng.name,Uploadeng)
            url3=fs.url(name3)

            Uploadeng1=request.FILES['Uploadeng1']
            name4=fs.save(Uploadeng1.name,Uploadeng1)
            url4=fs.url(Uploadeng1)

            Uploadad=request.FILES['Uploadad']
            name5=fs.save(Uploadad.name,Uploadad)
            url5=fs.url(name5)

            Uploadad1=request.FILES['Uploadad1']
            name6=fs.save(Uploadad1.name,Uploadad1)
            url6=fs.url(name6)
        except:
            Uploadeng=None
            Uploadeng1=None
            Uploadad=None
            Uploadad1=None
            url3=None
            url4=None
            url5=None
            url6=None
        Email1=request.session['Email']
        error_message=None
        if(Email1!=Email):
            error_message="ohh your email doesn't matched with login mail"
            return render(request,'Admin_portal/stddetail.html',{'error':error_message})

        else:
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
            'Sscqual':Sscqual,'Sscname':Sscname,'Sscdate':Sscdate,'Sscmarks':Sscmarks,'Sscgrading':Sscgrading,'SscDoc':url,
            'Intqual':Intqual,'Intname':Intname,'Intdate':Intdate,'Intmarks':Intmarks,'Intgrading':Intgrading,
            'IntDoc':url1,'Uniqual':Uniqual,'Uniname':Uniname,'Unicname':Unicname,'Unidate':Unidate,'Unimarks': Unimarks,
            'Unigrading':Unigrading,'UniDoc':url2,
            'Testeng': Testeng,'Yeareng':Yeareng,'Overallscoreeng': Overallscoreeng,'Uploadeng':url3,
            'Testeng1': Testeng1,'Yeareng1':Yeareng1,'Overallscoreeng1': Overallscoreeng1,'Uploadeng1':url4,
            'Testad': Testad,'Yearad': Yearad,'Overallscoread':Overallscoread,'Uploadad':url5,
            'Testad1': Testad1,'Yearad1': Yearad1,'Overallscoread1':Overallscoread1,'Uploadad1':url6,
            'Applyingfor':Applyingfor,'Date':Date,'pcoun1':pcoun1,'pcoun2':pcoun2,'pcoun3':pcoun3,'pcour4':pcour4,'pcour5':pcour5,'pcour6':pcour6}
            print(value['Firstname'])
            print(value['SscDoc'])
            data={'value':value}

            return redirect('home')
