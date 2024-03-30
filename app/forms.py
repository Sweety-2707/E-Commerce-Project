from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer,state_choices,Delivery_Address


class CustomerRegistrationForm(ModelForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}),required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    cpassword = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    class Meta:
        model=Customer
        fields=['first_name','last_name','email']


class LoginForm(ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    class Meta:
        model=User
        fields=['username','password']

class ChangePassword(ModelForm):
    password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    class Meta:
        model=User
        fields=['password']

class AddressForm(ModelForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    mobile = forms.IntegerField(label='Mobile No', widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    locality=forms.CharField(label='Locality', widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    city=forms.CharField(label='City', widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    state=forms.ChoiceField(label='State', widget=forms.Select(attrs={'class':'form-control'}),choices=state_choices,required=True)
    pincode=forms.IntegerField(label='Pincode', widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    class Meta:
        model=Delivery_Address
        fields=['first_name','last_name','mobile','locality','city','state','pincode']