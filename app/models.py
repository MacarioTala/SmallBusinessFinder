"""
Definition of models.
"""

from django.db import models
#helper functions
def get_display(key, list):
    d = dict(list)
    if key in d:
        return d[key]
    return None

# Create your models here.
class Restaurant(models.Model):
	DELIVERY_CHOICES = (("DELIVERY","Delivery"),("TAKEOUT","TakeOut"))
	
	name = models.CharField(max_length=100,blank=True, default='')
	description = models.TextField(default='')
	cuisine = models.TextField(default='')
	address = models.TextField(default='')
	city = models.CharField(max_length=100,blank=True, default='')
	state = models.CharField(max_length=100,blank=True, default='')
	phoneNumber = models.CharField(max_length=100,blank=True, default='')
	startTime= models.TimeField(auto_now=False,null=True)
	endTime= models.TimeField(auto_now=False,null=True)
	monday = models.BooleanField(default=True)
	tuesday = models.BooleanField(default=True)
	wednesday = models.BooleanField(default=True)
	thursday = models.BooleanField(default=True)
	friday = models.BooleanField(default=True)
	saturday = models.BooleanField(default=True)
	sunday = models.BooleanField(default=True)
	delivers = models.CharField(choices=DELIVERY_CHOICES,default="TAKEOUT",max_length=10)
	ifYouveNeverBeenHereTryThisFirst = models.CharField('If youve never been here before, try this',max_length=100,blank=True, default='')
	isLive = models.BooleanField(default=False)
	
	def delivers_verbose(self):
		return get_display(self.delivers,DELIVERY_CHOICES)

	def validate(self):
		isValid = True
		if self.id != 0:
			isValid=False
			model_error = "NotUnique"
		return isValid
	
	class Meta:
		ordering = ['name']
