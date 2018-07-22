from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
# Create your models here.
fs = FileSystemStorage(location='files/')
class category(models.Model):
	name=models.CharField(max_length=200)
	about=models.CharField(max_length=250)
	img=models.FileField(upload_to='pictures/')
	date=models.DateField()
	upload_date=models.DateTimeField(default=timezone.now())
	status=models.BooleanField(default=True)

	def __str__(self):
		return self.name

class books(models.Model):
	book_category= models.ForeignKey( category, on_delete=models.CASCADE )
	Title=models.CharField(max_length=200)
	Author=models.CharField(max_length=200)
	image=models.FileField(upload_to='pictures/')
	book=models.FileField(storage=fs)
	date=models.DateField()
	upload_date=models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.Title
