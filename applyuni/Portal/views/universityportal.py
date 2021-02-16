from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from Portal.models.newcourse import Newcourse

class Universityportal(View):
    def get(self,request):
        return render(request,'University_portal/newcourse.html')

    def post(self,request):
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
        Universitymail=request.session['university_Email']

        newcourse=Newcourse(Coursename=Coursename,Coursetype=Coursetype,Facultyname=Facultyname,Courseapproval=Courseapproval,
        Approvalauthority=Approvalauthority,Tutionfee=Tutionfee,Amount1=Amount1,Sem1=Sem1,Sem2=Sem2,Sem3=Sem3,Sem4=Sem4,
        Sem5=Sem5,Sem6=Sem6,Duration1=Duration1,Noofsems=Noofsems,Criteria1=Criteria1,Criteria2=Criteria2,Criteria3=Criteria3,Universitymail=Universitymail)

        newcourse.register()

        return redirect('Unisettings')
