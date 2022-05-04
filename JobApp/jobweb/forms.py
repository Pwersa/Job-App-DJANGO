from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *


class first_registration(ModelForm):

    class Meta:
        model = account_registration 
        #fields = ['email', 'password1', 'password2', 'photo', 'first_name', 'middle_name', 'last_name', 'address', 'cellphone', 'birthday']
        fields = '__all__' 

        widgets = {'password1': forms.PasswordInput(), 'password2': forms.PasswordInput()}
        labels = {'email': 'Email (This Will Be Your Login)',
                'password1': 'Password',
                'password2': 'Confirm your Password',
                'photo': 'Upload 1x1 Photo',
                'last_name': 'Surname',
                'first_name': 'First Name',
                'middle_name': 'Middle Name',
                'address': 'Address',
                'cellphone': 'Cellphone Number',
                'birthday': 'Birthday',
                'applyingfor': 'Applying For:'
                }


class second_registration(ModelForm):
    class Meta:
        model = other_info
        #fields = ['email', 'password1', 'password2', 'photo', 'first_name', 'middle_name', 'last_name', 'address', 'cellphone', 'birthday']
        fields = '__all__'
