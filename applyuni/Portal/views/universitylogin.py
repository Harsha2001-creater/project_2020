from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from Portal.models.universityinfo import University
from Portal.models.univdetail import Univdetail

from django.views import View
class universitylogin(View):
    return_url = None
    def get(self,request):
        universitylogin.return_url = request.GET.get('return_url')
        return render(request,'login/universitylogin.html')

    def post(self,request):
        Email=request.POST.get('Universitymail')
        Password=request.POST.get('Password')
        university=University.get_university_by_email(Email)
        error_message= None

        if university:
            flag= (Password==university.Password)
            if flag:
                request.session['university_Email']=university.Universitymail
                request.session['name']=university.Universityname
                if(university):
                    univdetail=Univdetail.get_univdetail_by_email(university.Universitymail)
                print(univdetail)
                if(univdetail):
                    print("kis")
                    print(univdetail.Year)
                    value={'Institutemode': univdetail.Institutemode,'Institutetype': univdetail.Institutetype,'Year':univdetail.Year,'Rank':univdetail.Rank,'About':univdetail.About,'Campuses':univdetail.Campuses,
                    'Departments' :univdetail.Departments,'Education':univdetail.Education,'Feeug':univdetail.Feeug,'Feepg':univdetail.Feepg,'Intake': univdetail.Intake,'Awards':univdetail.Awards,
                    'Staff':univdetail.Staff,'Students':univdetail.Students,'Location':univdetail.Location,'Phonenumber':univdetail.Phonenumber,'Email':univdetail.Email,

                    'Applyfee':univdetail.Applyfee,'Currency':univdetail.Currency,'Amount':univdetail.Amount,'Applyform':univdetail.Applyform,'Duration':univdetail.Duration,
                    'Applypro1':univdetail.Applypro1,'Applypro2':univdetail.Applypro2,'Applypro3':univdetail.Applypro3,'Applypro4':univdetail.Applypro4,'Doc1':univdetail.Doc1,'Doc2':univdetail.Doc2,
                    'Doc3':univdetail.Doc3,'Doc4':univdetail.Doc4,'Doc5':univdetail.Doc5,'Doc6':univdetail.Doc6,'Doc7':univdetail.Doc7,'Doc8':univdetail.Doc8,'Doc9':univdetail.Doc9,'Term1':univdetail.Term1,
                    'Term2':univdetail.Term2,'Term3':univdetail.Term3,'Term4':univdetail.Term4}
                    data={'value':value}
                    return render(request,'University_portal/university_settings.html',data)
                else:
                    return render(request,'University_portal/university_settings.html')
                '''
                if universitylogin.return_url():
                    return HttpResponseRedirect(return_url)
                else:
                    universitylogin.return_url=None
                    return redirect('homepage')
                    '''
            else:
                error_message='Password is invalid!!!'
                return render(request,'login/universitylogin.html',{'error': error_message})
        else:
            error_message='Email is invalid!!!'
            return render(request,'login/universitylogin.html',{'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('universityloginpage')
