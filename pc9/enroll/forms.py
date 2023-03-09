from django import forms

class UserRegistrationForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    