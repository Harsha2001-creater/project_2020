from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse


def stdhome(request):
    return render(request,'student_portal/studenthome.html')
def stdnav(request):
    return render(request,'student_portal/studentnav.html')
def stdsaved(request):
    return render(request,'student_portal/studentsaved.html')
def stdunivlist(request):
    return render(request,'student_portal/university_cards.html')
