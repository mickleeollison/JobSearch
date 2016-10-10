from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jobsearch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'search.views.searchPage', name = 'searchPage'),
	url(r'^search/', 'search.views.search', name = 'search'),
	url(r'^applications/', 'applications.views.applications', name = 'applications'),
	url(r'^appRemove/(\d+)/', 'applications.views.appRemove', name = 'appRemove'),
	url(r'^login/', 'login.views.loginForm', name='loginForm'),
	url(r'^logout/', 'login.views.logout', name='logout'),
	url(r'^register/', 'login.views.registerForm', name='registerForm'),
	url(r'^submitlogin/', 'login.views.login',name='login'),
	url(r'^submitregister/', 'login.views.register',name='register'),
	url(r'^settings/', 'template.views.settings',name='settings'),
	url(r'^updateTemplate/', 'template.views.updateTemplate',name='updateTemplate'),
	url(r'^templates/','template.views.templates', name='templates'),
	url(r'^chooseTemplate/(\d+)/', 'template.views.chooseTemplate',name='chooseTemplate' ),
	url(r'^removeTemplate/(\d+)/', 'template.views.removeTemplate',name='removeTemplate' ),
)
