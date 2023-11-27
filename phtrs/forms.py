from django import forms
from django.contrib.auth.models import User
from . import models


# for admin signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


# for student related form
class WorkerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class WorkerForm(forms.ModelForm):
    class Meta:
        model = models.Worker
        fields = ['address', 'mobile', 'status']


# for teacher related form
class CitizenUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class CitizenForm(forms.ModelForm):
    class Meta:
        model = models.Citizen
        fields = ['address', 'mobile', 'status']

class CitizenSubmitHoleForm(forms.ModelForm):
    priority = forms.IntegerField(initial=0, required=False)
    status=forms.CharField(initial="not repair",required=False)
    class Meta:
        model =models.Hole
        fields = ['street', 'size','position','area']



