from django.db import models

#create your models here.

class KirrURL(models.Model):
	url = models.CharField(max_length=220)
	shortcode =  models.CharField(max_length=15, unique=True)
	#shortcode = models.CharField(max_length=15, null=True) Empty in database is okay
	#shortcode = models.CharField(max_length=15, default='cfedefaultshortcode')

	def __str__(self):
			return str(self.url)

	def __unicode__(self):
		return str(self.url)



# when you make changes
#1.python manage.py makemigrations
#2.python manage.py migrate
#3.python manage.py createsuperuser


