from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User

class dform(forms.ModelForm):
    caption=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Write Something Here','rows':20,'cols':150,'style':'resize:none;width:300px;','class':'form-control'}))
    pic=forms.FileField(required=False)
    class Meta:
        model=blog
        fields='__all__'
        exclude=['username']




# class PasswordChangeForm(forms.ModelForm):
#     old_password=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Write Something Here','rows':4,'cols':50,'style':'resize:none;width:300px;','class':'form-control'}))
#     new_password=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Write Something Here','rows':4,'cols':50,'style':'resize:none;width:300px;','class':'form-control'}))
#     confirm_password=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Write Something Here','rows':4,'cols':50,'style':'resize:none;width:300px;','class':'form-control'}))
#
#     class Meta:
#         model=User
#         fields=['old_password','new_password','confirm_password']