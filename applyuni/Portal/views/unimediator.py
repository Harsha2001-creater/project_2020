from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from Portal.models.universityinfo import University
from Portal.models.univdetail import Univdetail
from Portal.models.newcourse import Newcourse
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

def Uniappli(request):
    return render(request,'University_portal/application_box.html')
def Unihome(request):
    return render(request,'University_portal/university_home.html')
def Unisupport(request):
    return render(request,'University_portal/support.html')
def Unilogout(request):
    request.session.clear()
    return redirect('universityloginpage')

class Unisettings(View):
    def get(self,request):

        try:

            univdetail=Univdetail.get_univdetail_by_email(request.session['university_Email'])
            print("Nanda Anumolu")
            univ_courses=Newcourse.objects.filter(Universitymail=request.session['university_Email'])

            value={'Institutemode': univdetail.Institutemode,'Institutetype': univdetail.Institutetype,'Year':univdetail.Year,'Rank':univdetail.Rank,'About':univdetail.About,'Campuses':univdetail.Campuses,
            'Departments' :univdetail.Departments,'Education':univdetail.Education,'Feeug':univdetail.Feeug,'Feepg':univdetail.Feepg,'Intake': univdetail.Intake,'Awards':univdetail.Awards,
            'Staff':univdetail.Staff,'Students':univdetail.Students,'Location':univdetail.Location,'Phonenumber':univdetail.Phonenumber,'Email':univdetail.Email,

            'Applyfee':univdetail.Applyfee,'Currency':univdetail.Currency,'Amount':univdetail.Amount,'Applyform':univdetail.Applyform,'Duration':univdetail.Duration,
            'Applypro1':univdetail.Applypro1,'Applypro2':univdetail.Applypro2,'Applypro3':univdetail.Applypro3,'Applypro4':univdetail.Applypro4,'Doc1':univdetail.Doc1,'Doc2':univdetail.Doc2,
            'Doc3':univdetail.Doc3,'Doc4':univdetail.Doc4,'Doc5':univdetail.Doc5,'Doc6':univdetail.Doc6,'Doc7':univdetail.Doc7,'Doc8':univdetail.Doc8,'Doc9':univdetail.Doc9,'Term1':univdetail.Term1,
            'Term2':univdetail.Term2,'Term3':univdetail.Term3,'Term4':univdetail.Term4,

            }
            data={'value':value,'univ_courses':univ_courses}

            return render(request,'University_portal/university_settings.html',data)
        except:
            return render(request,'University_portal/university_settings.html')
    def post(self,request):
        univdetail=Univdetail.get_univdetail_by_email(request.session['university_Email'])
        Institutemode= request.POST.get('Institutemode')
        if(Institutemode==None):
            try:
                Institutemode=univdetail.Institutemode
            except:
                Institutemode=None
        Institutetype= request.POST.get('Institutetype')
        if(Institutetype==None):
            try:
                Institutetype=univdetail.Institutetype
            except:
                Institutetype=None
        Year=request.POST.get('Year')
        if(Year==None):
            try:
                Year=univdetail.Year
            except:
                Year=None
            print(Year)
        Rank=request.POST.get('Rank')
        if(Rank==None):
            try:
                Rank=univdetail.Rank
            except:
                Rank=None
        About=request.POST.get('About')
        if(About==None):
            try:
                About=univdetail.About
            except:
                About=None
        Campuses=request.POST.get('Campuses')
        if(Campuses==None):
            try:
                Campuses=univdetail.Campuses
            except:
                Campuses=None
        Departments = request.POST.get('Departments')
        if(Departments==None):
            try:
                Departments=univdetail.Departments
            except:
                Departments=None
        Education=request.POST.get('Education')
        if(Education==None):
            try:
                Education=univdetail.Education
            except:
                Education=None
        Feeug=request.POST.get('Feeug')
        if(Feeug==None):
            try:
                Feeug=univdetail.Feeug
            except:
                Feeug=None
        Feepg=request.POST.get('Feepg')
        if(Feepg==None):
            try:
                Feepg=univdetail.Feepg
            except:
                Feepg=None
        Intake= request.POST.get('Intake')
        if(Intake==None):
            try:
                Intake=univdetail.Intake
            except:
                Intake=None
        Awards=request.POST.get('Awards')
        if(Awards==None):
            try:
                Awards=univdetail.Awards
            except:
                Awards=None
        Staff=request.POST.get('Staff')
        if(Staff==None):
            try:
                Staff=univdetail.Staff
            except:
                Staff=None
        Students=request.POST.get('Students')
        if(Students==None):
            try:
                Students=univdetail.Students
            except:
                Students=None
        Location=request.POST.get('Location')
        if(Location==None):
            try:
                Location=univdetail.Location
            except:
                Location=None
        Phonenumber=request.POST.get('Phonenumber')
        if(Phonenumber==None):
            try:
                Phonenumber=univdetail.Phonenumber
            except:
                Phonenumber=None
        Email=request.POST.get('Email')
        if(Email==None):
            try:
                Email=univdetail.Email
            except:
                Email=None
        Applyfee=request.POST.get('Applyfee')
        if(Applyfee==None):
            try:
                Applyfee=univdetail.Applyfee
            except:
                Applyfee=None
        Currency=request.POST.get('Currency')
        if(Currency==None):
            try:
                Currency=univdetail.Currency
            except:
                Currency=None
        Amount=request.POST.get('Amount')
        if(Amount==None):
            try:
                Amount=univdetail.Amount
            except:
                Amount=None
        Applyform=request.FILES.get('Applyform')
        if(Applyform==None):
            try:
                Applyform=univdetail.Applyform
            except:
                Applyform=None
        Duration=request.POST.get('Duration')
        if(Duration==None):
            try:
                Duration=univdetail.Duration
            except:
                Duration=None
        Applypro1=request.POST.get('Applypro1')
        if(Applypro1==None):
            try:
                Applypro1=univdetail.Applypro1
            except:
                Applypro1=None
        Applypro2=request.POST.get('Applypro2')
        if(Applypro2==None):
            try:
                Applypro2=univdetail.Applypro2
            except:
                Applypro2=None
        Applypro3=request.POST.get('Applypro3')
        if(Applypro3==None):
            try:
                Applypro3=univdetail.Applypro3
            except:
                Applypro3=None
        Applypro4=request.POST.get('Applypro4')
        if(Applypro4==None):
            try:
                Applypro4=univdetail.Applypro4
            except:
                Applypro4=None
        Doc1=request.POST.get('Doc1')
        if(Doc1==None):
            try:
                Doc1=univdetail.Doc1
            except:
                Doc1=None
        Doc2=request.POST.get('Doc2')
        if(Doc2==None):
            try:
                Doc2=univdetail.Doc2
            except:
                Doc2=None
        Doc3=request.POST.get('Doc3')
        if(Doc3==None):
            try:
                Doc3=univdetail.Doc3
            except:
                Doc3=None
        Doc4=request.POST.get('Doc4')
        if(Doc4==None):
            try:
                Doc4=univdetail.Doc4
            except:
                Doc4=None
        Doc5=request.POST.get('Doc5')
        if(Doc5==None):
            try:
                Doc5=univdetail.Doc5
            except:
                Doc5=None
        Doc6=request.POST.get('Doc6')
        if(Doc6==None):
            try:
                Doc6=univdetail.Doc6
            except:
                Doc6=None
        Doc7=request.POST.get('Doc7')
        if(Doc7==None):
            try:
                Doc7=univdetail.Doc7
            except:
                Doc7=None
        Doc8=request.POST.get('Doc8')
        if(Doc8==None):
            try:
                Doc8=univdetail.Doc8
            except:
                Doc8=None
        Doc9=request.POST.get('Doc9')
        if(Doc9==None):
            try:
                Doc9=univdetail.Doc9
            except:
                Doc9=None
        Term1=request.POST.get('Term1')
        if(Term1==None):
            try:
                Term1=univdetail.Term1
            except:
                Term1=None
        Term2=request.POST.get('Term2')
        if(Term2==None):
            try:
                Term2=univdetail.Term2
            except:
                Term2=None
        Term3=request.POST.get('Term3')
        if(Term3==None):
            try:
                Term3=univdetail.Term3
            except:
                Term3=None
        Term4=request.POST.get('Term4')
        if(Term4==None):
            try:
                Term4=univdetail.Term4
            except:
                Term4=None
        
        #####course page


        ####end
        value={'Institutemode': Institutemode,'Institutetype': Institutetype,'Year':Year,'Rank':Rank,'About':About,'Campuses':Campuses,
        'Departments' : Departments,'Education':Education,'Feeug':Feeug,'Feepg':Feepg,'Intake': Intake,'Awards':Awards,
        'Staff':Staff,'Students':Students,'Location':Location,'Phonenumber':Phonenumber,'Email':Email,

        'Applyfee':Applyfee,'Currency':Currency,'Amount':Amount,'Applyform':Applyform,'Duration':Duration,
        'Applypro1':Applypro1,'Applypro2':Applypro2,'Applypro3':Applypro3,'Applypro4':Applypro4,'Doc1':Doc1,'Doc2':Doc2,
        'Doc3':Doc3,'Doc4':Doc4,'Doc5':Doc5,'Doc6':Doc6,'Doc7':Doc7,'Doc8':Doc8,'Doc9':Doc9,'Term1':Term1,
        'Term2':Term2,'Term3':Term3,'Term4':Term4

        }


        univdetail=Univdetail(Institutemode= Institutemode,Institutetype= Institutetype,Year=Year,Rank=Rank,About=About,
        Campuses=Campuses,
        Departments = Departments,Education=Education,Feeug=Feeug,Feepg=Feepg,Intake= Intake,Awards=Awards,
        Staff=Staff,Students=Students,Location=Location,Phonenumber=Phonenumber,Email=Email,

        Applyfee=Applyfee,Currency=Currency,Amount=Amount,Applyform=Applyform,Duration=Duration,
        Applypro1=Applypro1,Applypro2=Applypro2,Applypro3=Applypro3,Applypro4=Applypro4,Doc1=Doc1,Doc2=Doc2,
        Doc3=Doc3,Doc4=Doc4,Doc5=Doc5,Doc6=Doc6,Doc7=Doc7,Doc8=Doc8,Doc9=Doc9,Term1=Term1,
        Term2=Term2,Term3=Term3,Term4=Term4
        )


        university1=University.get_university_by_email(request.session['university_Email'])

        univdetail1=Univdetail.get_univdetail_by_email(university1.Universitymail)
        print(univdetail1)
        print("monish")
        if(univdetail1):
            univdetail1.delete()
        univdetail.register()



        univ_courses=Newcourse.objects.filter(Universitymail=request.session['university_Email'])


        data={'value':value,'univ_courses':univ_courses}

        #password
        university1=University.get_university_by_email(request.session['university_Email'])
        print(university1.Univcontactnumber)
        a=university1.Password
        Password=request.POST.get('Password')
        Confirmpassword=request.POST.get('Confirmpassword')
        Confirmpassword1=request.POST.get('Confirmpassword1')
        error_message=None
        flag=check_password(Password,a)

        if(flag):
            if(Confirmpassword == Confirmpassword1):

                university1.Password=make_password(Confirmpassword)
                university1.Confirmpassword=make_password(Confirmpassword1)
                university1.register()
                return render(request,'University_portal/university_settings.html',data)
            else:

                error_message='Password and current password doesnt match !!!'
                data['error']=error_message
                return render(request,'University_portal/university_settings.html',data)
        else:
            error_message='Current Password is invalid!!!'
            data['error']=error_message
            return render(request,'University_portal/university_settings.html',data)
