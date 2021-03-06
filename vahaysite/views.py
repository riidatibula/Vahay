# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout

from .models import Vahay

# Create your views here.


def home(request):
	all_vahay = Vahay.objects.all()
	context={
		'all_vahay': all_vahay
	}

	if request.user.is_authenticated:
		return render(request, 'vahaysite/homepage.html', context=context)

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


def logout_view(request):
	logout(request)
	return render(request, 'vahaysite/signin.html')


def profile(request, username):
	return render(request, 'vahaysite/profile.html')


def addVahay(request, username):
	return render(request, 'vahaysite/addVahay.html')

def vahayDetails(request, username, pk):
	vahay = get_object_or_404(Vahay, pk=pk)
	return render(request, 'vahaysite/vahayDetails.html', {'vahay': vahay})


