"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Restaurant(models.Model):
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
	delivers = models.BooleanField(default=False)
	ifYouveNeverBeenHereTryThisFirst = models.CharField('If youve never been here before, try this',max_length=100,blank=True, default='')
	
	
	class Meta:
		ordering = ['name']
