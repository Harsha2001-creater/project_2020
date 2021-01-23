from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views.studentlogin import studentlogin
from .views.universitylogin import universitylogin
from .views.mediator import home
from .views.mediator import signup_mediator
from .views.mediator import login_mediator
from .views.studentsignup import studentsignup
from .views.universitysignup import universitysignup
from .views.facebook import HomeView
from django.views.generic import TemplateView
from .views.stdquery import stdquery
from .views.stddetail import stddetail
from .views import stddetail1
from .views.unimediator import Uniappli
from .views.unimediator import Unihome
from .views.unimediator import Unisupport
from .views.unimediator import Unisettings
from .views.unihome1 import unihome1
from .views.overview import overview
from .views.stdportal import stdhome
from .views.stdportal import stdnav
from .views.stdportal import stdsaved
from .views.payment import payment
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
path('',home,name='home'),
path('facebook', HomeView.as_view(), name='facebook'),
#path('google', HomeView.as_view(), name='google'),
path('google', TemplateView.as_view(template_name="login/studentlogin.html")),
path('accounts/', include('allauth.urls')),
path('stddetail1',stddetail1.home,name='stddetail1'),
path('oauth/', include('social_django.urls', namespace='social')),
path('studentlogin',studentlogin.as_view(),name='studentloginpage'),
path('universitylogin',universitylogin.as_view(),name='universityloginpage'),
path('password-reset', auth_views.PasswordResetView.as_view(template_name="login/password_reset.html"),name='password_reset'),
path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name="login/password_reset_done.html"),name='password_reset_done'),
path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="login/password_reset_confirm.html"),name='password_reset_confirm'),
path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name="login/password_reset_complete.html"),name='password_reset_complete'),

path('studentsignup',studentsignup.as_view(),name='studentsignup'),
path('universitysignup',universitysignup.as_view(),name='universitysignup'),
path('signup-mediator',signup_mediator,name='signup-mediator'),
path('login-mediator',login_mediator,name='login-mediator'),
path('stdquery',stdquery.as_view(),name='stdquery'),
path('stddetail',stddetail.as_view(),name='stddetail'),

#university portal
path('applications',Uniappli,name='uniappli'),
path('unihome',Unihome,name='unihome'),
path('support',Unisupport,name='Unisupport'),
path('unisettings',Unisettings.as_view(),name='Unisettings'),
path('unihome1',unihome1.as_view(),name='unihome1'),
path('overview',overview.as_view(),name='overview'),

#student Portal
path('stdhome',stdhome,name='stdhome'),
path('stdnav',stdnav,name='stdnav'),
path('stdsaved',stdsaved,name='stdsaved'),
path('payment',payment,name='payment')
]
#urlpatterns+=staticfiles_urlpatterns
