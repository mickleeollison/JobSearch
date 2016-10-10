from django.db import models
from login.models import User

class Template(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=300)
	emailSubject = models.CharField(max_length=1070)
	emailBody = models.CharField(max_length=1070)
	resume = models.FileField(upload_to = 'documents')
	coverLetter = models.FileField(upload_to = 'documents')
	
	class Meta:
		db_table = "templates"
