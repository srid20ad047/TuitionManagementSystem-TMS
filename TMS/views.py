from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import NinthClass, TenthClass, EleventhClass, TwelvethClass, IXPayment, XPayment, XIPayment, XIIPayment , NinthAttendance , TenthAttendance , EleventhAttendance , TwelvethAttendance
from datetime import datetime
from collections import defaultdict

# Create your views here.

def index(request):
    return render(request, 'tms/index.html')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('index')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        curr_user = authenticate(username=username, password=password)
        print(curr_user)
        if curr_user is not None:
            login(request, curr_user)
            return redirect('index')
        else:
            return render(request, 'tms/pages/samples/login.html')
    else:
        return render(request, 'tms/pages/samples/login.html')


def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')


def attendance_call(request, title):
    print(title)

    if title == "9":
        li = []
        details = NinthClass.objects.all()
        date = request.POST.get('date')
        for i in details:
            value = request.POST.get(i.STUDENT_ID)
            IXattendance = NinthAttendance(STUDENT_ID=i.STUDENT_ID, NAME=i.NAME, DATE=date, STATUS=value)
            IXattendance.save()
    elif title == "10":
        li = []
        details = TenthClass.objects.all()
        date = request.POST.get('date')
        for i in details:
            value = request.POST.get(i.STUDENT_ID)
            Xattendance = TenthAttendance(STUDENT_ID=i.STUDENT_ID, NAME=i.NAME, DATE=date, STATUS=value)
            Xattendance.save()
    elif title == "11":
        li = []
        details = EleventhClass.objects.all()
        date = request.POST.get('date')
        for i in details:
            value = request.POST.get(i.STUDENT_ID)
            XIattendance = EleventhAttendance(STUDENT_ID=i.STUDENT_ID, NAME=i.NAME, DATE=date, STATUS=value)
            XIattendance.save()
    elif title == "12":
        li = []
        details = TwelvethClass.objects.all()
        date = request.POST.get('date')
        for i in details:
            value = request.POST.get(i.STUDENT_ID)
            XIIattendance = TwelvethAttendance(STUDENT_ID=i.STUDENT_ID, NAME=i.NAME, DATE=date, STATUS=value)
            XIIattendance.save()
    return redirect('attendance')


