from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    ad = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Ad'}))
    soyad = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Soyad'}))
