from django.shortcuts import render
from django.views import generic
from . import models
from django.http import HttpResponse
from . import forms
# Create your views here.
def books(request):
	if request.user.is_authenticated:
		books = models.booklist.objects.all()
		return render(request, 'libadmin/Home.html', {'booklist': books})
	else:
		return HttpResponse("You need to login to access books")

def booklist(request,pk):
	if request.user.is_authenticated:
		books =models.booklist.objects.get(pk=pk)
		return render(request,'libadmin/list.html',{'library':books})
	else:
		return HttpResponse("You need to login to access the books")
def add_books(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			form = forms.BookaddForm(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponse("Book added")
		else:
			form=forms.BookaddForm()
		return render(request,'',{'form':form})
	else:
		return HttpResponse("You need to login to access the books")
