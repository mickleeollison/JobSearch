from django import forms

class LoginForm(forms.Form):
	email = forms.CharField()
	password = forms.CharField()

class RegisterForm(forms.Form):
	email = forms.CharField()
	password = forms.CharField()