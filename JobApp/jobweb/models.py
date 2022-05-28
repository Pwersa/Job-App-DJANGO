from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class account_registration(AbstractUser):
    
    #applyingfor1 = [('Choice1', 'Please select here')]

    username = models.EmailField(primary_key=True, verbose_name='username', unique=True, default="")
    password1 = models.CharField(verbose_name='password1', max_length=20, default="")
    password2 = models.CharField(verbose_name='password2', max_length=20, default="")
    photo = models.ImageField(verbose_name='photo', null=True, upload_to="picture/")
    first_name = models.CharField(verbose_name='first_name' ,max_length=99, default="")
    middle_name = models.CharField(verbose_name='middle_name' ,max_length=99, default="")
    last_name = models.CharField(verbose_name='last_name' ,max_length=99, default="")
    address = models.CharField(verbose_name='address' ,max_length=99)
    cellphone = models.CharField(verbose_name='cellphone' ,max_length=11)
    birthday = models.DateField(verbose_name='birthday', null=True, blank=False)
    applyingfor = models.CharField(verbose_name='applyingfor',max_length=99, default="")
    job = models.CharField(verbose_name='job',max_length=99, default='Applicant')
    employment_status = models.CharField(verbose_name='job',max_length=99, default='Not yet Employed')
    account_type = models.CharField(verbose_name='account_type',max_length=99)
    verified_user = models.BooleanField(verbose_name='verified_user', max_length=99, default=False)


    USERNAME_FIELD = 'username'

class other_info(models.Model):

    citizenship_options = [('Single', 'Single'), 
                            ('Married', 'Married'), 
                            ('Widowed', 'Widowed'),
                            ]

    username = models.ForeignKey(account_registration, primary_key=True, on_delete=models.CASCADE, default="")
    bplace = models.CharField(verbose_name='bplace' ,max_length=99, null=True)
    civilstatus = models.CharField(verbose_name='civilstatus' ,max_length=99, null=True, choices=citizenship_options)
    citizenship = models.CharField(verbose_name='citizenship' ,max_length=99, null=True)
    religion = models.CharField(verbose_name='religion' ,max_length=99, null=True)
    e_contact = models.CharField(verbose_name='e_contact' ,max_length=99, null=True)
    e_no = models.CharField(verbose_name='e_no', max_length=99, null=True)
    elementary = models.CharField(verbose_name='elementary' ,max_length=99, null=True)
    elementary_grad = models.CharField(verbose_name='elementary_grad', max_length=99, null=True)
    highschool = models.CharField(verbose_name='highschool' ,max_length=99, null=True)
    highschool_grad = models.CharField(verbose_name='highschool_grad', max_length=99, null=True)
    college = models.CharField(verbose_name='college' ,max_length=99, null=True)
    college_grad = models.CharField(verbose_name='college_grad', max_length=99, null=True)
    company1 = models.CharField(verbose_name='company1',max_length=99, null=True)
    position1 = models.CharField(verbose_name='position1',max_length=99, null=True)
    from1 = models.CharField(verbose_name='from_1' ,max_length=99, null=True)
    to1 = models.CharField(verbose_name='to_1' ,max_length=99, null=True)
    company2 = models.CharField(verbose_name='company2',max_length=99, null=True, blank=True)
    position2 = models.CharField(verbose_name='position2', max_length=99, null=True, blank=True)
    from2 = models.CharField(verbose_name='from_2' ,max_length=99,  null=True, blank=True)
    to2 = models.CharField(verbose_name='to_2' ,max_length=99, null=True, blank=True)
    ref1 = models.CharField(verbose_name='ref1',max_length=99, null=True)
    refcon1 = models.CharField(verbose_name='refcon1', max_length=99, null=True)
    refpos1 = models.CharField(verbose_name='refpos1',max_length=99, null=True)
    refcom1 = models.CharField(verbose_name='refcom1',max_length=99, null=True)
    ref2 = models.CharField(verbose_name='ref2',max_length=99, null=True, blank=True)
    refcon2 = models.CharField(verbose_name='refcon2', max_length=99, null=True, blank=True)
    refpos2 = models.CharField(verbose_name='refpos2',max_length=99, null=True, blank=True)
    refcom2 = models.CharField(verbose_name='refcom2',max_length=99, null=True, blank=True)
    philhealth = models.CharField(verbose_name='philhealth', max_length=99, null=True, blank=True)
    pagibig = models.CharField(verbose_name='pagibig', max_length=99, null=True, blank=True)
    TIN = models.CharField(verbose_name='TIN', max_length=99, null=True, blank=True)
    NBI = models.CharField(verbose_name='NBI', max_length=99, null=True, blank=True)
    SSS = models.CharField(verbose_name='SSS', max_length=99, null=True, blank=True)
    med_record = models.CharField(verbose_name='med_record', max_length=6, null=True, blank=True)
    signature = models.ImageField(verbose_name='signature', null=True, default="No photo", upload_to="signature/")
    

    USERNAME_FIELD = 'username'
    
class job_listing(models.Model):
    jtitle = models.CharField(primary_key = True, verbose_name='jtitle', max_length=99)
    jdesc = models.TextField(verbose_name='jdesc', max_length=300)
    jobreq1 = models.CharField(verbose_name='jobreq1', default="No Diploma Needed", max_length=99)
    jobreq2 = models.CharField(verbose_name='jobreq2', default="No Reference Needed" , max_length=99)
    salary = models.PositiveIntegerField(verbose_name='salary')

class interview(models.Model):
    username = models.ForeignKey(account_registration, primary_key=True, on_delete=models.CASCADE, default="")
    first_name = models.CharField(verbose_name='first_name' ,max_length=99,  null=True)
    middle_name = models.CharField(verbose_name='middle_name' ,max_length=99, null=True)
    last_name = models.CharField(verbose_name='last_name' ,max_length=99, null=True)
    jitle = models.ForeignKey(job_listing, verbose_name='jtitle',max_length=99, null=True, on_delete=models.CASCADE)
    date_time =  models.DateTimeField(verbose_name='date_time', null=True)