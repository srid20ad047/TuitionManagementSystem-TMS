from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginUser, name='login'),
    path('logoutUser',views.logoutUser,name='logoutUser'),
    path('index', views.index, name='index'),
    path('base', views.base, name='base'),
    path('buttons', views.buttons, name='buttons'),
    path('dropdowns', views.dropdowns, name='dropdowns'),
    path('topology', views.topology, name='topology'),
    path('basic_elements', views.basic_elements, name='basic_elements'),
    path('basic_table', views.basic_table, name='basic_table'),
    path('charts', views.charts, name='charts'),
    path('mdi', views.mdi, name='mdi'),
    path('blank_page', views.blank_page, name='blank_page'),
    path('error_404', views.error_404, name='error_404'),
    path('error_500', views.error_500, name='error_500'),
    path('documentation', views.documentation, name='documentation'),
    path('register', views.register, name='register'),
]