from django import forms


class TemplateForm(forms.Form):
	tname = forms.CharField()
	emailSubject = forms.CharField()
	emailBody = forms.CharField()
	resume = forms.FileField()
	coverLetter = forms.FileField()