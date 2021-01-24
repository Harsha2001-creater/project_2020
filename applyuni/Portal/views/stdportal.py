from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from Portal.models.universityinfo import University

def stdhome(request):
    value={'Name':request.session['Firstname']}
    data={'value':value}
    return render(request,'student_portal/studenthome.html',data)
def stdnav(request):
    return render(request,'student_portal/studentnav.html')
def stdsaved(request):
    return render(request,'student_portal/studentsaved.html')
def stdunivlist(request):
    total_univs=University.objects.all()
    data={}
    data['total_univs']=total_univs
    return render(request,'student_portal/university_cards.html',data)
