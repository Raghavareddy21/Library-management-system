from django.shortcuts import render
from django.views import generic
from libadmin.models import category
from libadmin.models import books
from libadmin import models
from . import forms
from django.http import HttpResponse


def categorylist(request):
	if request.user.is_authenticated:
		categories = models.category.objects.all()
		return render(request, 'libuser/Home.html',{'category_list':categories})
	else:
		return HttpResponse("you need to login to access categories")
def booklist(request,pk):
	if request.user.is_authenticated:
		book=models.category.objects.get(pk=pk)
		return render(request, 'libuser/booklist.html',{'categories':book})
	else:
		return HttpResponse("you need to login to access books")
def placerequest(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = forms.placerequest(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponse("Your request has been placed")
			else:
				return render(request, 'libuser/placerequest.html', {'form': form})
		else:
			form = forms.placerequest()
			return render(request, 'libuser/placerequest.html', {'form': form})
	else:
		return HttpResponse("You must login to place request")