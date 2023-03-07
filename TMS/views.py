from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import NinthClass,TenthClass,EleventhClass,TwelvethClass

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
        Medium =request.POST.get('medium')
        gender = request.POST.get('gender')
        join_date = request.POST.get('join_date')
        subject = request.POST.get('subject')
        class_name = request.POST.get('class_name')
        phone_number = request.POST.get('phone_number')
        price = request.POST.get('price')
        discount = request.POST.get('discount')
        total = request.POST.get('total')
        print(NAME,gender,join_date,subject,class_name,phone_number,price,discount,total)
        if (class_name=="9th"):
            if(Medium=="cbse" and NinthClass.objects.count()<10):
                Student_id = "IXCBSE0"+str(NinthClass.objects.count()+1)
                det=NinthClass(NAME=NAME,STUDENT_ID=Student_id,MEDIUM=Medium,GENDER=gender,JOIN_DATE=join_date,SUBJECT=subject,CLASS=class_name,PHONE_NUMBER=phone_number,PRICE=price,DISCOUNT=discount,TOTAL=total)
                det.save()
            elif(Medium=="cbse" and NinthClass.objects.count()>9):
                Student_id = "IXCBSE" + str(NinthClass.objects.count() + 1)
                det = NinthClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender,JOIN_DATE=join_date, SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number,PRICE=price, DISCOUNT=discount, TOTAL=total)
                det.save()
            elif(Medium=="state" and NinthClass.objects.count()<10):
                Student_id = "IXSB0" + str(NinthClass.objects.count() + 1)
                det = NinthClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,DISCOUNT=discount, TOTAL=total)
                det.save()
            elif(Medium=="state" and NinthClass.objects.count()>9):
                Student_id = "IXSB" + str(NinthClass.objects.count() + 1)
                det = NinthClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,DISCOUNT=discount, TOTAL=total)
                det.save()

        elif(class_name=="10th"):
            if (Medium == "cbse" and TenthClass.objects.count() < 10):
                Student_id = "XCBSE0" + str(TenthClass.objects.count() + 1)
                det = TenthClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "cbse" and TenthClass.objects.count() > 9):
                Student_id = "XCBSE" + str(TenthClass.objects.count() + 1)
                det = TenthClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "state" and TenthClass.objects.count() < 10):
                Student_id = "XSB0" + str(TenthClass.objects.count() + 1)
                det = TenthClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "state" and TenthClass.objects.count() > 9):
                Student_id = "XSB" + str(TenthClass.objects.count() + 1)
                det = TenthClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,DISCOUNT=discount, TOTAL=total)
                det.save()

        elif (class_name=="11th"):
            if (Medium == "cbse" and EleventhClass.objects.count() < 10):
                Student_id = "XICBSE0" + str(EleventhClass.objects.count() + 1)
                det = EleventhClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "cbse" and EleventhClass.objects.count() > 9):
                Student_id = "XICBSE" + str(EleventhClass.objects.count() + 1)
                det = EleventhClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "state" and EleventhClass.objects.count() < 10):
                Student_id = "XISB0" + str(EleventhClass.objects.count() + 1)
                det = EleventhClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "state" and EleventhClass.objects.count() > 9):
                Student_id = "XISB" + str(EleventhClass.objects.count() + 1)
                det = EleventhClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,DISCOUNT=discount, TOTAL=total)
                det.save()

        elif (class_name=="12th"):
            if (Medium == "cbse" and TwelvethClass.objects.count() < 10):
                Student_id = "XIICBSE0" + str(TwelvethClass.objects.count() + 1)
                det = TwelvethClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "cbse" and TwelvethClass.objects.count() > 9):
                Student_id = "XIICBSE" + str(TwelvethClass.objects.count() + 1)
                det = TwelvethClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "state" and TwelvethClass.objects.count() < 10):
                Student_id = "XIISB0" + str(TwelvethClass.objects.count() + 1)
                det = TwelvethClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "state" and TwelvethClass.objects.count() > 9):
                Student_id = "XIISB" + str(TwelvethClass.objects.count() + 1)
                det = TwelvethClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date, SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price, DISCOUNT=discount, TOTAL=total)
                det.save()

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
def basic_element(request):
    return render(request,'tms/pages/forms/basic_elements.html')
def display(request):
    return render(request,'tms/display.html',{"data_nine":NinthClass.objects.all(),"data_ten":TenthClass.objects.all(),"data_eleven":EleventhClass.objects.all(),"data_twelve":TwelvethClass.objects.all()})
def stud_details(request):
    return render(request,'tms/stud_details.html')
def admin(request):
    return render(request,'adminpage')
def attendance(request):
    return render(request,'tms/attendance.html')