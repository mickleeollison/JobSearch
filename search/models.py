from django.db import models
import random
from login.models import User

# Create your models here
class Application(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=240)
	resume = models.CharField(max_length=500)
	coverLetter = models.CharField(max_length=500)
	emailSubject = models.CharField(max_length=500)
	emailBody = models.CharField(max_length=1000)
	timeApplied = models.CharField(max_length=240)
	class Meta:
		db_table = "applications"

class Plugin(models.Model):
	application = models.ForeignKey(Application)
	key = models.CharField(max_length=240)
	value = models.CharField(max_length=1070)
	class Meta:
		db_table = "plugins"
		