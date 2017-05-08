# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
	if request.user.is_authenticated:
		return render(request, 'vahaysite/homepage.html')

	context={}
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return render(request, 'vahaysite/homepage.html', context=context)
		else:
			context['error_message'] = 'wrong username or password'
			context['username'] = username
				
	return render(request, 'vahaysite/signin.html', context = context)
