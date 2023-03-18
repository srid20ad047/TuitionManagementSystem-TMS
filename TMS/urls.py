from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser, name='login'),
    path('logoutUser',views.logoutUser,name='logoutUser'),
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('display', views.display, name='display'),
    path('details', views.stud_details, name='details'),
    path('admin', views.admin, name='adminpage'),
    path('attendance', views.attendance, name='attendance'),
    path('attendance/<slug:title>',views.attendance_call, name='attendance'),
    path('payment', views.payment, name='payment'),
    path('attendanceReport', views.attendanceReport, name='attendanceReport'),
    # path('home', views.home, name='home'),
]