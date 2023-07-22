from django.urls import path
from .import views

urlpatterns = [

path('',views.index,name='index'),
path('about/',views.about,name='about'),
path('contact/',views.contact,name='contact'),
path('register/',views.registration,name='register'),
path('signin/',views.signin,name='signin'),
path('signout/',views.signout,name='signout'),
path('dashboard/',views.dashboard,name='dashboard'),
path('course_signup/',views.course_signup,name='course_signup'),
path('profile/',views.profile1,name='profile'),
path('profile_edit/',views.profile_edit,name='profile_edit'),
path('change_pass/',views.change_pass,name='change_pass'),
path('forget_pass/',views.forget_pass,name='forget_pass'),
path('otp/',views.otp,name='otp'),
path('search/',views.search,name='search'),
path('signedup/',views.signedup,name='signedup'),
]