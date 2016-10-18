from django.shortcuts import render, redirect
from login.credentials import *
from login.forms import *
from search.views import searchPage
from django.http import HttpResponse, HttpResponseRedirect

credentials = Credentials()

def loginForm(request):
	try:
		return render(request, "login/login.html", {'error':request.session['error']})
	except:
		return render(request, "login/login.html", {'error':None})

def login(request):
	MyLoginForm = LoginForm(request.POST)
	if MyLoginForm.is_valid():
		email=MyLoginForm.cleaned_data['email']
		password=MyLoginForm.cleaned_data['password']
		if credentials.validSignIn(email,password,request):
			request.session['email'] = email
			request.session['templateId'] = 0
			return redirect(searchPage)
		else:
			return redirect(loginForm)
	else:
		return redirect(loginForm)

def registerForm(request):
	try:
		return render(request, "login/register.html", {'error':request.session['error']})
	except:
		return render(request, "login/register.html", {'error':None})

def register(request):
	MyRegisterForm = RegisterForm(request.POST)
	if MyRegisterForm.is_valid():
		email=MyRegisterForm.cleaned_data['email']
		password=MyRegisterForm.cleaned_data['password']

		if not credentials.validRegistration(email, password,request):
			return redirect(registerForm)

		password = credentials.encryptPassword(password)
		newuser = User(email=email,password=str(password))
		newuser.save()
		return redirect(loginForm)
	else:
		return redirect(registerForm)
		
def logout(request):
	try:
		del request.session['email']
	except:
		pass
	request.session['error'] = None
	return redirect(loginForm)