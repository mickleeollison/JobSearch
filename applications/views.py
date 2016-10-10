from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from search.models import *
from login.models import User

def applications(request):
	if  not request.session.has_key('email'):
		return HttpResponseRedirect("/login")
	else:
		today = datetime.datetime.now().date()
		user = User.objects.filter(email = request.session['email'])[0]
		pastApplications = Application.objects.filter(user = user)
		applications = []
		for a in pastApplications:
			plugins = Plugin.objects.filter(application_id = a.id)
			application = {}
			for kv in plugins:
				application[kv.key] = kv.value
				application['name'] = a.name
				application['id'] = a.id
				application['timeApplied'] = a.timeApplied
				application['resume'] = a.resume
				application['coverLetter'] = a.coverLetter
				application['emailSubject'] =  a.emailSubject
				application['emailBody'] = a.emailBody
			applications.append(application)
		return render(request, "applications.html", {"applications" : applications})

def appRemove(request, appId):
	if  not request.session.has_key('email'):
		return HttpResponseRedirect("/login")
	else:
		instance = Application.objects.get(id=appId)
		instance.delete()	
		return redirect(applications)
