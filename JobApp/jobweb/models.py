from ensurepip import version
from operator import mod
from pickle import TRUE
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.

class account_data(models.Model):
    email = models.EmailField(primary_key = True , verbose_name='email')
    password = models.CharField(verbose_name='password', max_length=20)
    photo = models.ImageField(verbose_name='photo')
    first_name = models.CharField(verbose_name='first_name' ,max_length=99, default="")
    middle_name = models.CharField(verbose_name='middle_name' ,max_length=99, default="")
    last_name = models.CharField(verbose_name='last_name' ,max_length=99, default="")
    address = models.CharField(verbose_name='address' ,max_length=99)
    cellphone = models.CharField(verbose_name='cellphone' ,max_length=11)
    birthday = models.DateField(verbose_name='birthday')
    bplace = models.CharField(verbose_name='bplace' ,max_length=99)
    civilstatus = models.CharField(verbose_name='civilstatus' ,max_length=99)
    citizenship = models.CharField(verbose_name='citizenship' ,max_length=99)
    religion = models.CharField(verbose_name='religion' ,max_length=99)
    e_contact = models.CharField(verbose_name='e_contact' ,max_length=99)
    e_no = models.CharField(verbose_name='e_no' ,max_length=11)
    elementary = models.CharField(verbose_name='elementary' ,max_length=99)
    elementary_grad = models.CharField(verbose_name='elementary_grad' ,max_length=99)
    highschool = models.CharField(verbose_name='highschool' ,max_length=99)
    highschool_grad = models.CharField(verbose_name='highschool_grad' ,max_length=99)
    college = models.CharField(verbose_name='college' ,max_length=99)
    college_grad = models.CharField(verbose_name='college_grad' ,max_length=99)
    company1 = models.CharField(verbose_name='company1',max_length=99)
    position1 = models.CharField(verbose_name='position1',max_length=99)
    from1 = models.CharField(verbose_name='from_1' ,max_length=99)
    to1 = models.CharField(verbose_name='to_1' ,max_length=99, default="")
    company2 = models.CharField(verbose_name='company2',max_length=99, default="")
    position2 = models.CharField(verbose_name='position2',max_length=99)
    from2 = models.CharField(verbose_name='from_2' ,max_length=99, default="")
    to2 = models.CharField(verbose_name='to_2' ,max_length=99, default="")
    ref1 = models.CharField(verbose_name='ref1',max_length=99, default="")
    refcon1 = models.CharField(verbose_name='refcon1',max_length=99, default="")
    refpos1 = models.CharField(verbose_name='refpos1',max_length=99, default="")
    refcom1 = models.CharField(verbose_name='refcom1',max_length=99, default="")
    ref2 = models.CharField(verbose_name='ref2',max_length=99, default="")
    refcon2 = models.CharField(verbose_name='refcon2',max_length=99, default="")
    refpos2 = models.CharField(verbose_name='refpos2',max_length=99, default="")
    refcom2 = models.CharField(verbose_name='refcom2',max_length=99, default="")
    philhealth = models.CharField(verbose_name='philhealth', max_length=12)
    pagibig = models.CharField(verbose_name='pagibig', max_length=12)
    TIN = models.CharField(verbose_name='TIN', max_length= 9)
    NBI = models.CharField(verbose_name='NBI', max_length=6)
    SSS = models.CharField(verbose_name='SSS', max_length=10)
    med_record = models.CharField(verbose_name='med_record', max_length=6)
    applyingfor = models.CharField(verbose_name='applyingfor',max_length=99)
    job = models.CharField(verbose_name='job',max_length=99, default='Applicant')
    account_type = models.CharField(verbose_name='account_type',max_length=99, default='Applicant')
    signature = models.ImageField(verbose_name='signature',default="")
    #name = last_name + first_name + middle_name
    

class job_listing(models.Model):
    jtitle = models.CharField(primary_key = True , verbose_name='jtitle', max_length=99)
    jdesc = models.TextField(verbose_name='jdesc', max_length=300)
    jobreq1 = models.CharField(verbose_name='jobreq1', default="No Diploma Needed", max_length=99)
    jobreq2 = models.CharField(verbose_name='jobreq2', default="No Reference Needed" , max_length=99)
    salary = models.PositiveIntegerField(verbose_name='salary')

class interview(models.Model):
    name = models.CharField(verbose_name='name' ,max_length=99)
    applying_for = models.CharField(verbose_name='applying_for',max_length=99)
    date_time =  models.DateField(verbose_name='date_time')
    email_add = models.EmailField(primary_key = True, verbose_name='email_add')