def payment(request):
    if request.method == 'POST':
        NAME = request.POST.get('name')
        CLASS = request.POST.get('class')
        DATE_OF_PAYMENT = request.POST.get('date_of_payment')
        NET_AMOUNT_PAID = request.POST.get('net_amount_paid')
        MODE_OF_PAYMENT = request.POST.get('mode_of_payment')
        STUDENT_ID = request.POST.get('student_id')
        SUBJECT = request.POST.get('subject')

        if (CLASS == "9th"):
            if IXPayment.objects.count() < 10:
                date = datetime.strptime(DATE_OF_PAYMENT, "%Y-%m-%d")
                month = date.strftime("%b")
                PAYMENT_ID = "IX-FEE-" + month + "0" + str(IXPayment.objects.count() + 1)
                det = IXPayment(NAME=NAME, CLASS=CLASS, DATE_OF_PAYMENT=DATE_OF_PAYMENT,
                                NET_AMOUNT_PAID=NET_AMOUNT_PAID, MODE_OF_PAYMENT=MODE_OF_PAYMENT,
                                PAYMENT_RECEIPT_ID=PAYMENT_ID, STUD_ID=STUDENT_ID, SUBJECT=SUBJECT)
                det.save()
            elif IXPayment.objects.count() >= 10:
                date = datetime.strptime(DATE_OF_PAYMENT, "%Y-%m-%d")
                month = date.strftime("%b")
                PAYMENT_ID = "IX-FEE-" + month + str(IXPayment.objects.count() + 1)
                det = IXPayment(NAME=NAME, CLASS=CLASS, DATE_OF_PAYMENT=DATE_OF_PAYMENT,
                                NET_AMOUNT_PAID=NET_AMOUNT_PAID, MODE_OF_PAYMENT=MODE_OF_PAYMENT, PAYMENT_RECEIPT_ID=PAYMENT_ID, STUD_ID=STUDENT_ID, SUBJECT=SUBJECT)
                det.save()


        if (CLASS == "10th"):
            if XPayment.objects.count() < 10:
                date = datetime.strptime(DATE_OF_PAYMENT, "%Y-%m-%d")
                month = date.strftime("%b")
                PAYMENT_ID = "X-FEE-" + month + "0" + str(XPayment.objects.count() + 1)
                det = XPayment(NAME=NAME, CLASS=CLASS, DATE_OF_PAYMENT=DATE_OF_PAYMENT, NET_AMOUNT_PAID=NET_AMOUNT_PAID,
                               MODE_OF_PAYMENT=MODE_OF_PAYMENT, PAYMENT_RECEIPT_ID=PAYMENT_ID, STUD_ID=STUDENT_ID, SUBJECT=SUBJECT)
                det.save()
            elif XPayment.objects.count() >= 10:
                date = datetime.strptime(DATE_OF_PAYMENT, "%Y-%m-%d")
                month = date.strftime("%b")
                PAYMENT_ID = "X-FEE-" + month + str(XPayment.objects.count() + 1)
                det = XPayment(NAME=NAME, CLASS=CLASS, DATE_OF_PAYMENT=DATE_OF_PAYMENT, NET_AMOUNT_PAID=NET_AMOUNT_PAID,
                               MODE_OF_PAYMENT=MODE_OF_PAYMENT, PAYMENT_RECEIPT_ID=PAYMENT_ID, STUD_ID=STUDENT_ID, SUBJECT=SUBJECT)
                det.save()



        if (CLASS == "11th"):
            if XIPayment.objects.count() < 10:
                date = datetime.strptime(DATE_OF_PAYMENT, "%Y-%m-%d")
                month = date.strftime("%b")
                PAYMENT_ID = "XI-FEE-" + month + "0" + str(XIPayment.objects.count() + 1)
                det = XIPayment(NAME=NAME, CLASS=CLASS, DATE_OF_PAYMENT=DATE_OF_PAYMENT,
                                NET_AMOUNT_PAID=NET_AMOUNT_PAID, MODE_OF_PAYMENT=MODE_OF_PAYMENT,
                                PAYMENT_RECEIPT_ID=PAYMENT_ID, STUD_ID=STUDENT_ID, SUBJECT=SUBJECT)
                det.save()
            elif XIPayment.objects.count() >= 10:
                date = datetime.strptime(DATE_OF_PAYMENT, "%Y-%m-%d")
                month = date.strftime("%b")
                PAYMENT_ID = "XI-FEE-" + month + str(XIPayment.objects.count() + 1)
                det = XIPayment(NAME=NAME, CLASS=CLASS, DATE_OF_PAYMENT=DATE_OF_PAYMENT,
                                NET_AMOUNT_PAID=NET_AMOUNT_PAID, MODE_OF_PAYMENT=MODE_OF_PAYMENT, PAYMENT_RECEIPT_ID=PAYMENT_ID, STUD_ID=STUDENT_ID, SUBJECT=SUBJECT)
                det.save()

        if (CLASS == "12th"):
            if XIIPayment.objects.count() < 10:
                date = datetime.strptime(DATE_OF_PAYMENT, "%Y-%m-%d")
                month = date.strftime("%b")
                PAYMENT_ID = "XII-FEE-" + month + "0" + str(XIIPayment.objects.count() + 1)
                det = XIIPayment(NAME=NAME, CLASS=CLASS, DATE_OF_PAYMENT=DATE_OF_PAYMENT,
                                 NET_AMOUNT_PAID=NET_AMOUNT_PAID, MODE_OF_PAYMENT=MODE_OF_PAYMENT,
                                 PAYMENT_RECEIPT_ID=PAYMENT_ID, STUD_ID=STUDENT_ID, SUBJECT=SUBJECT)
                det.save()
            elif XIIPayment.objects.count() >= 10:
                date = datetime.strptime(DATE_OF_PAYMENT, "%Y-%m-%d")
                month = date.strftime("%b")
                PAYMENT_ID = "XII-FEE-" + month + str(XIIPayment.objects.count() + 1)
                det = XIIPayment(NAME=NAME, CLASS=CLASS, DATE_OF_PAYMENT=DATE_OF_PAYMENT,
                                 NET_AMOUNT_PAID=NET_AMOUNT_PAID, MODE_OF_PAYMENT=MODE_OF_PAYMENT,
                                 PAYMENT_RECEIPT_ID=PAYMENT_ID, STUD_ID=STUDENT_ID, SUBJECT=SUBJECT)
                det.save()

        return render(request, 'tms/payment.html')

    data = NinthClass.objects.all()
    val1 = []
    id1= []
    subject1 = []
    amount1 = []

    for i in data:
        id1.append(i.STUDENT_ID)
        val1.append(i.NAME)
        subject1.append(i.SUBJECT)
        amount1.append(i.TOTAL)
    print(val1)

    data = TenthClass.objects.all()
    val2 = []
    id2 = []
    amount2 = []
    subject2 = []
    for i in data:
        id2.append(i.STUDENT_ID)
        val2.append(i.NAME)
        subject2.append(i.SUBJECT)
        amount2.append(i.TOTAL)
    print(val2)


    data = EleventhClass.objects.all()
    val3 = []
    id3 = []
    amount3 = []
    subject3 = []
    for i in data:
        id3.append(i.STUDENT_ID)
        val3.append(i.NAME)
        subject3.append(i.SUBJECT)
        amount3.append(i.TOTAL)
    print(val3)


    data = TwelvethClass.objects.all()
    val4 = []
    id4 = []
    amount4 = []
    subject4 = []
    for i in data:
        id4.append(i.STUDENT_ID)
        val4.append(i.NAME)
        subject4.append(i.SUBJECT)
        amount4.append(i.TOTAL)
    print(val4)



    return render(request, 'tms/payment.html',{'data': data, 'val1': val1, 'val2': val2, 'val3': val3, 'val4': val4,'id1': id1, 'id2': id2, 'id3': id3, 'id4': id4,'amount1': amount1, 'amount2': amount2, 'amount3': amount3, 'amount4': amount4,'subject1': subject1, 'subject2': subject2, 'subject3': subject3, 'subject4': subject4})


