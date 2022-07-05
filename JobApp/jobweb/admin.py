from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

class account_registration_admin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'applyingfor', 'account_type', 'date_joined']

class other_info_admin(admin.ModelAdmin):
    list_display = ['username']

class job_listing_admin(admin.ModelAdmin):
    list_display = ['jtitle', 'jdesc']


admin.site.site_header = 'Job Web App Dashboard'
admin.site.register(account_registration, account_registration_admin)
admin.site.register(job_listing, job_listing_admin)
admin.site.register(other_info, other_info_admin)
admin.site.unregister(Group)



# Register your models here.
