from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from Portal.models.universityinfo import University
from Portal.models.univdetail import Univdetail
from Portal.models.saved import Saved
from django.views import View

def stdhome(request):
    value={'Name':request.session['Firstname']}
    data={'value':value}
    return render(request,'student_portal/studenthome.html',data)
def stdnav(request):
    return render(request,'student_portal/studentnav.html')
def stdsaved(request):
    return render(request,'student_portal/studentsaved.html')
def stdunivlist(request):
    
    print("coming")
    search=request.POST.get('Search')
    print(search)
    if(search):
        total_univs=University.objects.filter(Universityname__icontains=search)
    else:
        print("in else")
        total_univs=University.objects.all()
        print("taking total univs done")
    data={}
    data['total_univs']=total_univs
    return render(request,'student_portal/university_cards.html',data)

class saved(View): 
    def get(self,request,name="a"):
        saved_univ=Saved.objects.filter(Mail=request.session['Email'])
        print(saved_univ)
        data={}
        for i in saved_univ:
            print(i.Universityname)
        #print(saved_univ.Univerisityname)
        data['saved_univ']=saved_univ
        print("nanda")
        return render(request,'student_portal/studentsaved.html',data)
    def post(self,request,name="a"):
        university=University.objects.get(Universityname=name)
        univdetail=Univdetail.objects.get(Email=university.Universitymail)
        name=university.Universityname
        About=univdetail.About
        Mail=request.session['Email']
        
        print(request.session['Email'])
        flag=Saved.objects.filter(Mail=Mail)
        print(flag)
        print(name)
        print("##")
        count=0
        for i in flag:
            count=0
            print(i.Universityname)
            if i.Universityname == name:
                count=1
            if count == 1:
                break
        if count == 0:
            saved=Saved(Universityname=name,About=About,Mail=Mail)
            saved.register()
            print("anumolu")
            return redirect('stdunivlist')
        else:
            return redirect('stdunivlist')
        
def delete(request,name):

     university=Saved.objects.get(Universityname=name)
     university.delete()
     return redirect('stdsaved')