def register(request):
    if request.method == 'POST':
        NAME = request.POST.get('name')
        Medium = request.POST.get('medium')
        gender = request.POST.get('gender')
        join_date = request.POST.get('join_date')
        subject = request.POST.get('subject')
        class_name = request.POST.get('class_name')
        phone_number = request.POST.get('phone_number')
        price = request.POST.get('price')
        discount = request.POST.get('discount')
        total = request.POST.get('total')

        if (class_name == "9th"):
            if (Medium == "cbse" and NinthClass.objects.count() < 10):
                Student_id = "IXCBSE0" + str(NinthClass.objects.count() + 1)
                det = NinthClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,
                                 SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,
                                 DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "cbse" and NinthClass.objects.count() > 9):
                Student_id = "IXCBSE" + str(NinthClass.objects.count() + 1)
                det = NinthClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,
                                 SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,
                                 DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "state" and NinthClass.objects.count() < 10):
                Student_id = "IXSB0" + str(NinthClass.objects.count() + 1)
                det = NinthClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,
                                 SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,
                                 DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "state" and NinthClass.objects.count() > 9):
                Student_id = "IXSB" + str(NinthClass.objects.count() + 1)
                det = NinthClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,
                                 SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,
                                 DISCOUNT=discount, TOTAL=total)
                det.save()

        elif (class_name == "10th"):
            if (Medium == "cbse" and TenthClass.objects.count() < 10):
                Student_id = "XCBSE0" + str(TenthClass.objects.count() + 1)
                det = TenthClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,
                                 SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,
                                 DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "cbse" and TenthClass.objects.count() > 9):
                Student_id = "XCBSE" + str(TenthClass.objects.count() + 1)
                det = TenthClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,
                                 SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,
                                 DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "state" and TenthClass.objects.count() < 10):
                Student_id = "XSB0" + str(TenthClass.objects.count() + 1)
                det = TenthClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,
                                 SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,
                                 DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "state" and TenthClass.objects.count() > 9):
                Student_id = "XSB" + str(TenthClass.objects.count() + 1)
                det = TenthClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,
                                 SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,
                                 DISCOUNT=discount, TOTAL=total)
                det.save()

        elif (class_name == "11th"):
            if (Medium == "cbse" and EleventhClass.objects.count() < 10):
                Student_id = "XICBSE0" + str(EleventhClass.objects.count() + 1)
                det = EleventhClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,
                                    SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,
                                    DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "cbse" and EleventhClass.objects.count() > 9):
                Student_id = "XICBSE" + str(EleventhClass.objects.count() + 1)
                det = EleventhClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,
                                    SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,
                                    DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "state" and EleventhClass.objects.count() < 10):
                Student_id = "XISB0" + str(EleventhClass.objects.count() + 1)
                det = EleventhClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,
                                    SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,
                                    DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "state" and EleventhClass.objects.count() > 9):
                Student_id = "XISB" + str(EleventhClass.objects.count() + 1)
                det = EleventhClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,
                                    SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,
                                    DISCOUNT=discount, TOTAL=total)
                det.save()

        elif (class_name == "12th"):
            if (Medium == "cbse" and TwelvethClass.objects.count() < 10):
                Student_id = "XIICBSE0" + str(TwelvethClass.objects.count() + 1)
                det = TwelvethClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,
                                    SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,
                                    DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "cbse" and TwelvethClass.objects.count() > 9):
                Student_id = "XIICBSE" + str(TwelvethClass.objects.count() + 1)
                det = TwelvethClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,
                                    SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,
                                    DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "state" and TwelvethClass.objects.count() < 10):
                Student_id = "XIISB0" + str(TwelvethClass.objects.count() + 1)
                det = TwelvethClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,
                                    SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,
                                    DISCOUNT=discount, TOTAL=total)
                det.save()
            elif (Medium == "state" and TwelvethClass.objects.count() > 9):
                Student_id = "XIISB" + str(TwelvethClass.objects.count() + 1)
                det = TwelvethClass(NAME=NAME, STUDENT_ID=Student_id, MEDIUM=Medium, GENDER=gender, JOIN_DATE=join_date,
                                    SUBJECT=subject, CLASS=class_name, PHONE_NUMBER=phone_number, PRICE=price,
                                    DISCOUNT=discount, TOTAL=total)
                det.save()

        return render(request, 'tms/register.html')
    return render(request, 'tms/register.html')


