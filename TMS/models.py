from django.db import models

# Create your models here.

class NinthClass(models.Model):
    NAME = models.CharField(max_length=100)
    STUDENT_ID = models.CharField(max_length=100)
    CBSE_STATE = models.CharField(max_length=100)
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
    STUDENT_ID = models.CharField(max_length=100)
    CBSE_STATE = models.CharField(max_length=100)
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
    STUDENT_ID = models.CharField(max_length=100)
    CBSE_STATE = models.CharField(max_length=100)
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
    STUDENT_ID = models.CharField(max_length=100)
    CBSE_STATE = models.CharField(max_length=100)
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