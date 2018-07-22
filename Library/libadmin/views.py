from django.shortcuts import render
from django.views import generic
from . import models
from django.http import HttpResponse
from . import forms

def add_books(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			form = forms.BookaddForm(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponse("Book added")
		else:
			form=forms.BookaddForm()
			return render(request,'addbook.html',{'form':form})
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
			return render(request,'addcategory.html',{'form':form})
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
		return render(request, 'libadmin/booklist.html')
	else:
		return HttpResponse("you need to login to access books")
