
# Create your models here.
import bcrypt
from Crypto.Cipher import AES
from login.models import *


def encryptPassword(unencrypted_password):
	# Encryption
	salt = bcrypt.gensalt()
	password = bcrypt.hashpw(str(unencrypted_password), salt)
	print password
	return password

def validSignIn(email, unencrypted_password):
	exists = User.objects.filter(email =email).exists()
	if not exists:
		return False
	password = User.objects.filter(email = email)[0].password
	try:
		if  password == bcrypt.hashpw(str(unencrypted_password).encode('utf-8'), password.encode('utf-8')):
			return True
		else:
			return False
	except:
		return False

def userNameInUse(email):
	user = User.objects.filter(email =email).exists()
	if user:
		return True
	else:
		return False