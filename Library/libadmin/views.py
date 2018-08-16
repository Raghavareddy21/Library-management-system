from django.shortcuts import render
from django.views import generic
from . import models
from libuser import models as model
from django.http import HttpResponse
from . import forms
import logging
import sys

def add_books(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			form = forms.BookaddForm(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponse("Book added")
		else:
			form=forms.BookaddForm()
			return render(request,'libadmin/addbook.html',{'form':form})
	else:
		return HttpResponse("You need to login to access the books")


def add_category(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			form =forms.add_category(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponse("Category added")
		else:
			form=forms.add_category()
			return render(request,'libadmin/addcategory.html',{'form':form})
	else:
		return HttpResponse("you need to login to access the categories")


def categorylist(request):
	if request.user.is_authenticated:
		categories = models.category.objects.all()
		return render(request, 'libadmin/Home.html',{'category_list':categories})
	else:
		return HttpResponse("you need to login to access categories")


def booklist(request,pk):
	if request.user.is_authenticated:
		book=models.category.objects.get(pk=pk)
		return render(request, 'libadmin/details.html',{'categories':book})
	else:
		return HttpResponse("you need to login to access books")


def notification(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			book=model.placerequest.objects.filter(accept=True)
			form =forms.notification(request.POST)
			if form.is_valid():
			 	form.save()
			 	return HttpResponse("the request has been accepted")
		else:
			form=forms.notification(request.POST,request.FILES)
			book=model.placerequest.objects.filter(accept=False)
			return render(request,'libadmin/notification.html',{'categories':book,'form':form})
	else:
		return HttpResponse("you need to login to accept the request")