from django.db import models

class Bikes(models.Model):
	bike_name = models.CharField(max_length=15)
	launch_date = models.CharField(max_length=20)
	bike_desc = models.CharField(max_length=500)
	review = models.CharField(max_length=250)
	
	
	def __unicode__(self):
		return self.bike_name
	
	

class Next(models.Model):
	bike_name = models.CharField(max_length=15)
	launch_date = models.CharField(max_length=20)
	bike_desc = models.CharField(max_length=500)
	review = models.CharField(max_length=250)
	
	
	def __unicode__(self):
		return self.bike_name
	