def base(request):
    return render(request, 'tms/base.html')


def display(request):
    return render(request, 'tms/display.html',
                  {"data_nine": NinthClass.objects.all(), "data_ten": TenthClass.objects.all(),
                   "data_eleven": EleventhClass.objects.all(), "data_twelve": TwelvethClass.objects.all()})


def stud_details(request):
    return render(request, 'tms/stud_details.html')


def admin(request):
    return render(request, 'adminpage')


def attendance(request):
    return render(request, 'tms/attendance.html',
                  {'data_nine': NinthClass.objects.all(), 'data_ten': TenthClass.objects.all(),
                   'data_eleven': EleventhClass.objects.all(), 'data_twelve': TwelvethClass.objects.all()})

def attendanceReport(request):
    nine_details = defaultdict(list)
    for i in NinthClass.objects.all():
        nine_details["Name"].append(i.NAME)
    for i in NinthAttendance.objects.all():
        nine_details[i.DATE].append(i.STATUS)
    ten_details = defaultdict(list)
    for i in TenthClass.objects.all():
        ten_details["Name"].append(i.NAME)
    for i in TenthAttendance.objects.all():
        ten_details[i.DATE].append(i.STATUS)
    eleven_details = defaultdict(list)
    for i in EleventhClass.objects.all():
        eleven_details["Name"].append(i.NAME)
    for i in EleventhAttendance.objects.all():
        eleven_details[i.DATE].append(i.STATUS)
    twelve_details = defaultdict(list)
    for i in TwelvethClass.objects.all():
        twelve_details["Name"].append(i.NAME)
    for i in TwelvethAttendance.objects.all():
        twelve_details[i.DATE].append(i.STATUS)
    print(nine_details)
    return render(request, 'tms/attendance_display.html',{'nine_details' : dict(nine_details),'ten_details' : dict(ten_details),'eleven_details' : dict(eleven_details),'twelve_details' : dict(twelve_details)})
