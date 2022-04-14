from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import account_registration



class first_registration(ModelForm):
    class Meta:
        model = account_registration 
        #fields = ['email', 'password1', 'password2', 'photo', 'first_name', 'middle_name', 'last_name', 'address', 'cellphone', 'birthday']
        fields = '__all__' 
        labels = {'email': 'Email (This Will Be Your Login)',
                'password1': 'Password (1 A-Z, 1 no. and > 8 char)',
                'password2': 'Confirm your Password',
                'photo': 'Upload Photo',
                'last_name': 'Surname',
                'first_name': 'Last Name',
                'middle_name': 'Middle Name',
                'address': 'Address',
                'cellphone': 'Cellphone Number',
                'birthday': 'Birthday',
                }