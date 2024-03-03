from django import forms
from .models import post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, SetPasswordForm
from django.contrib.auth.forms import User
from django.utils.translation import gettext, gettext_lazy as _

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {"first_name":"First Name", 
                  "last_name":"Last_Name",
                  "email":"Email"}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                   'first_name':forms.TextInput(attrs={'class':'form-control'}),
                   'last_name':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.EmailInput(attrs={'class':'form-control'}),
                   }
        

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control', 'autofocus':True}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'class':'form-control', 'autocomplete':True}))


class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title', 'disc']
        labels = {'title':'Title', 'disc':'Description'}
        
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                   'desc':forms.Textarea(attrs={'class':'form-control'}),
                   }