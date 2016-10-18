
# Create your models here.
import bcrypt
from Crypto.Cipher import AES
from login.models import *
import re

class Credentials:
	"class for logging in and registering users"

	def encryptPassword(self,unencrypted_password):
		# Encryption
		salt = bcrypt.gensalt()
		password = bcrypt.hashpw(str(unencrypted_password), salt)
		return password

	def validSignIn(self,email, unencrypted_password, request):
		exists = User.objects.filter(email =email).exists()
		if not exists:
			request.session['error'] = "User does not exist"
			return False
		password = User.objects.filter(email = email)[0].password
		try:
			if  password == bcrypt.hashpw(str(unencrypted_password).encode('utf-8'), password.encode('utf-8')):
				return True
			else:
				request.session['error'] = "Password Incorrect"
				return False
		except:
			Credentials.error = None
			return False

	def validRegistration(self, email, unencrypted_password, request):
		user = User.objects.filter(email =email).exists()
		if user:
			request.session['error'] = "User name in use"
			return False
		if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$', unencrypted_password):
			request.session['error'] = "Password must be 8 characters long and contain a letter, number, and special character"
			return False
		else:
			request.session['error'] = None
			return True