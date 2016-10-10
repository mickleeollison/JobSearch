from django.shortcuts import render, redirect
from template.forms import *
from template.models import *
from django.http import HttpResponse, HttpResponseRedirect
import re
from template.currentTemplate import *

def settings(request):
	if  not request.session.has_key('email'):
		return HttpResponseRedirect("/login")
	else:
		return render(request, "templates/settings.html")

def updateTemplate(request):
	if  not request.session.has_key('email'):
		return HttpResponseRedirect("/login")
	else:
		if request.method == "POST":
			#Get the posted form
			MyTemplateForm = TemplateForm(request.POST, request.FILES)
			if MyTemplateForm.is_valid():
				template = Template()
				template.name = MyTemplateForm.cleaned_data["tname"]
				template.emailSubject = MyTemplateForm.cleaned_data['emailSubject']
				template.emailBody = MyTemplateForm.cleaned_data['emailBody']
				template.resume = MyTemplateForm.cleaned_data["resume"]
				template.coverLetter = MyTemplateForm.cleaned_data["coverLetter"]
				template.user = User.objects.filter(email=request.session['email'])[0]
				template.save()
		else:
			MyTemplateForm = Templateform()		
		return redirect(settings)

def templates(request):
	if  not request.session.has_key('email'):
		return HttpResponseRedirect("/login")
	else:
		return render(request, "templates/templates.html",
		 {"templates" : getTemplates(request), 'currentTemplate': int(request.session['templateId'])})

def chooseTemplate(request,id):
	if  not request.session.has_key('email'):
		return HttpResponseRedirect("/login")
	else:
		request.session['templateId'] = id
		return redirect(templates)
	
def removeTemplate(request,removeId):
	if  not request.session.has_key('email'):
		return HttpResponseRedirect("/login")
	else:
		Template.objects.get(id = removeId).delete()
		return redirect(templates)

