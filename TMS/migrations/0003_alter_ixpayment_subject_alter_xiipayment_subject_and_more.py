# Generated by Django 4.1.7 on 2023-03-18 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0002_eleventhattendance_ninthattendance_tenthattendance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ixpayment',
            name='SUBJECT',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='xiipayment',
            name='SUBJECT',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='xipayment',
            name='SUBJECT',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='xpayment',
            name='SUBJECT',
            field=models.CharField(max_length=100),
        ),
    ]