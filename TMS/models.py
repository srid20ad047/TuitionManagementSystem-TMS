from django.db import models

# Create your models here.

class NinthClass(models.Model):
    NAME = models.CharField(max_length=100)
    MEDIUM = models.CharField(max_length=100)
    STUDENT_ID = models.CharField(max_length=100)
    GENDER = models.CharField(max_length=100)
    JOIN_DATE = models.CharField(max_length=100)
    SUBJECT = models.CharField(max_length=100)
    CLASS = models.CharField(max_length=100)
    PHONE_NUMBER = models.CharField(max_length=100)
    PRICE = models.CharField(max_length=100)
    DISCOUNT = models.CharField(max_length=100)
    TOTAL = models.CharField(max_length=100)
    def __str__(self):
        return self.NAME
class TenthClass(models.Model):
    NAME = models.CharField(max_length=100)
    MEDIUM = models.CharField(max_length=100)
    STUDENT_ID = models.CharField(max_length=100)
    GENDER = models.CharField(max_length=100)
    JOIN_DATE = models.CharField(max_length=100)
    SUBJECT = models.CharField(max_length=100)
    CLASS = models.CharField(max_length=100)
    PHONE_NUMBER = models.CharField(max_length=100)
    PRICE = models.CharField(max_length=100)
    DISCOUNT = models.CharField(max_length=100)
    TOTAL = models.CharField(max_length=100)
    def __str__(self):
        return self.NAME
class EleventhClass(models.Model):
    NAME = models.CharField(max_length=100)
    MEDIUM = models.CharField(max_length=100)
    STUDENT_ID = models.CharField(max_length=100)
    GENDER = models.CharField(max_length=100)
    JOIN_DATE = models.CharField(max_length=100)
    SUBJECT = models.CharField(max_length=100)
    CLASS = models.CharField(max_length=100)
    PHONE_NUMBER = models.CharField(max_length=100)
    PRICE = models.CharField(max_length=100)
    DISCOUNT = models.CharField(max_length=100)
    TOTAL = models.CharField(max_length=100)
    def __str__(self):
        return self.NAME
class TwelvethClass(models.Model):
    NAME = models.CharField(max_length=100)
    MEDIUM = models.CharField(max_length=100)
    STUDENT_ID = models.CharField(max_length=100)
    GENDER = models.CharField(max_length=100)
    JOIN_DATE = models.CharField(max_length=100)
    SUBJECT = models.CharField(max_length=100)
    CLASS = models.CharField(max_length=100)
    PHONE_NUMBER = models.CharField(max_length=100)
    PRICE = models.CharField(max_length=100)
    DISCOUNT = models.CharField(max_length=100)
    TOTAL = models.CharField(max_length=100)
    def __str__(self):
        return self.NAME


class IXPayment(models.Model):
    STUD_ID = models.CharField(max_length=100)
    PAYMENT_RECEIPT_ID = models.CharField(max_length=100)
    NAME = models.CharField(max_length=100)
    CLASS = models.CharField(max_length=100)
    DATE_OF_PAYMENT = models.CharField(max_length=100)
    NET_AMOUNT_PAID = models.CharField(max_length=100)
    MODE_OF_PAYMENT = models.CharField(max_length=100)

    def __str__(self):
        return self.NAME

class XPayment(models.Model):
    STUD_ID = models.CharField(max_length=100)
    PAYMENT_RECEIPT_ID = models.CharField(max_length=100)
    NAME = models.CharField(max_length=100)
    CLASS = models.CharField(max_length=100)
    DATE_OF_PAYMENT = models.CharField(max_length=100)
    NET_AMOUNT_PAID = models.CharField(max_length=100)
    MODE_OF_PAYMENT = models.CharField(max_length=100)

    def __str__(self):
        return self.NAME

class XIPayment(models.Model):
    STUD_ID = models.CharField(max_length=100)
    PAYMENT_RECEIPT_ID = models.CharField(max_length=100)
    NAME = models.CharField(max_length=100)
    CLASS = models.CharField(max_length=100)
    DATE_OF_PAYMENT = models.CharField(max_length=100)
    NET_AMOUNT_PAID = models.CharField(max_length=100)
    MODE_OF_PAYMENT = models.CharField(max_length=100)

    def __str__(self):
        return self.NAME

class XIIPayment(models.Model):
    STUD_ID = models.CharField(max_length=100)
    PAYMENT_RECEIPT_ID = models.CharField(max_length=100)
    NAME = models.CharField(max_length=100)
    CLASS = models.CharField(max_length=100)
    DATE_OF_PAYMENT = models.CharField(max_length=100)
    NET_AMOUNT_PAID = models.CharField(max_length=100)
    MODE_OF_PAYMENT = models.CharField(max_length=100)

    def __str__(self):
        return self.NAME

class NinthAttendance(models.Model):
    NAME = models.CharField(max_length=100)
    STUDENT_ID = models.CharField(max_length=100)
    DATE = models.CharField(max_length=100)
    STATUS = models.CharField(max_length=100)
    def __str__(self):
        return self.NAME

class TenthAttendance(models.Model):
    NAME = models.CharField(max_length=100)
    STUDENT_ID = models.CharField(max_length=100)
    DATE = models.CharField(max_length=100)
    STATUS = models.CharField(max_length=100)
    def __str__(self):
        return self.NAME

class EleventhAttendance(models.Model):
    NAME = models.CharField(max_length=100)
    STUDENT_ID = models.CharField(max_length=100)
    DATE = models.CharField(max_length=100)
    STATUS = models.CharField(max_length=100)
    def __str__(self):
        return self.NAME

class TwelvethAttendance(models.Model):
    NAME = models.CharField(max_length=100)
    STUDENT_ID = models.CharField(max_length=100)
    DATE = models.CharField(max_length=100)
    STATUS = models.CharField(max_length=100)
    def __str__(self):
        return self.NAME