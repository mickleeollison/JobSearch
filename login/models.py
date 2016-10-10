from django.db import models

class User(models.Model):
	email = models.CharField(max_length=300)
	password = models.CharField(max_length=1070)
	
	class Meta:
		db_table = "users"
