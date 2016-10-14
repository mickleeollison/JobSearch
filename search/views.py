from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from search.forms import *
from search.firstDoc import *
from search.models import *
from login.models import User
from login.credentials import *
from template.currentTemplate import *
import re
from datetime import datetime
from django.views.static import serve
import os

# Create your views here.
def searchPage(request):
	if  not request.session.has_key('email'):
		return HttpResponseRedirect("/login")
	else:
		return render(request, "search/search.html",
		{'email':{'body':getCurrentEmailBody(request), 'subject': getCurrentEmailSubject(request)},
		'resume': getResume(getCurrentResume(request)), 'coverLetter': getCoverLetter(getCurrentCoverLetter(request)), 
		'plugins': getTemplate(request), 'user':request.session['email']})

def search(request):
	if  not request.session.has_key('email'):
		return HttpResponseRedirect("/login")
	else:
		kwargs={}
		for k in request.POST.keys():
			kwargs[k] = forms.CharField()
		# Creating the form object and manipulating/validating it
		form = DynForm() # Create the form
		form.setFields(kwargs) # Set the fields as defined in the kwargs dictionary
		form.setData(request.POST) # Set the form data
		form.validate(request.POST) # validate the from 

		application = Application(name = getCurrentTemplateName(request),
		resume = getCurrentResume(request), coverLetter=getCurrentCoverLetter(request),
		timeApplied="{:%B %d, %Y}".format(datetime.now()),
		emailBody=getCurrentEmailBody(request), emailSubject=getCurrentEmailSubject(request),
		user=User.objects.filter(email=request.session['email'])[0])
		application.save()

		sargs = {}
		for k, v in request.POST.items():
			if k != "csrfmiddlewaretoken":
				sargs[k] = v
				plugin = Plugin(key = k, value = v)
				plugin.application = application
				plugin.save()
		
		zipFile = submit(request, **sargs)
		zip_file = open(zipFile, 'rb')
		response = HttpResponse(content=zip_file)
		response['Content-Type'] = 'application/zip'
		response['Content-Disposition'] = 'attachment; filename=%s.zip' % (datetime.now().strftime("%Y%m%d") + getCurrentTemplateName(request)) 
		return response



