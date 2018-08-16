from django.db import models
from django.utils import timezone
from datetime import datetime,timedelta
from django.core.files.storage import FileSystemStorage
from libadmin.models import category
from libadmin.models import books
from dateutil.parser import parse
from django.contrib.auth.models import User
# Create your models here.
class placerequest(models.Model):
	Username=models.CharField(max_length=200,default=User)
	book_category=models.ForeignKey(category,on_delete=models.CASCADE)
	book=models.ForeignKey(books,on_delete=models.CASCADE,primary_key=True)
	request_date=models.DateTimeField(default=timezone.now())
	submition_date=models.DateTimeField(default=datetime.now()+timedelta(days=30))
	accept=models.BooleanField(default=False)
	
	def __str__(self):
		return self.book.Title
