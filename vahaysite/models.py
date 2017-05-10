# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Vahay(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	rent_range = models.CharField(max_length=100)
	category = models.CharField(max_length=100)
	contact_details = models.CharField(max_length=100)
	rating = models.IntegerField(default=0)
	location = models.CharField(max_length=255)
	available = models.BooleanField(default=1)

	def __str__(self):
		return self.name + " - " + self.location

	def isAvailable(self):
		if self.available == 1:
			return True
		else:
			return False


class Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.CharField(max_length=500)

	def __str__(self):
		return self.user.username + " - " + self.comment

