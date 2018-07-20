from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
# Create your models here.
fs = FileSystemStorage(location='files/')
class booklist(models.Model):
	Title=models.CharField(max_length=200)
	Author=models.CharField(max_length=200)
	Category=models.CharField(max_length=100 )
	image=models.FileField(upload_to='pictures/')
	book=models.FileField(storage=fs)
	date=models.DateField()
	upload_date=models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.Title
