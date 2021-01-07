from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views.studentlogin import studentlogin
from .views.universitylogin import universitylogin
from .views.mediator import home
from .views.mediator import signup_mediator
from .views.mediator import login_mediator

#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
path('',home,name='home'),
path('studentlogin',studentlogin.as_view(),name='studentloginpage'),
path('universitylogin',universitylogin.as_view(),name='universityloginpage'),
path('password-reset', auth_views.PasswordResetView.as_view(template_name="login/password_reset.html"),name='password_reset'),
path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name="login/password_reset_done.html"),name='password_reset_done'),
path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="login/password_reset_confirm.html"),name='password_reset_confirm'),
path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name="login/password_reset_complete.html"),name='password_reset_complete'),
path('signup-mediator',signup_mediator,name='signup-mediator'),
path('login-mediator',login_mediator,name='login-mediator'),

]
#urlpatterns+=staticfiles_urlpatterns
