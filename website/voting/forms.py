from django.contrib.auth.models import User
from django import forms
from .models import candidate

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
      model=User
      fields=['username' ,'password']

class CandidateAdd(forms.ModelForm):
    class Meta:
      model=candidate
      fields = ['name', 'logo', 'political_party', 'quote', 'photo', 'area']