from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from Portal.models.universityinfo import University
from django.views import View
class universitylogin(View):
    return_url = None
    def get(self,request):
        universitylogin.return_url = request.GET.get('return_url')
        return render(request,'login/universitylogin.html')

    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        university=University.get_university_by_email(email)
        error_message= None

        if university:
            flag= (password==student.password)
            if flag:
                request.session['university']=university.id
                request.session['name']=university.name
                '''
                if universitylogin.return_url():
                    return HttpResponseRedirect(return_url)
                else:
                    universitylogin.return_url=None
                    return redirect('homepage')
                    '''
            else:
                error_message='Password is invalid!!!'
        else:
            error_message='Email is invalid!!!'
        return render(request,'login/universitylogin.html',{'error': error_message})
def logout(request):
    request.session.clear()
    return redirect('universityloginpage')
