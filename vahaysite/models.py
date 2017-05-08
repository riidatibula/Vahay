# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


# Create your models here.

class Vahay(models.Model):
	owner = models.ForeignKey(AUTH_USER_MODEL)
	name = models.CharField(max_length=255)
	rent_range = models.CharField(max_length=100)
	category = models.CharField(max_length=100)
	contact_details = models.CharField(max_length=100)
	rating = models.IntegerField(default=0)
	location = models.CharField(max_length=255)
	available = models.BooleanField(default=1)