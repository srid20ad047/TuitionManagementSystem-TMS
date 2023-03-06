from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser, name='login'),
    path('logoutUser',views.logoutUser,name='logoutUser'),
    path('index', views.index, name='index'),
    path('base', views.base, name='base'),
    path('buttons', views.buttons, name='buttons'),
    path('dropdowns', views.dropdowns, name='dropdowns'),
    path('topology', views.topology, name='topology'),
    path('basic_element', views.basic_element, name='basic_element'),
    path('charts', views.charts, name='charts'),
    path('mdi', views.mdi, name='mdi'),
    path('blank_page', views.blank_page, name='blank_page'),
    path('error_404', views.error_404, name='error_404'),
    path('error_500', views.error_500, name='error_500'),
    path('documentation', views.documentation, name='documentation'),
    path('register', views.register, name='register'),
    path('display', views.display, name='display'),
    path('details', views.stud_details, name='details'),
    path('admin', views.admin, name='adminpage'),
]