from django.shortcuts import render, redirect
from login.credentials import *
from login.forms import *
from search.views import searchPage
from django.http import HttpResponse, HttpResponseRedirect


def loginForm(request):
	return render(request, "login/login.html")

def login(request):
	MyLoginForm = LoginForm(request.POST)
	if MyLoginForm.is_valid():
		email=MyLoginForm.cleaned_data['email']
		password=MyLoginForm.cleaned_data['password']
	if validSignIn(email,password):
		request.session['email'] = email
		request.session['templateId'] = 0
		return redirect(searchPage)
	else:
		return redirect(loginForm)

def registerForm(request):
	return render(request, "login/register.html")

def register(request):
	MyRegisterForm = RegisterForm(request.POST)
	if MyRegisterForm.is_valid():
		email=MyRegisterForm.cleaned_data['email']
		password=MyRegisterForm.cleaned_data['password']

		if userNameInUse(email):
			return redirect(registerForm)

		password = encryptPassword(password)
		print str(password)
		newuser = User(email=email,password=str(password))
		newuser.save()
	return redirect(loginForm)

def logout(request):
	try:
		del request.session['email']
	except:
		pass
	return redirect(loginForm)