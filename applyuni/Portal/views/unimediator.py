from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from Portal.models.universityinfo import University
from Portal.models.univdetail import Univdetail
from django.views import View

def Uniappli(request):
    return render(request,'University_portal/application_box.html')
def Unihome(request):
    return render(request,'University_portal/university_home.html')
def Unisupport(request):
    return render(request,'University_portal/support.html')

class Unisettings(View):
    def get(self,request):
        
        univdetail=Univdetail.get_univdetail_by_email(request.session['university_Email'])
        print("Nanda Anumolu")


        print(univdetail.Coursename)
        value={'Institutemode': univdetail.Institutemode,'Institutetype': univdetail.Institutetype,'Year':univdetail.Year,'Rank':univdetail.Rank,'About':univdetail.About,'Campuses':univdetail.Campuses,
        'Departments' :univdetail.Departments,'Education':univdetail.Education,'Feeug':univdetail.Feeug,'Feepg':univdetail.Feepg,'Intake': univdetail.Intake,'Awards':univdetail.Awards,
        'Staff':univdetail.Staff,'Students':univdetail.Students,'Location':univdetail.Location,'Phonenumber':univdetail.Phonenumber,'Email':univdetail.Email,

        'Applyfee':univdetail.Applyfee,'Currency':univdetail.Currency,'Amount':univdetail.Amount,'Applyform':univdetail.Applyform,'Duration':univdetail.Duration,
        'Applypro1':univdetail.Applypro1,'Applypro2':univdetail.Applypro2,'Applypro3':univdetail.Applypro3,'Applypro4':univdetail.Applypro4,'Doc1':univdetail.Doc1,'Doc2':univdetail.Doc2,
        'Doc3':univdetail.Doc3,'Doc4':univdetail.Doc4,'Doc5':univdetail.Doc5,'Doc6':univdetail.Doc6,'Doc7':univdetail.Doc7,'Doc8':univdetail.Doc8,'Doc9':univdetail.Doc9,'Term1':univdetail.Term1,
        'Term2':univdetail.Term2,'Term3':univdetail.Term3,'Term4':univdetail.Term4,
        
        'Coursename':univdetail.Coursename,'Coursetype':univdetail.Coursetype,'Facultyname':univdetail.Facultyname,'Courseapproval':univdetail.Courseapproval,
        'Approvalauthority':univdetail.Approvalauthority,'Tutionfee':univdetail.Tutionfee,'Amount1':univdetail.Amount1,'Sem1':univdetail.Sem1,'Sem2':univdetail.Sem2,'Sem3':univdetail.Sem3,'Sem4':univdetail.Sem4,
        'Sem5':univdetail.Sem5,'Sem6':univdetail.Sem6,'Duration1':univdetail.Duration1,'Noofsems':univdetail.Noofsems,'Criteria1':univdetail.Criteria1,'Criteria2':univdetail.Criteria2,'Criteria3':univdetail.Criteria3}
        data={'value':value}

        return render(request,'University_portal/university_settings.html',data)
    def post(self,request):
        Institutemode= request.POST.get('Institutemode')
        Institutetype= request.POST.get('Institutetype')
        Year=request.POST.get('Year')
        Rank=request.POST.get('Rank')
        About=request.POST.get('About')
        Campuses=request.POST.get('Campuses')
        Departments = request.POST.get('Departments')
        Education=request.POST.get('Education')
        Feeug=request.POST.get('Feeug')
        Feepg=request.POST.get('Feepg')
        Intake= request.POST.get('Intake')
        Awards=request.POST.get('Awards')
        Staff=request.POST.get('Staff')
        Students=request.POST.get('Students')
        Location=request.POST.get('Location')
        Phonenumber=request.POST.get('Phonenumber')
        Email=request.POST.get('Email')

        Applyfee=request.POST.get('Applyfee')
        Currency=request.POST.get('Currency')
        Amount=request.POST.get('Amount')
        Applyform=request.FILES.get('Applyform')
        Duration=request.POST.get('Duration')
        Applypro1=request.POST.get('Applypro1')
        Applypro2=request.POST.get('Applypro2')
        Applypro3=request.POST.get('Applypro3')
        Applypro4=request.POST.get('Applypro4')
        Doc1=request.POST.get('Doc1')
        Doc2=request.POST.get('Doc2')
        Doc3=request.POST.get('Doc3')
        Doc4=request.POST.get('Doc4')
        Doc5=request.POST.get('Doc5')
        Doc6=request.POST.get('Doc6')
        Doc7=request.POST.get('Doc7')
        Doc8=request.POST.get('Doc8')
        Doc9=request.POST.get('Doc9')
        Term1=request.POST.get('Term1')
        Term2=request.POST.get('Term2')
        Term3=request.POST.get('Term3')
        Term4=request.POST.get('Term4')

        #####course page

        Coursename=request.POST.get('coursename')
        Coursetype=request.POST.get('coursetype')
        Facultyname=request.POST.get('facultyname')
        Courseapproval=request.POST.get('courseapproval')
        Approvalauthority=request.POST.get('approval')
        Tutionfee=request.POST.get('fee')
        Amount1=request.POST.get('amount1')
        Sem1=request.POST.get('sem1')
        Sem2=request.POST.get('sem2')
        Sem3=request.POST.get('sem3')
        Sem4=request.POST.get('sem4')
        Sem5=request.POST.get('sem5')
        Sem6=request.POST.get('sem6')
        Duration1=request.POST.get('duration1')
        Noofsems=request.POST.get('noofsems')
        Criteria1=request.POST.get('criteria1')
        Criteria2=request.POST.get('criteria2')
        Criteria3=request.POST.get('criteria3')

        ####end
        value={'Institutemode': Institutemode,'Institutetype': Institutetype,'Year':Year,'Rank':Rank,'About':About,'Campuses':Campuses,
        'Departments' : Departments,'Education':Education,'Feeug':Feeug,'Feepg':Feepg,'Intake': Intake,'Awards':Awards,
        'Staff':Staff,'Students':Students,'Location':Location,'Phonenumber':Phonenumber,'Email':Email,

        'Applyfee':Applyfee,'Currency':Currency,'Amount':Amount,'Applyform':Applyform,'Duration':Duration,
        'Applypro1':Applypro1,'Applypro2':Applypro2,'Applypro3':Applypro3,'Applypro4':Applypro4,'Doc1':Doc1,'Doc2':Doc2,
        'Doc3':Doc3,'Doc4':Doc4,'Doc5':Doc5,'Doc6':Doc6,'Doc7':Doc7,'Doc8':Doc8,'Doc9':Doc9,'Term1':Term1,
        'Term2':Term2,'Term3':Term3,'Term4':Term4,
        
        'Coursename':Coursename,'Coursetype':Coursetype,'Facultyname':Facultyname,'Courseapproval':Courseapproval,
        'Approvalauthority':Approvalauthority,'Tutionfee':Tutionfee,'Amount1':Amount1,'Sem1':Sem1,'Sem2':Sem2,'Sem3':Sem3,'Sem4':Sem4,
        'Sem5':Sem5,'Sem6':Sem6,'Duration1':Duration1,'Noofsems':Noofsems,'Criteria1':Criteria1,'Criteria2':Criteria2,'Criteria3':Criteria3}


        univdetail=Univdetail(Institutemode= Institutemode,Institutetype= Institutetype,Year=Year,Rank=Rank,About=About,
        Campuses=Campuses,
        Departments = Departments,Education=Education,Feeug=Feeug,Feepg=Feepg,Intake= Intake,Awards=Awards,
        Staff=Staff,Students=Students,Location=Location,Phonenumber=Phonenumber,Email=Email,

        Applyfee=Applyfee,Currency=Currency,Amount=Amount,Applyform=Applyform,Duration=Duration,
        Applypro1=Applypro1,Applypro2=Applypro2,Applypro3=Applypro3,Applypro4=Applypro4,Doc1=Doc1,Doc2=Doc2,
        Doc3=Doc3,Doc4=Doc4,Doc5=Doc5,Doc6=Doc6,Doc7=Doc7,Doc8=Doc8,Doc9=Doc9,Term1=Term1,
        Term2=Term2,Term3=Term3,Term4=Term4,
        
        Coursename=Coursename,Coursetype=Coursetype,Facultyname=Facultyname,Courseapproval=Courseapproval,
        Approvalauthority=Approvalauthority,Tutionfee=Tutionfee,Amount1=Amount1,Sem1=Sem1,Sem2=Sem2,Sem3=Sem3,Sem4=Sem4,
        Sem5=Sem5,Sem6=Sem6,Duration1=Duration1,Noofsems=Noofsems,Criteria1=Criteria1,Criteria2=Criteria2,Criteria3=Criteria3)


        university1=University.get_university_by_email(Email)

        univdetail1=Univdetail.get_univdetail_by_email(university1.Universitymail)
        print(univdetail1)
        print("monish")
        if(univdetail1):
            univdetail1.delete()
        univdetail.register()






        data={'value':value}
        return render(request,'University_portal/university_settings.html',data)
