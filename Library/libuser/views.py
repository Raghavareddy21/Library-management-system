from django.shortcuts import render
from django.views import generic
from libadmin.models import category
from libadmin.models import books
from libadmin import models
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

# Create your views here.
