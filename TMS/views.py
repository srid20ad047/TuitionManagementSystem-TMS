from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, 'tms/index.html')
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('index')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        curr_user = authenticate(username=username,password=password)
        print(curr_user)
        if curr_user is not None:
            login(request,curr_user)
            return redirect('index')
        else:
            return render(request,'tms/pages/samples/login.html')
    else:
        return render(request,'tms/pages/samples/login.html')

def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        NAME = request.POST.get('name')
        gender = request.POST.get('gender')
        join_date = request.POST.get('join_date')
        subject = request.POST.get('subject')
        class_name = request.POST.get('class')
        phone_number = request.POST.get('phone_number')
        price = request.POST.get('price')
        discount = request.POST.get('discount')
        total = request.POST.get('total')
        print(NAME,gender,join_date,subject,class_name,phone_number,price,discount,total)
        return render(request,'tms/register.html')
    return render(request,'tms/register.html')

def base(request):
    return render(request, 'tms/base.html')
def buttons(request):
    return render(request, 'tms/pages/ui-features/buttons.html')
def dropdowns(request):
    return render(request, 'tms/pages/ui-features/dropdowns.html')
def topology(request):
    return render(request, 'tms/pages/ui-features/typography.html')

def charts(request):
    return render(request, 'tms/pages/charts/chartjs.html')
def mdi(request):
    return render(request, 'tms/pages/icons/mdi.html')
def blank_page(request):
    return render(request, 'tms/pages/samples/blank-page.html')
def error_404(request):
    return render(request, 'tms/pages/samples/error-404.html')
def error_500(request):
    return render(request, 'tms/pages/samples/error-500.html')

def documentation(request):
    return render(request, 'tms/pages/documentation/documentation.html')

def register(request):
    return render(request,'tms/register.html')

def basic_element(request):
    return render(request,'tms/pages/forms/basic_elements.html')
def display(request):
    return render(request,'tms/display.html')

def stud_details(request):
    return render(request,'tms/stud_details.html')
def admin(request):
    return render(request,'adminpage')
