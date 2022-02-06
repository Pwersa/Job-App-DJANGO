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
    full_name = models.CharField(verbose_name='full_name' ,max_length=99)
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
    from1 = models.DateField(verbose_name='from1')
    to1 = models.DateField(verbose_name='to1')
    company2 = models.CharField(verbose_name='company2',max_length=99)
    position2 = models.CharField(verbose_name='position2',max_length=99)
    from2 = models.DateField(verbose_name='from2')
    to2 = models.DateField(verbose_name='to2')
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
    job = models.CharField(verbose_name='job',max_length=99, default="Applicant")
    account_type = models.CharField(verbose_name='account_type',max_length=99, default="Applicant")
    signature = models.ImageField(verbose_name='signature',default="")
    

class job_listing(models.Model):
    jtitle = models.CharField(primary_key = True , verbose_name='job_title', max_length=99)
    jdesc = models.TextField(verbose_name='job_description', max_length=300)
    no_dipl = models.BooleanField(verbose_name='no_diploma')
    hs_grad = models.BooleanField(verbose_name='highschool_graduate')
    col_grad = models.BooleanField(verbose_name='college_graduate')
    no_char = models.BooleanField(verbose_name='no_character_reference_needed')
    char_ref1 = models.BooleanField(verbose_name='1_character_reference_needed')
    char_ref2 = models.BooleanField(verbose_name='2_character_reference_needed')
    salary = models.PositiveIntegerField(verbose_name='salary')

class interview(models.Model):
    name = models.CharField(verbose_name='name' ,max_length=99)
    applying_for = models.CharField(verbose_name='applying_for',max_length=99)
    date_time =  models.DateField(verbose_name='date_time')
    email_add = models.EmailField(primary_key = True, verbose_name='email_add')